from django.utils.translation import ugettext as _
from django.template.defaulttags import CsrfTokenNode
from django.utils.encoding import smart_unicode

import jinja2

from jingo import register


@register.function
@jinja2.contextfunction
def csrf(context):
    return jinja2.Markup(CsrfTokenNode().render(context))


@register.filter
def f(string, *args, **kwargs):
    """
    Uses ``str.format`` for string interpolation.

    >>> {{ "{0} arguments and {x} arguments"|f('positional', x='keyword') }}
    "positional arguments and keyword arguments"
    """
    string = unicode(string)
    return string.format(*args, **kwargs)


@register.filter
def nl2br(string):
    """Turn newlines into <br>."""
    if not string:
        return ''
    return jinja2.Markup('<br>'.join(jinja2.escape(string).splitlines()))


@register.filter
def datetime(t, fmt=None):
    """Call ``datetime.strftime`` with the given format string."""
    if fmt is None:
        fmt = _('%B %e, %Y')
    return smart_unicode(t.strftime(fmt.encode('utf-8'))) if t else u''


@register.filter
def ifeq(a, b, text):
    """Return ``text`` if ``a == b``."""
    return jinja2.Markup(text if a == b else '')


@register.filter
def class_selected(a, b):
    """Return ``'class="selected"'`` if ``a == b``."""
    return ifeq(a, b, 'class="selected"')
