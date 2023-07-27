from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title=models.CharField(max_length=255)
    full_text = models.TextField()
    summary = models.TextField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    #todo slug
    #todo cat as foreigin key
    # todo del summary
    def get_absolute_url(self):
        return reverse('article_page', kwargs={'article_slug': self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)