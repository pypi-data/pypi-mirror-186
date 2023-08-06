from collections import defaultdict

from miniapp.comm.http import MIME_JSON


class ApiSwagger(object):
    """
    Swagger generator for MiniREST.
    """
    def __init__(self, rest_intf, title: str="", version: str="...", server_url: str="?", include_docs: bool=True, enable_authenticated_calls: bool=True):
        self.rest_intf = rest_intf
        self.title = title
        self.version = version
        self.server_url = server_url
        self.include_docs = include_docs
        self.enable_authenticated_calls = enable_authenticated_calls

    def gather_categories(self):
        categories = []
        cat_names = set()
        for handlers in self.rest_intf.handlers.values():
            for h_i in handlers:
                if not h_i.spec:
                    continue
                if not self.enable_authenticated_calls and self.rest_intf.handler_requires_authentication(h_i.handler_fn):
                    continue
                h_j = h_i.spec_json(include_docs=self.include_docs)
                category = h_j["category"]
                if category in cat_names:
                    continue
                descr = ""
                if hasattr(h_i.spec.handler_inst, "DESCRIPTION"):
                    descr = getattr(h_i.spec.handler_inst, "DESCRIPTION")
                seq = h_i.spec.handler_inst.sequence if hasattr(h_i.spec.handler_inst, "sequence") else 9999
                categories.append((category, descr, seq))
                cat_names.add(category)
        categories.sort(key=lambda cat: (cat[2], cat[0]))
        return categories

    def describe_api(self):
        """
        Our internal JSON representation of the API.
        Call this from an API handler to make a self-describing API.
        """
        by_category = defaultdict(list)
        categories = {}
        for cat, descr, seq in self.gather_categories():
            categories[cat] = (descr, seq)
        all_handlers = []
        for method, handlers in self.rest_intf.handlers.items():
            for h_i in handlers:
                all_handlers.append((method, h_i, (h_i.sequence or 999, h_i.spec.title if h_i.spec else "")))
        for method, h_i, sort_key in sorted(all_handlers, key=lambda r: r[2]):
            if not self.enable_authenticated_calls and self.rest_intf.handler_requires_authentication(h_i.handler_fn):
                continue
            if h_i.spec:
                h_j = h_i.spec_json(include_docs=self.include_docs)
                category = h_j["category"]
                del h_j["category"]
                h_j["method"] = method
                by_category[category].append(h_j)
        cat_descr = lambda cat: categories.get(cat, ("", 0))[0]
        cat_seq = lambda cat: (categories.get(cat, ("", 0))[1], cat)
        out = list((cat, calls, cat_descr(cat)) for cat, calls in sorted(by_category.items(), key=lambda i: cat_seq(i[0])))
        return out

    def describe_api_swagger(self):
        """
        A Swagger description of the API.
        """
        out = {
            "openapi": "3.0.0",
            "info": {
                "version": self.version,
                "title": self.title
            },
            "servers": [{"url": self.server_url}],
            "paths": defaultdict(dict),
        }
        paths = out["paths"]
        tags = set()
        for method in ["get", "put", "post", "delete"]:
            handlers = self.rest_intf.handlers.get(method, [])
            for h_i in sorted(handlers, key=lambda r: r.sequence or 999999):
                if not self.enable_authenticated_calls and self.rest_intf.handler_requires_authentication(h_i.handler_fn):
                    continue
                self._one_swagger_call(method, h_i, paths, tags, include_docs=self.include_docs)
        out["tags"] = [
            {"name": name, "description": descr}
            for name, descr, seq in self.gather_categories()
        ]
        return out

    def _one_swagger_call(self, method, h_i, paths, tags, include_docs):
        if not h_i.spec:
            return
        h_j = h_i.spec_json(include_docs=include_docs)
        url = h_j["url"].replace(":*", "")
        if url.startswith("/{"):
            # ignoring global paths for now
            return
        paths[url][method] = descr = {}
        doc, doc_detail = h_j.get("description", ("", {}))
        doc_params = {k: v for k, v in doc_detail.get("parameters", [])}
        descr["description"] = doc
        descr["operationId"] = h_j["title"]
        if h_i.methods and method != h_i.methods[0]:
            # if there are multiple methods, append method name to make the operationId unique
            descr["operationId"] += f"_{method}"
        descr["tags"] = [h_j["category"]]
        tags.add(h_j["category"])
        descr["parameters"] = params = []
        descr["responses"] = responses = {}
        for param in h_j["parameters"]:
            sch = self._py_type_to_json_type(param.get("type"))
            in_type = "path" if "{%s}" % param["name"] in url else "query"
            param_def = {
                "name": param["name"],
                "in": in_type,
                "description": doc_params.get(param["name"], ""),
                "required": in_type == "path" or "default" not in param,
                "schema": sch
            }
            params.append(param_def)
        spec_response_type = h_i.spec.response_type
        if spec_response_type in {"download", "raw"}:
            response_mime_type = "application/octet-stream"
        elif spec_response_type == "json":
            response_mime_type = MIME_JSON
        else:
            response_mime_type = MIME_JSON
        responses["200"] = {"content": {response_mime_type: {"schema": {}}}, "description": ""}

    @staticmethod
    def _py_type_to_json_type(p_type):
        # TODO handle composite types
        if p_type == "int":
            return {"type": "number", "format": "int32"}
        elif p_type == "float":
            return {"type": "number", "format": "double"}
        elif p_type == "dict":
            return {"type": "object"}
        elif p_type == "list":
            return {"type": "array", "items": {}}
        elif p_type == "bool":
            return {"type": "boolean"}
        elif p_type == "str":
            return {"type": "string"}
        else:
            return {"type": "string"}

