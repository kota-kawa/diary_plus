"""
Entry & Like models.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
import markdown2
from PIL import Image

def cover_upload_to(instance, filename):
    return f"covers/{instance.author.username}/{filename}"

class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    title = models.CharField(max_length=255)
    body_md = models.TextField("本文 (Markdown)")
    body_html = models.TextField(editable=False)
    cover_image = models.ImageField(upload_to=cover_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)
    likes = models.ManyToManyField(User, related_name="liked_entries", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.body_html = markdown2.markdown(self.body_md, extras=["fenced-code-blocks"])
        super().save(*args, **kwargs)
        # thumbnail
        if self.cover_image:
            img = Image.open(self.cover_image.path)
            img.thumbnail((600, 600))
            img.save(self.cover_image.path)

    def get_absolute_url(self):
        return reverse("entry_detail", args=[self.pk])

    def __str__(self):
        return self.title
