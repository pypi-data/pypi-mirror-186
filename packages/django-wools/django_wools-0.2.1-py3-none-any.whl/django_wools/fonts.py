from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import BytesIO
from os.path import splitext
from pathlib import Path
from typing import Iterator
from zipfile import ZipFile, ZipInfo

import httpx
from fontTools.ttLib import TTFont

from ._google_fonts import extract_font_info
from .settings import wool_settings
from .settings_types import FontFamily, FontFormat


@dataclass
class ExtractedFile:
    """
    All the required meta-information about a file. It's basically what goes
    into a @font-face directive, except that the file_name is relative to a
    path that suits the caller and the callee.
    """

    file_name: str
    format: FontFormat
    family: str
    style: str
    weight: int


class WoolFontProvider(ABC):
    """
    Interface of font provider, you can implement it to provide fonts from
    another source.
    """

    @classmethod
    @abstractmethod
    def open_family(cls, family: FontFamily) -> "WoolFontProvider":
        """
        Opens a family from the source, this is basically a disguised way to
        have a well defined constructor which does not enforce anything on the
        actual constructor.

        Parameters
        ----------
        family
            Font family that this source will provide
        """

        raise NotImplementedError

    @abstractmethod
    def extract_files(self, to_directory: Path) -> Iterator[ExtractedFile]:
        """
        Extracts all the files from the source into a specified directory
        (which is temporary) and returns an iterator over all extracted
        files with their meta-data.

        Parameters
        ----------
        to_directory
            Directory into which files must be extracted
        """

        raise NotImplementedError


class WoolFontConverter(ABC):
    """
    Font conversion interface. A converter only converts into one format.
    """

    @abstractmethod
    def convert(self, source_path: Path, target_path: Path) -> None:
        """
        Converts the source file into the target format.

        Parameters
        ----------
        source_path
            Path to the source file
        target_path
            Path to write with the converted file
        """

        raise NotImplementedError

    @abstractmethod
    def get_format(self) -> FontFormat:
        """
        Returns the output format of this converter
        """

        raise NotImplementedError


class GoogleFontsProvider(WoolFontProvider):
    ENDPOINT = "https://fonts.google.com/download"

    def __init__(self, family: FontFamily):
        self.family = family

    @classmethod
    def open_family(cls, family: FontFamily) -> "WoolFontProvider":
        return cls(family)

    def extract_files(self, to_directory: Path) -> Iterator[ExtractedFile]:
        """
        Getting files from Google Fonts is as easy as downloading and
        extracting a zip file. Then a little bit of parsing on files names
        gives us all the meta-data that we need.
        """

        r = httpx.get(self.ENDPOINT, params=dict(family=self.family.name))
        r.raise_for_status()
        zip_bytes = BytesIO(r.content)

        with zip_bytes, ZipFile(zip_bytes, "r") as zf:
            zf.extractall(to_directory)

            file: ZipInfo
            for file in zf.infolist():
                _, ext = splitext(file.filename)

                if ext.lower() == ".ttf":
                    info = extract_font_info(file.filename)

                    yield ExtractedFile(
                        file_name=file.filename,
                        format=FontFormat.ttf,
                        family=info.family,
                        style=info.style,
                        weight=info.weight,
                    )


class KeepFormat(WoolFontConverter):
    """
    Special internal converter that just copies the file. It's not advised to
    use it in your configuration, it does not even implement the full API.
    It's really some internal sauce.
    """

    def get_format(self) -> FontFormat:
        pass

    def convert(self, source_path: Path, target_path: Path) -> None:
        with open(source_path, "rb") as file_in, open(target_path, "wb") as file_out:
            while chunk := file_in.read(10240):
                file_out.write(chunk)

        return None  # noqa


class TtfToWoff(WoolFontConverter):
    """
    Converts from TTF to WOFF using fonttools
    """

    def get_format(self) -> FontFormat:
        return FontFormat.woff

    def convert(self, source_path: Path, target_path: Path) -> None:
        f = TTFont(source_path)
        f.flavor = "woff"
        f.save(target_path)


class TtfToWoff2(WoolFontConverter):
    """
    Converts from TTF to WOFF2 using fonttools
    """

    def get_format(self) -> FontFormat:
        return FontFormat.woff2

    def convert(self, source_path: Path, target_path: Path) -> None:
        f = TTFont(source_path)
        f.flavor = "woff2"
        f.save(target_path)


def get_provider(family: FontFamily) -> WoolFontProvider:
    """
    Retrieves the provider instance for a font family
    """

    return wool_settings.FONTS_PROVIDERS[family.provider].open_family(family)
