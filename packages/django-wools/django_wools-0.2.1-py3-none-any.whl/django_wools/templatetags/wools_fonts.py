import posixpath

from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import Context, Template
from django.contrib.staticfiles import finders
from django.conf import settings

from ..settings import wool_settings

register = template.Library()


@register.simple_tag
def fonts_head():
    """
    This tag will inject into your template the CSS font declarations from the
    wools fonts system. The output will be a `<style>` tag.
    """

    template_static_path = f"{wool_settings.FONTS_DIR}/fonts.html"
    normalized_path = posixpath.normpath(template_static_path).lstrip('/')

    if settings.DEBUG:
        absolute_path = finders.find(normalized_path)
    else:
        absolute_path = staticfiles_storage.path(normalized_path)

    if absolute_path:
        with open(absolute_path, "r", encoding="utf-8") as tf:
            template_code = tf.read()
    else:
        template_code = ''

    tpl = Template(
        f"{{% load wools_utils %}}{{% minify %}}{ template_code }{{% endminify %}}"
    )
    ctx = Context()

    return tpl.render(ctx)
