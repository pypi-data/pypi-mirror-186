import re
from typing import NamedTuple

_FAMILY_WEIGHT_REGEX = r"([^/-]+)-(\w+)\.[ot]tf$"

_KNOWN_WEIGHTS = {
    "Thin": 100,
    "Hairline": 100,
    "ExtraLight": 200,
    "Light": 300,
    "Regular": 400,
    "": 400,
    "Medium": 500,
    "SemiBold": 600,
    "Bold": 700,
    "ExtraBold": 800,
    "Black": 900,
}


class GoogleFontInfo(NamedTuple):
    file: str
    family: str
    style: str
    weight: int


class ParseError(Exception):
    """Exception used when parse failed."""


def get_family_name(font_name: str):
    """
    Attempts to build family name from font name.

    For example, HPSimplifiedSans => HP Simplified Sans.
    """

    font_name = re.sub("(.)([A-Z][a-z]+)", r"\1 \2", font_name)
    font_name = re.sub("([a-z])([0-9]+)", r"\1 \2", font_name)
    return re.sub("([a-z0-9])([A-Z])", r"\1 \2", font_name)


def get_style(style_name: str) -> str:
    return "italic" if "Italic" in style_name else "normal"


def get_weight(style_name: str) -> int:
    """
    Derive weight from a style name.
    """

    if style_name.endswith("Italic"):
        return _KNOWN_WEIGHTS[style_name[:-6]]

    return _KNOWN_WEIGHTS[style_name]


def extract_font_info(path) -> GoogleFontInfo:
    """
    Extracts family, style, and weight from Google Fonts standard filename.
    """

    m = re.search(_FAMILY_WEIGHT_REGEX, path)

    if not m:
        raise ParseError("Could not parse %s" % path)

    style = get_style(m.group(2))
    weight = get_weight(m.group(2))

    return GoogleFontInfo(path, get_family_name(m.group(1)), style, weight)
