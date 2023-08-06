from guppy import hpy
import gc

from miniapp.api.base import endpoint
from miniapp.api.cat_base import ApiCategoryBase
from miniapp.utils.generic_obj import make_object


def generate_mem_leak_category(api, permission_required, sequence=1000):
    """
    Generate an API category which tests for memory leaks.
    """
    class MemLeaks(ApiCategoryBase):
        """
        Analyze memory leaks.
        """
        DESCRIPTION = "Memory leak analysis"

        def __init__(self, api):
            super(MemLeaks, self).__init__(api, sequence=sequence)
            self.hp = hpy()
            self.heap = None
            self.diff = None

        '''
        @endpoint("get", "leak")
        def leak(self):
            """
            Placeholder endpoint for testing memory leaks.
            """
            return make_object(note="this is an endpoint to call repeatedly -- fill in with code to test for memory leaks, or make other calls")
        '''

        @endpoint("get", "start", permission_required=permission_required, sequence=1)
        def start(self):
            """
            Mark the start of memory leak detection.  The memory heap is captured and everything allocated up to this
            point will be ignored.  Call end() next.
            """
            gc.collect()
            self.heap = self.hp.heap()
            return make_object(note="now call end()")

        @endpoint("get", "end", permission_required=permission_required, sequence=2)
        def end(self):
            """
            Capture memory leaks.  Call start() first, then once some memory has leaked call this method.
            """
            gc.collect()
            self.diff = self.hp.heap() - self.heap
            return make_object(note="now call look()")

        @endpoint("get", "look/{mode:*}", permission_required=permission_required, sequence=3)
        def look(self, mode: str):
            """
            Generates an HTML page showing memory allocated between start() and end().  Open this in a separate tab.
            """
            if not self.diff:
                return "Please call start()/end() first", "text/plain"
            path = self.api.current_request().path
            mode = mode.strip("/")
            view = self.diff
            for part in mode.split("/"):
                if not part:
                    continue
                if part.isdigit():
                    view = view[int(part)]
                    continue
                if not hasattr(view, part):
                    return "No attribute '%s'" % part, "text/plain"
                view = getattr(view, part)
            out = "<pre>%s</pre>\n<hr/>\n" % str(view)
            # suggestions
            for opt in ["byid", "byrcs", "bytype", "referrers", "theone"]:
                try:
                    if hasattr(view, opt):
                        out += "<a href='{path}/{opt}'>{opt}</a><br/>\n".format(path=path, opt=opt)
                except Exception:
                    pass
            if not mode.endswith("/theone"):
                out += ", ".join("<a href='{path}/{opt}'>[{opt}]</a>\n".format(path=path, opt=n) for n in range(9))
            out += "<br/>"
            if mode:
                out += "<a href='..'>UP</a>, "
                top = path[:len(path) - len(mode)]
                out += "<a href='%s'>TOP</a>" % top
            return out, "text/html"

        @endpoint("get", "gc", permission_required=permission_required, sequence=10)
        def gc_info(self):
            return make_object(
                counts=gc.get_count(),
                thresholds=gc.get_threshold(),
                stats=gc.get_stats(),
                freeze_count=gc.get_freeze_count()
            )

        @endpoint("post", "gc", permission_required=permission_required, sequence=12)
        def gc_collect(self, generation: int=2):
            gc.collect(generation)
            return make_object()

    return MemLeaks(api)
