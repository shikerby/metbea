import datetime
import markdown

from django.db.models import Count
from django.utils.safestring import mark_safe
from django import template

from blog.models import Post
from blog.forms import SearchForm


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.filter(publish__gte=datetime.date.today()).count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments', '-publish')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag('blog/search_widget.html')
def show_search_widget():
    search_form = SearchForm()
    return {'search_form': search_form}