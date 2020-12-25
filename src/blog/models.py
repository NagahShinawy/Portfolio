from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, editable=False)
    objects = models.manager

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
