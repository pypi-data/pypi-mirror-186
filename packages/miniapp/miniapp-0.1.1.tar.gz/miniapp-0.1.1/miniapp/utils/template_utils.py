try:
    import jinja2
except:
    jinja2 = None
import os
import json
import sys

ENGLISH = "en"
DEFAULT_LANGUAGE = ENGLISH


class Templates(object):
    """
    Wrapper around jinja2.
    """
    def __init__(self, folder: str):
        self.root = folder
        self.custom_functions = {}
        self.environment_cache = {}

    def _create_template_loader(self):
        inst = self

        class TemplateLoader(jinja2.BaseLoader):
            """
            Simple template loader.  Normal paths are checked relative to the template root, but for testing, an absolute
            path can be given (starts with /) to point elsewhere.
            """
            def __init__(self, env_path):
                self.root = inst.root
                self.envPath = env_path

            def get_source(self, environment, requestedPath, justChecking=False):
                full_path = requestedPath if requestedPath.startswith("/") else os.path.join(self.root, requestedPath)
                if not os.path.exists(full_path):
                    if justChecking:
                        return "", None, False
                    print("template not found: {}".format(requestedPath), file=sys.stderr)
                    return "template not found: {}".format(full_path), None, False
                mtime = os.path.getmtime(full_path)
                with open(full_path, 'r') as f:
                    source = f.read()
                return source, full_path, lambda: mtime == os.path.getmtime(full_path)
        return TemplateLoader(None)

    def get_environment(self, language: str=None):
        """
        Get a templating environment for the given language.  Translation messages will come from the language-specific
        JSON file.
        """
        language = language or DEFAULT_LANGUAGE
        if language not in self.environment_cache:
            lang_file = os.path.join(self.root, language.lower() + ".json")
            env = jinja2.Environment(
                loader=self._create_template_loader(),
                extensions=['jinja2.ext.i18n'],
                autoescape=lambda templateName: templateName and templateName.endswith(".html")
            )
            env.globals.update(self.custom_functions)
            if hasattr(env, "install_gettext_translations"):
                env.install_gettext_translations(TemplateTranslations(lang_file))
            self.environment_cache[language] = env
        return self.environment_cache[language]

    def template_exists(self, path):
        """
        Test whether a given template exists.
        """
        templ, _, _ = self._create_template_loader().get_source(None, path, justChecking=True)
        return bool(templ)

    def render(self, template_path: str, template_data: dict=None, language: str=None):
        env = self.get_environment(language or ENGLISH)
        templ = env.get_template(template_path)
        return templ.render(**(template_data or {})).strip()


class TemplateTranslations(object):
    def __init__(self, lang_file):
        self.mtime = -1
        self._trans = None
        self.lang_file = lang_file

    @property
    def trans(self):
        cur_time = os.path.getmtime(self.lang_file) if os.path.exists(self.lang_file) else 0
        if cur_time != self.mtime:
            self.mtime = cur_time
            with open(self.lang_file, 'r') as f_r:
                self._trans = json.load(f_r) if cur_time else None
        return self._trans or {}

    def ugettext(self, message):
        return self.trans.get(message, message)

    def ungettext(self, singular, plural, n):
        if n == 1:
            return self.trans.get(singular, singular)
        else:
            return self.trans.get(plural, plural)
