from . import _version
from .plugin import BotWhatsappPlugin, MediaType  # noqa: F401, F403

__version__ = _version.get_versions()['version']
