import re
from enum import Enum
from typing import Iterator, NamedTuple, Optional
from wagtail.images.models import SourceImageIOError
from django import template
from wagtail.images.models import AbstractImage

from ..settings import wool_settings

register = template.Library()


class WidthInfo(NamedTuple):
    """
    Computed width from generate_widths()
    """

    width: int
    pixel_ratio: float


def generate_widths(spec_width) -> Iterator[WidthInfo]:
    """
    Generates width and device pixel ratios based on settings bounds and the
    initial spec width of the image.

    Parameters
    ----------
    spec_width
        On-screen width of the image
    """

    width = spec_width
    max_width = spec_width * wool_settings.MAX_PIXEL_RATIO

    for _ in range(0, 1000):
        yield WidthInfo(width, round(float(width) / float(spec_width), 4))

        if width > max_width:
            return

        width *= 1 + wool_settings.INCREMENT_STEP_PERCENT / 100.0


class WagtailSizeOperation(Enum):
    """
    Allowed Wagtail operations
    """

    max = "max"
    min = "min"
    width = "width"
    fill = "fill"


class WagtailSizeSpec(NamedTuple):
    """
    Parsed Wagtail size specification
    """

    operation: WagtailSizeOperation
    width: int
    height: Optional[int]
    zoom: int = 0

    def __str__(self):
        """
        Un-parses the string
        """

        out = f"{self.operation.value}-{self.width}"

        if self.height:
            out += f"x{self.height}"

        if self.zoom:
            out += f"-c{self.zoom}"

        return out

    @classmethod
    def parse(cls, spec) -> "WagtailSizeSpec":
        """
        Parses a spec and returns the parsed tuple
        """

        ops = "|".join(WagtailSizeOperation._member_names_)  # noqa
        exp = re.compile(
            rf"(?P<op>{ops})-(?P<width>\d+)x(?P<height>\d+)?(-c(?P<zoom>\d+))?"
        )

        if not (m := exp.match(spec)):
            raise ValueError(
                f'Provided spec "{spec}" cannot be parsed. Please bear in '
                f'mind that "scale" and "height" operations are not permitted '
                f"since they do not have any width constraint."
            )

        return cls(
            operation=WagtailSizeOperation(m.group("op")),
            width=int(m.group("width")),
            height=(int(m.group("height")) if m.group("height") else None),
            zoom=(int(m.group("zoom")) if m.group("zoom") else 0),
        )

    def at_width(self, width: int) -> "WagtailSizeSpec":
        """
        Returns a scaled version of this spec to fit the new width
        """

        ratio = float(width) / float(self.width)

        if self.height:
            new_height = ratio * self.height
        else:
            new_height = None

        return self._replace(height=round(new_height), width=round(width))


@register.inclusion_tag("wools/images/fixed_size.html")
def image_fixed_size(
    image: AbstractImage,
    spec: str,
    css_class: str = "",
    fallback_format: str = "png",
    lossless: bool = False,
):
    """
    This tag manages images whose size on screen stay the same and simply
    needs larger images for larger pixel ratios.

    Image will be encoded in WebP with a fallback of the choosing of the
    caller, by default PNG to make sure to lose nothing (neither quality
    neither alpha channel).

    Parameters
    ----------
    image
        Original Wagtail image
    spec
        Wagtail size spec
    css_class
        CSS class that will be added to the root <picture> element
    fallback_format
        The format to use for browsers that do not support WebP
    lossless
        Enables lossless compression for WebP. If you want the fallback to also
        be lossless, you need to use "png" as fallback_format.
    """

    parsed_spec = WagtailSizeSpec.parse(spec)

    if fallback_format not in {"png", "jpeg"}:
        raise ValueError('Only "png" and "jpeg" are allowed as fallbacks')

    if not isinstance(image, AbstractImage):
        return {}

    try:
        base_rendition = image.get_rendition(f"{spec}|format-{fallback_format}")
    except SourceImageIOError as e:
        """
        An error can exist if the image has been manually deleted from the S3 bucket for example
        """
        return dict(spec_width=parsed_spec.width, spec_height=parsed_spec.height)

    sources = {}

    if lossless:
        webp_format = "webp-lossless"
    else:
        webp_format = "webp"

    for fmt in [webp_format, fallback_format]:
        sources[fmt] = dict(set=[], base=image.get_rendition(f"{spec}|format-{fmt}"))

        for width, density in generate_widths(parsed_spec.width):
            if int(density) == density:
                density = int(density)

            rendition = image.get_rendition(
                f"{parsed_spec.at_width(width)}|format-{fmt}"
            )

            sources[fmt]["set"].append(
                dict(
                    rendition=rendition,
                    density=density,
                    string=f"{rendition.url} {density}x",
                )
            )

        sources[fmt]["srcset"] = ", ".join(x["string"] for x in sources[fmt]["set"])

    return dict(
        base_url=base_rendition.url,
        size=dict(width=base_rendition.width, height=base_rendition.height),
        alt=image.default_alt_text,
        sources=sources,
        css_class=css_class,
    )
