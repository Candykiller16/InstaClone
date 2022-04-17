from django.db import models
from django.urls import reverse


class Post(models.Model):
    # owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug_field': self.slug})
