from . import _version
from .kv import BotHashicorpKVPlugin  # noqa: F401, F403

__version__ = _version.get_versions()['version']
