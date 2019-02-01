from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Count

from .models import Post, Comment
from .forms import CommentForm


def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])[:3]
    return render(request, 'blog/list.html', {'object_list': object_list, 'tag': tag})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day,
                                   status='published')

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:2]

    comments = Comment.objects.filter(post=post, active=True)[:5]
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 
                                                'comments': comments, 
                                                'new_comment': new_comment, 
                                                'comment_form': comment_form,
                                                'similar_posts': similar_posts})
