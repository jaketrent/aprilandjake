from django import template
from django.template.defaultfilters import stringfilter
from django.template import loader
register = template.Library()
from content.models import Content	
from django.template.defaultfilters import stringfilter

@register.simple_tag
def list_template(content):
	return loader.render_to_string(content.collection.template.list_path, {'object': content})

@register.simple_tag
def detail_template(content):
	return loader.render_to_string(content.collection.template.detail_path, {'object': content})

def paginator(object):
    return {'object': object}
register.inclusion_tag('includes/_paginator.html')(paginator)

@register.filter("eq")
def eq(value,arg):
    retval = False
    if (value != None):
        retval = int(value) == int(arg)
    return retval

	
@register.filter("get_quote_font_size")
def get_quote_font_size(quote):
	retval = "2em"
	if (len(quote) > 200):
		retval = "1.5em"
	return retval

class VerbatimNode(template.Node):
  def __init__(self, text):
    self.text = text
  def render(self, context):
    return self.text

@register.tag
def verbatim(parser, token):
  text = []
  while 1:
    token = parser.tokens.pop(0)
    if token.contents == 'endverbatim':
      break
    if token.token_type == template.TOKEN_VAR:
      text.append('{{')
    elif token.token_type == template.TOKEN_BLOCK:
      text.append('{%')
    text.append(token.contents)
    if token.token_type == template.TOKEN_VAR:
      text.append('}}')
    elif token.token_type == template.TOKEN_BLOCK:
      text.append('%}')
  return VerbatimNode(''.join(text))