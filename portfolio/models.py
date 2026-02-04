from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
