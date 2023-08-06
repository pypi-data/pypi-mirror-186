from . import _version
from .models import Author, Color, Field, Footer, Message  # noqa: F401, F403
from .plugin import BotSlackPlugin  # noqa: F401, F403

__version__ = _version.get_versions()['version']
