from __future__ import absolute_import
from datetime import datetime

from celery import shared_task
from .models import Post

@shared_task
def update_post_status():
    posts_of_waiting = Post.objects.filter(status='waiting')
    res = []
    now = datetime.now()
    for p in posts_of_waiting:
        if p.publish <= now:
            p.status = 'published'
            p.save(update_fields=['status'])
            res.append(p.title)
    if res:
        return res
    else:
        return now
