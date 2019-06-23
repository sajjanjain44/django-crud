from __future__ import  unicode_literals
from django.db import models

# Create your models here.
from django.urls import reverse


class blog_posts(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit',kwargs={'pk' : self.pk})


