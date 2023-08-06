from . import _version
from .plugin import BotGmailPlugin  # noqa: F401, F403
from .utils import GmailDefaultLabels  # noqa: F401, F403

__version__ = _version.get_versions()['version']
