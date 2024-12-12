from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    categories = models.ManyToManyField(Category, related_name='films')
    image_url = models.URLField(blank=True, null=True)  # Rasm URL
    video_url = models.URLField(blank=True, null=True)  # Video URL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
