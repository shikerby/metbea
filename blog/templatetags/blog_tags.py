import datetime
from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.filter(publish__gte=datetime.date.today()).count()