import pathlib
__version__ = (pathlib.Path(__file__).parent / "version").read_text().strip()

from .api.base import ApiBase, endpoint
from .api.configbase import ConfigBase
from .api.cat_base import ApiCategoryBase, ApiCategoryBaseCRUD
from .api.cat_common import generate_common_category, ApiCommonModule
from .api.cat_user import generate_user_category, generate_user_category_class
from .api.cat_user_activity import generate_user_activity_api_category
from .api.cat_help import generate_help_category
from .api.entrypoint import entry_point, on_stopped
from .errs import GeneralError, BadRequest, ReportedException, AccessDenied403, Unauthorized401, InternalError
