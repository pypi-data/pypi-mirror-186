from . import _version
from .filter import Filter  # noqa: F401, F403
from .plugin import BotAWSS3Plugin  # noqa: F401, F403

__version__ = _version.get_versions()['version']
