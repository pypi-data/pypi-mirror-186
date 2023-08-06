from dataclasses import dataclass
from enum import Enum


class FontFormat(Enum):
    """
    All formats that exist as a web font
    """

    ttf = "ttf"
    otf = "otf"
    woff = "woff"
    woff2 = "woff2"
    eot = "eot"
    svg = "svg"


@dataclass
class FontFamily:
    """
    Font family description for the settings
    """

    provider: str
    name: str
