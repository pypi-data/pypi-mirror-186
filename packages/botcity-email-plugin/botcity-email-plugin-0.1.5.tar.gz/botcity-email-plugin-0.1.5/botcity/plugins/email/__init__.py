from . import _version
from .plugin import BotEmailPlugin  # noqa: F401, F403
from .plugin import MailFilters  # noqa: F401, F403
from .servers_config import MailServers  # noqa: F401, F403

__version__ = _version.get_versions()['version']
