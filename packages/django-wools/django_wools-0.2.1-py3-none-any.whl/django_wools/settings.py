import math
from importlib import import_module
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .settings_types import FontFamily, FontFormat


def import_class(class_fqn: str):
    """
    Importing the class from its FQN
    """

    module, class_name = class_fqn.rsplit(".", 1)

    try:
        return getattr(import_module(module), class_name)
    except Exception:
        raise ImproperlyConfigured(f'Class "{class_fqn}" cannot be imported')


class WoolsSettings:
    """
    Proxy over the Django settings to provide defaults (and shortcuts)
    """

    _defaults = dict(
        MAX_PIXEL_RATIO=3.0,
        INCREMENT_STEP_PERCENT=(math.sqrt(2) - 1) * 100,
        FONTS_DIR="fonts",
        FONTS_STATIC_ROOT=None,
        FONTS_FAMILIES=[],
        FONTS_PROVIDERS={"google": "django_wools.fonts.GoogleFontsProvider"},
        FONTS_FORMATS=[FontFormat.woff2, FontFormat.ttf],
        FONTS_CONVERSIONS={
            (FontFormat.ttf, FontFormat.woff): ["django_wools.fonts.TtfToWoff"],
            (FontFormat.ttf, FontFormat.woff2): ["django_wools.fonts.TtfToWoff2"],
        },
    )

    def get_fonts_families(self, data):
        try:
            return [
                (FontFamily(*x) if not isinstance(x, FontFamily) else x) for x in data
            ]
        except Exception:
            raise ImproperlyConfigured(
                'Unable to parse "WOOLS_FONTS_FAMILIES". It must be a list of '
                "FontFamily instances or *args for the FontFamily constructor"
            )

    def get_fonts_formats(self, data):
        try:
            return [FontFormat(x) if not isinstance(x, FontFormat) else x for x in data]
        except Exception:
            raise ImproperlyConfigured(
                'Unable to parse "WOOLS_FONTS_FORMATS". It must be a list of '
                "valid format names or FontFormat instances"
            )

    def get_fonts_providers(self, data):
        return {name: import_class(class_fqn) for name, class_fqn in data.items()}

    def get_fonts_conversions(self, data):
        out = {}

        for (from_format, to_format), conversion_path in data.items():
            if not isinstance(from_format, FontFormat):
                from_format = FontFormat(from_format)

            if not isinstance(to_format, FontFormat):
                to_format = FontFormat(to_format)

            conversion_path = [import_class(x)() for x in conversion_path]

            out[(from_format, to_format)] = conversion_path

        return out

    def get_fonts_static_root(self, data):
        return data or settings.STATICFILES_DIRS[0]

    def make_fonts_dir(self) -> Path:
        return Path(self.FONTS_STATIC_ROOT) / self.FONTS_DIR

    def __getattr__(self, item):
        if item.startswith("get_"):
            return None

        data = getattr(settings, f"WOOLS_{item}", self._defaults[item])

        if getter := getattr(self, f"get_{item.lower()}"):
            return getter(data)
        else:
            return data


wool_settings = WoolsSettings()
