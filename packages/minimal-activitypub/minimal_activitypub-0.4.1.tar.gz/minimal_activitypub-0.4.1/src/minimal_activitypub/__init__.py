"""Package 'minimal_activitypub' level definitions."""
import sys

from typing_extensions import Final


__version__: Final[str] = "0.4.1"
__display_name__: Final[str] = "Minimal-ActivityPub"
__package_name__: Final[str] = __display_name__.lower()
USER_AGENT: Final[
    str
] = f"{__display_name__}_v{__version__}_Python_{sys.version.split()[0]}"
