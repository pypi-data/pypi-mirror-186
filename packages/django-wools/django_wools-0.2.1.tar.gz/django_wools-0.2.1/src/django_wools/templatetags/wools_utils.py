from django import template
from django.template.base import Node, Parser, TemplateSyntaxError, Token
from minify_html import minify

register = template.Library()


def do_minify(parser: Parser, token: Token):
    """
    Parsing function for the HTML minification tag

    Parameters
    ----------
    parser
        Template parser
    token
        Template token
    """

    bits = token.split_contents()

    if len(bits) > 1:
        raise TemplateSyntaxError("Unexpected arguments to minify_html")

    nodelist = parser.parse(("endminify",))
    parser.delete_first_token()

    return MinifyHtmlNode(nodelist)


class MinifyHtmlNode(Node):
    """
    Template tag that minifies HTML, including inside <style> and <script>
    tags.
    """

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return minify(output, minify_js=True, minify_css=True)


register.tag("minify", do_minify)
