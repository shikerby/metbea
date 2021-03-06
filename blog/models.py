import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.timezone import utc

from django.contrib.auth.models import User
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.conf import settings


now = datetime.datetime.utcnow().replace(tzinfo=utc)


class PublishedManager(models.Manager):
    def get_queryset(self):
        qs = super(PublishedManager, self).get_queryset().filter(status='published')
        return qs


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('waiting', 'Waiting'),
        ('published', 'Published'),
    )
    author = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='my_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    pv = models.PositiveIntegerField(default=0)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_like', blank=True)

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.created.year,
                                                 self.created.month,
                                                 self.created.day,
                                                 self.slug])
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)