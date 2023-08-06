from collections import defaultdict
from dataclasses import replace
from itertools import product
from logging import WARNING, getLogger
from os.path import splitext
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict, List, NamedTuple

from django.core.management import BaseCommand
from django.template.loader import render_to_string

from django_wools.fonts import ExtractedFile, KeepFormat, get_provider
from django_wools.settings import wool_settings
from django_wools.settings_types import FontFamily, FontFormat

logger = getLogger("wools.import_fonts")


class FontFace(NamedTuple):
    """
    Font face grouping key for the template
    """

    family: str
    weight: int
    style: str


class Command(BaseCommand):
    """
    Downloads the fonts from the source and saves them into the static
    directory (configured in the settings).
    """

    def handle(self, *args, **options):
        """
        Overall, all we need is to go around all families, download them,
        convert them and when it's done generate the CSS file that will serve
        to expose them to the browser.
        """

        getLogger("fontTools").setLevel(WARNING)

        imported: List[ExtractedFile] = []
        converted: Dict[FontFace, List[ExtractedFile]] = defaultdict(list)

        if not wool_settings.FONTS_FAMILIES:
            logger.warning("No families set in WOOLS_FONTS_FAMILIES")
            exit(0)

        fonts_dir = wool_settings.make_fonts_dir()
        fonts_dir.mkdir(parents=True, exist_ok=True)

        with TemporaryDirectory() as td:
            td_path = Path(td)

            self.import_families(imported, td_path)
            self.convert_fonts(converted, fonts_dir, imported, td_path)

        self.write_css(converted, fonts_dir)

    def write_css(self, converted, fonts_dir):
        """
        Generates the template file for those fonts.
        """

        css = render_to_string(
            "wools/fonts.html",
            context=dict(converted={**converted}, static_path=wool_settings.FONTS_DIR),
        )
        css_file = fonts_dir / "fonts.html"

        with open(css_file, "w") as f:
            f.write(css)

        logger.info("Wrote %s", css_file)

    def convert_fonts(self, converted, fonts_dir, imported, td_path):
        """
        Converts and copies to the static dir all the fonts in all the formats.
        """

        file: ExtractedFile
        font_format: FontFormat
        for file, font_format in product(imported, wool_settings.FONTS_FORMATS):
            logger.debug('Generating %s for "%s"', font_format.value, file.family)

            if file.format == font_format:
                convert_path = [KeepFormat()]
            else:
                try:
                    convert_path = wool_settings.FONTS_CONVERSIONS[
                        (file.format, font_format)
                    ]
                except KeyError:
                    logger.error(
                        "No conversion path from %s to %s", file.format, font_format
                    )
                    return exit(1)

            name, _ = splitext(file.file_name)
            old_path = td_path / file.file_name

            for converter in convert_path[:-1]:
                logger.debug(
                    "Intermediate conversion through %s", converter.__class__.__name__
                )
                ext = converter.get_format().value
                new_path = td_path / f"{name}.{ext}"
                converter.convert(old_path, new_path)
                old_path = new_path

            converter = convert_path[-1]
            ext = font_format.value
            file_name = f"{name}.{ext}"
            new_path = fonts_dir / file_name
            converter.convert(old_path, new_path)

            converted[
                FontFace(family=file.family, weight=file.weight, style=file.style)
            ].append(replace(file, file_name=file_name, format=font_format))

    def import_families(self, imported, td_path):
        """
        Runs the importation code on all required families
        """

        family: FontFamily
        for family in wool_settings.FONTS_FAMILIES:
            logger.debug("Importing %s", family.name)
            provider = get_provider(family)

            logger.debug("Extracting %s", family.name)
            imported.extend(provider.extract_files(td_path))
