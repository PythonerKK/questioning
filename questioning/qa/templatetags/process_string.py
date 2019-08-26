import re

from django import template

register = template.Library()


@register.filter
def removeHTML(value):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', value)
    return dd[:300] + '...'

@register.filter
def removeHTML100(value):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', value)
    return dd[:130] + '...'


@register.filter
def processDate(value):
    return value.strftime("%Y-%m-%d")


@register.filter
def process_title(value):
    return value[:20] + '...'


@register.filter
def process_comment_content(value):
    return value[:50] + '...'