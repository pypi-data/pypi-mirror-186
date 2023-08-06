from miniapp.api.base import endpoint
from miniapp.api.cat_base import ApiCategoryBase
from miniapp.errs import GeneralError
from miniapp.utils.generic_obj import make_object


def generate_common_category(api, system_title: str=None, sequence: int=-1) -> ApiCategoryBase:
    """
    Create a 'common' category to plug into an API with general purpose methods that apply to the whole application.

    Call this from your API's constructor if you want to have support for such things as API and version discovery:
      .

    :param api:             API we'll be part of.
    :param system_title:    A title for the system, for generating Swagger and such.
    :param sequence:        Sequence within list of categories.

    :return:        An API category instance.
    """
    return ApiCommonModule(api, system_title, sequence=sequence)


class ApiCommonModule(ApiCategoryBase):
    """
    All APIs should implement these functions, or similar.
    """
    prefix = ""

    def __init__(self, api, system_title=None, system_url: str=None, sequence: int=-1):
        super(ApiCommonModule, self).__init__(api, sequence=sequence)
        self.system_title = system_title or ""
        self.system_url = system_url
        if not self.system_url:
            cfg = self.api.get_config()
            if cfg:
                self.system_url = cfg.get_external_url()
        # if there are no schemas, disable the schema-related endpoints
        if not self.api._schema_path:
            self.disable_endpoint("fetch_schema")
            self.disable_endpoint("validate_schema")

    def category_name(self):
        return "general"

    @endpoint("get", sequence=10, activity_analysis=False, update_session_timer=False)
    def get_api(self, *args, swagger: bool=False):
        """
        JSON description of the API.

        :param swagger:     Specify 1/True to return Swagger JSON.  Default returns an API description in a proprietary
                            format.
        """
        is_authenticated = bool(self.api.current_user_id())
        include_docs = True
        if swagger:
            return make_object(**self.api._server.describe_api_swagger(
                title=self.system_title, server_url=self.system_url, include_docs=include_docs,
                enable_authenticated_calls=is_authenticated
            ))
        else:
            return make_object(
                api=self.api._server.describe_api(
                    include_docs=include_docs, enable_authenticated_calls=is_authenticated
                ),
                system=self.system_title
            )

    @endpoint("get", "version", sequence=20, activity_analysis=False, update_session_timer=False)
    def version(self, *args):
        """
        System version.
        """
        return make_object(**self.api.version())

    @endpoint("get", "csrf", sequence=25, activity_analysis=False, update_session_timer=False)
    def csrf(self):
        """
        CSRF support.
        """
        values = {}
        csrf = self.api._server.csrf
        if csrf:
            values["csrf_token"] = csrf.establish_in_session(self.api.current_request())
        return make_object(**values)

    @endpoint("get", "ping", sequence=40, activity_analysis=False, update_session_timer=False)
    def ping(self, level: str=None):
        """
        Health check.

        :param level:   An optional indication of how deeply to check the system.

        :raises:  Exception if anything is wrong with the system.
        """
        status = self.api.ping(level)
        return make_object(status=status)

    @endpoint("get", "schemas/{path:*}", sequence=60, activity_analysis=False)
    def fetch_schema(self, path: str):
        """
        Retrieve the JSON schema for a given validatable entity.  This allows the UI to know more about allowed fields
        and such.
        """
        if not self.api.current_user_id():
            # must be logged in
            return
        vis = self.api._visible_schemas
        if vis and not vis(path):
            # schema blocked
            return
        schema = self.api.get_validation_schema(path)
        return schema or None

    @endpoint("post", "schemas/{path:*}", sequence=61, activity_analysis=False)
    def validate_schema(self, path: str, data: (dict, list)):
        """
        Validate some data against one of the built-in schemas.  This makes it possible for the UI to test in advance
        that a particular request will be invalid.

        :param path:        Which schema to validate against.
        :param data:        Data to validate.
        :returns:           ok=True/False - overall result
                            code, message, etc. - details of validation
        """
        if not self.api.current_user_id():
            # must be logged in
            return
        vis = self.api._visible_schemas
        if vis and not vis(path):
            # schema blocked
            return
        try:
            self.api.validate_schema(path, data_to_validate=data)
            return make_object(ok=True)
        except GeneralError as err:
            details = err.public_details
            details.pop("_", None)
            return make_object(ok=False, message=err.message, **details)
