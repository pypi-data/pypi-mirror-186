from django.core.files.images import get_image_dimensions
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class PictureSizeForm(ModelForm):
    """
    Checks that picture fields listed in FIELDS have the right image size

    Notes
    -----
    This is here for compatibility reasons, I don't know why this wasn't made
    as a field initially.

    Examples
    --------

    >>> class PressReleaseForm(PictureSizeForm):
    >>>     FIELDS = {"thumbnail": [234, 330]}
    >>>
    >>>     class Meta:
    >>>         model = PressRelease
    >>>         exclude = []
    """

    FIELDS = {}

    def clean(self):
        data = super().clean()

        for field, expect in self.FIELDS.items():
            if not data.get(field):
                continue

            actual = get_image_dimensions(data[field])

            if tuple(expect) != tuple(actual):
                self.add_error(
                    field,
                    _(
                        "Vous avez envoyé une image de %(actual_size)s alors "
                        "qu'est attendue une image de %(expected_size)s."
                    )
                    % {
                        "actual_size": f"{actual[0]}x{actual[1]}px",
                        "expected_size": f"{expect[0]}x{expect[1]}px",
                    },
                )
