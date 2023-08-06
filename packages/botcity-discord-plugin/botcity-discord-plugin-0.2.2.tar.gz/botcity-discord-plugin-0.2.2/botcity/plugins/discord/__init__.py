from . import _version
from .models import (Author, Color, EmbeddedMessage, Field,  # noqa: F401, F403
                     Footer)
from .plugin import BotDiscordPlugin  # noqa: F401, F403

__version__ = _version.get_versions()['version']
