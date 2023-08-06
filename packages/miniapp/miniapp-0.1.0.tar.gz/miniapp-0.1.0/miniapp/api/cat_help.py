"""
API category to support searchable help pages.
"""
import os
import re
import mimetypes
import whoosh.index
import whoosh.fields
import whoosh.highlight
import whoosh.qparser
import tempfile
import time
import shutil
import threading
import io
import zipfile
import markdown

from miniapp.api.base import endpoint
from miniapp.api.cat_base import ApiCategoryBase
from miniapp.errs import BadRequest
from miniapp.utils.file_utils import T_DIR_ENTRY, store_file, walk_all, normalize_path
from miniapp.utils.generic_obj import make_object


class HelpDocInterface(object):
    """
    Interface to r/w help documents.
    """
    def __init__(self):
        self.index_folder = None
        self.build_lock = threading.Lock()
        self.index = None

    PTN_INCLUDE_FILES_IN_INDEX = re.compile(r'.*\.(txt|md)$')

    def read(self, path: str):
        """
        Read content.  If 'path' is a directory, returns a directory listing, otherwise returns raw binary content.
        Returns None if file does not exist, a [] for the directory listing, or bytes or a binary stream.  In the
        directory listing, a list of {}s is returned with one field: "name".  Directory names must end with "/".
        """

    def write(self, path: str, content):
        """
        Store help content.
        """

    def commit(self, path: str, commit_message: str=None):
        """
        Commit changed files.
        :returns:   True if there was a conflict.  User's changes may be overwritten depending on how conflict
                    resolution is implemented.
        """
        return False

    def walk(self, path: str=""):
        """
        Enumerate files & directories.  Returns an iteration of T_DIR_ENTRY.
        """
        for file in self.read(path):
            is_dir = file["name"].endswith("/")
            name = file["name"].strip("/")
            full = os.path.join(path, name)
            yield T_DIR_ENTRY(name, full, full, lambda: is_dir, None, None)
            if is_dir:
                subf = os.path.join(path, file["name"])
                for sub in self.walk(subf):
                    yield sub

    def build_index(self):
        """
        Build the index so that searches can happen.
        """
        with self.build_lock:
            new_index_folder = tempfile.mkdtemp()
            schema = whoosh.fields.Schema(path=whoosh.fields.ID(stored=True), content=whoosh.fields.TEXT(stored=True))
            index = whoosh.index.create_in(new_index_folder, schema)
            writer = index.writer()
            for f in self.walk():
                if f.is_dir():
                    continue
                if not self.PTN_INCLUDE_FILES_IN_INDEX.match(f.name):
                    continue
                content = self.read(f.name)
                if hasattr(content, "read"):
                    fh = content
                    content = fh.read()
                    fh.close()
                if isinstance(content, (bytes, bytearray)):
                    content = content.decode("utf-8", errors="ignore")
                writer.add_document(path=f.name, content=content)
            writer.commit()
            self.index_folder = new_index_folder
            self.index = index

    def search(self, query: str):
        """
        Perform search.
        """
        if query and len(query) > 160:
            raise BadRequest(message="query too long")
        if not self.index_folder:
            raise Exception("build index first")
        if not self.index and self.index_folder:
            self.index = whoosh.index.open_dir(self.index_folder)
        with self.index.searcher() as searcher:
            query = whoosh.qparser.QueryParser("content", self.index.schema).parse(query)
            results = searcher.search(query)
            results.fragmenter = whoosh.highlight.SentenceFragmenter()
            for result in results:
                snippets = result.highlights("content")
                yield {"score": result.score, "file": result["path"], "snippet": snippets}

    def close(self):
        """
        Clean up.
        """
        if self.index_folder:
            shutil.rmtree(self.index_folder)


class HelpDocInterface_Folder(HelpDocInterface):
    def __init__(self, folder: str):
        super(HelpDocInterface_Folder, self).__init__()
        self.folder = folder

    def read(self, path: str):
        full_path = os.path.join(self.folder, path)
        if not os.path.exists(full_path):
            return
        if os.path.isdir(full_path):
            out = []
            for f in os.listdir(full_path):
                sub = os.path.join(full_path, f)
                if os.path.isdir(sub):
                    f += "/"
                out.append({"name": f})
            return out
        return open(full_path, mode='rb')

    def write(self, path: str, content):
        full_path = os.path.join(self.folder, path)
        if os.path.isdir(full_path):
            raise BadRequest(message="is a directory: %s" % path)
        parent_dir = os.path.dirname(full_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
        store_file(full_path, content)

    def walk(self, path: str=""):
        full_path = os.path.join(self.folder, path)
        for f in walk_all(full_path):
            yield f


def generate_help_category(api, search_permission, write_permission, folder_or_intf: (str, HelpDocInterface), sequence: int=1000):
    """
    Generate an API category which manages help files.
    :param api:     API which will support help documents.
    :param search_permission:  Permission required for searching.
    :param write_permission:  Permission required for writes.
    :param folder_or_intf:  Where files are stored.  Or an implementation of HelpDocInterface.
    :param sequence:  Sequence of this category in the overall API.
    """
    interface = HelpDocInterface_Folder(folder_or_intf) if isinstance(folder_or_intf, str) else folder_or_intf
    build_lock = threading.Lock()

    class HelpDocs(ApiCategoryBase):
        DESCRIPTION = "Access to help documents."

        def __init__(self, api):
            super(HelpDocs, self).__init__(api, sequence=sequence)
            self.modified = False

        @endpoint("get", "docs/{path:*}", sequence=1)
        def read_help(self, path: str):
            """
            Serve up files from the help system.
            """
            path = normalize_path(path, safe=True)
            content = interface.read(path)
            if content is None:
                return
            if isinstance(content, list):
                return content
            # send file content for files
            return content, mimetypes.guess_type(path)[0]

        @endpoint("put", "docs/{path:*}", permission_required=write_permission, sequence=100)
        def write_help(self, path: str, post_data, commit: str=None):
            """
            Modify files in the help system.  The changes are made to the local filesystem and do not persist on their
            own.  The help documents can be mapped to a persistent volume, or they can be archived in some other way.
            :param path:        Where to write the file, relative to the root of the help system.
            :param post_data:   Data to write.
            :param commit:      If given, the changes are committed and the supplied string is used as the commit
                                message.
            """
            path = normalize_path(path, safe=True)
            interface.write(path, post_data)
            self.modified = True
            conflict = False
            if commit is not None:
                conflict = interface.commit(path, commit_message=commit)
            return make_object(conflict=conflict)

        def _build_if_needed(self):
            with build_lock:
                if interface.index_folder is None or self.modified:
                    self.modified = False
                    t0 = time.time()
                    self.api.log("rebuilding help index")
                    interface.build_index()
                    self.api.log("  rebuilt in %.3fs" % (time.time() - t0))

        @endpoint("get", "search", permission_required=search_permission, sequence=2)
        def search_help(self, query: str):
            """
            Search help documentation.
            """
            self._build_if_needed()
            results = list(interface.search(query))
            return make_object(results=results)

        @endpoint("get", "download", permission_required=write_permission, sequence=200, response_type="raw")
        def download_help(self, format: str="html", subfolder: str=""):
            """
            Download all of help (or a subset), as HTML.
            """
            if format != "html":
                raise BadRequest(message=f"unsupported export format: {format}")
            site_host = ""
            cfg = self.api.get_config() if self.api and hasattr(self.api, "get_config") else None
            if cfg:
                site_host = cfg.get_app_url()
                if site_host:
                    site_host = site_host.strip("/")
                    if "://" in site_host:
                        site_host = site_host.split("://")[1]
            def file_iterator():
                for f in interface.walk():
                    if not f.name:
                        continue
                    data = None
                    if not f.is_dir():
                        data = interface.read(f.path)
                        if hasattr(data, "read"):
                            data = data.read()
                    yield f.name, data
            zipped = help_to_html(file_iterator(), subfolder=subfolder, site_host=site_host)
            return zipped, "application/zip"

    return HelpDocs(api)


def help_to_html(file_iterator, subfolder: str=None, site_host: str=None):
    """
    Convert markdown files to HTML.

    :param file_iterator:       Iterates tuples of (filename, content).
    :param subfolder:           Restricts content to a particular subfolder.
    :param site_host:           Hostname to fill in with links that point to parts of the application.
    """
    return HelpConverter(subfolder=subfolder, site_host=site_host).create_zip(file_iterator)


class HelpConverter(object):
    """
    Conversion of help system into HTML.
    """
    PREFIX_CONTENT = "/api/v1/help/docs/"
    PREFIX_HELPREF = "/help/"
    PTN_APP_LINKS = re.compile(r'^/(?!(/api/v1/help/docs/|/help)).*$')

    def __init__(self, subfolder: str=None, site_host: str=None):
        """
        Prepare to convert.

        :param subfolder:   Optionally captures a sub-portion of the help system.
        :param site_host:   Hostname of described system, so that 'application links' will work.
        """
        subfolder = subfolder or ""
        if subfolder and not subfolder.endswith("/"):
            subfolder += "/"
        self.subfolder = subfolder
        self.site_host = site_host
        self.zip_stream = None

    def create_zip(self, file_iterator):
        """
        Generate a ZIP of the converted HTML.

        :param file_iterator:  An iterator over (file name, file content)
        """
        all_files = list(file_iterator)
        buf = io.BytesIO()
        # scan for CSS
        css_file = None
        for file_path, file_content in all_files:
            if file_path == "common.css":
                css_file = file_path
        with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zip_writer:
            for file_path, file_content in all_files:
                self.convert_file(zip_writer, file_path, file_content, css_file=css_file)
        return buf.getvalue()

    def convert_file(self, zip_writer, file_path, file_content, css_file: str):
        """
        Process one file.
        """
        if not file_path.startswith(self.subfolder) and file_path != css_file:
            return
        if file_content is None:
            return
        file_path_out = file_path
        if self.subfolder and file_path_out.startswith(self.subfolder):
            file_path_out = file_path_out[len(self.subfolder):]
        if file_path.endswith(".md"):
            file_path_out = re.sub(r'\.md$', ".html", file_path_out)
            if isinstance(file_content, (bytes, bytearray)):
                file_content = file_content.decode("utf-8")
            file_content = markdown.markdown(file_content)
            # work out prefix to reach resources in the help root
            folder_depth = len(file_path_out.strip("/").split("/"))
            to_root = "../" * (folder_depth - 1)
            # insert CSS reference
            if css_file:
                file_content = f'<link rel="stylesheet" href="{to_root}{css_file}"/>\n' + file_content
            # patch the links
            out = []
            pos = 0
            for m in re.finditer(r'(?:<a href="(.*?)">|<img\s+(?:[^/>]*\s)src="(.*?)"[^/>]*/?>)', file_content):
                out.append(file_content[pos:m.start()])
                href = m.group(1) or m.group(2)
                reg = m.regs[1] if m.group(1) else m.regs[2]
                if href.startswith(self.PREFIX_CONTENT):
                    # references to images and other static content reference the help download API
                    href = href[len(self.PREFIX_CONTENT):]
                elif href.startswith(self.PREFIX_HELPREF) and href.endswith(".md"):
                    # links to other help pages start with the help browsing base URL
                    href = href[len(self.PREFIX_HELPREF):]
                    if self.subfolder and href.startswith(self.subfolder):
                        href = href[len(self.subfolder):]
                    href = re.sub(r'\.md$', ".html", href)
                elif self.PTN_APP_LINKS.match(href):
                    # links to various places in the application: prepend hostname of the application
                    if self.site_host:
                        href = "https://" + self.site_host + ("" if href.startswith("/") else "/") + href
                out.append(file_content[m.start():reg[0]])
                out.append(href)
                out.append(file_content[reg[1]:m.end()])
                pos = m.end()
            out.append(file_content[pos:])
            file_content = "".join(out)
        zip_writer.writestr(file_path_out, file_content)
