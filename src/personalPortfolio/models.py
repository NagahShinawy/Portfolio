from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    desc = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='portfolio/images/')
    project_url = models.URLField(blank=True)
    slug = models.SlugField(max_length=200, default='', editable=False)
    objects = models.manager

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        print(self.slug)
        return self.title