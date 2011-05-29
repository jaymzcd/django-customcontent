from django import template
from django.conf import settings
from customcontent.models import CustomContent, CustomItem
import urlparse
register = template.Library()

def cc_item(request, *args):
    """
        Helper method to take the input request and a list of
        attributes (of a CustomContent object) and generates
        the stringified (!?) version of the code.
    """

    wrap_strings = {
        'css': """<style type="text/css">%s</style>""",
        'js': """<script type="text/javascript">%s</script>""",
    }
    content_items = CustomContent.find(request)
    content = list()

    for cc in content_items:
        for arg in args:
            c_content = getattr(cc, arg)
            try:
                # First see if it's a related manager
                items = c_content.all()
                for item in items:
                    content.append([item.render()])
            except AttributeError:
                # We've got a normal attribute on our CustomItem object
                try:
                    content.append([wrap_strings[arg] % c_content,])
                except KeyError:
                    content.append([c_content,])

    return '\n'.join([item for res in content for item in res])

@register.simple_tag(takes_context=True)
def customcontent_head(context):
    """
        Render out any extra headers for this path
    """   
    return cc_item(context['request'], 'extra_head')

@register.simple_tag(takes_context=True)
def customcontent_js(context):
    """
        Render out any custom JS for this path
    """
    return cc_item(context['request'], 'js')

@register.simple_tag(takes_context=True)
def customcontent_css(context):
    """
        Render out any custom CSS for this path
    """
    return cc_item(context['request'], 'css')

@register.simple_tag(takes_context=True)
def customcontent_allhead(context):
    """
        Saver method to call on all the header attributes
    """
    return cc_item(context['request'], 'extra_head', 'js', 'css')

@register.simple_tag(takes_context=True)
def customcontent_items(context):
    """
        Uses the related manager to return all the items for
        all the matching CustomContent objects for the current path
    """
    return cc_item(context['request'], 'customitem_set')

