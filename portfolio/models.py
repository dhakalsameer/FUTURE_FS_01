from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    about = models.TextField()
    email = models.EmailField()
    resume = models.FileField(upload_to="resume/")

    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class ProfilePhoto(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    image = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.profile.full_name} - Photo {self.order}"


class Role(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="skills/", blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, default="", blank=True)
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    issuer = models.CharField(max_length=150)
    date_awarded = models.DateField()
    certificate_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="certifications/", blank=True, null=True) 

    def __str__(self):
        return self.title