import os
from django.core.management.base import BaseCommand
from portfolio.models import Profile, Project, Skill, Certification, ProfilePhoto


class Command(BaseCommand):
    help = 'Fix double path issues in media files'

    def handle(self, *args, **options):
        # Fix Profile resume
        profile = Profile.objects.first()
        if profile and profile.resume and 'resume/resume/' in profile.resume.name:
            old_name = profile.resume.name
            new_name = old_name.replace('resume/resume/', 'resume/')
            profile.resume.name = new_name
            profile.save()
            self.stdout.write(f"Fixed resume path: {old_name} -> {new_name}")
        
        # Fix Projects
        for project in Project.objects.all():
            if project.image and 'projects/projects/' in project.image.name:
                old_name = project.image.name
                new_name = old_name.replace('projects/projects/', 'projects/')
                project.image.name = new_name
                project.save()
                self.stdout.write(f"Fixed project image: {old_name} -> {new_name}")
        
        # Fix Skills
        for skill in Skill.objects.all():
            if skill.icon and 'skills/skills/' in skill.icon.name:
                old_name = skill.icon.name
                new_name = old_name.replace('skills/skills/', 'skills/')
                skill.icon.name = new_name
                skill.save()
                self.stdout.write(f"Fixed skill icon: {old_name} -> {new_name}")
        
        # Fix Certifications
        for cert in Certification.objects.all():
            if cert.image and 'certifications/certifications/' in cert.image.name:
                old_name = cert.image.name
                new_name = old_name.replace('certifications/certifications/', 'certifications/')
                cert.image.name = new_name
                cert.save()
                self.stdout.write(f"Fixed certification image: {old_name} -> {new_name}")
        
        # Fix Profile Photos
        for photo in ProfilePhoto.objects.all():
            if photo.image and 'profile_photos/profile_photos/' in photo.image.name:
                old_name = photo.image.name
                new_name = old_name.replace('profile_photos/profile_photos/', 'profile_photos/')
                photo.image.name = new_name
                photo.save()
                self.stdout.write(f"Fixed profile photo: {old_name} -> {new_name}")
        
        self.stdout.write(self.style.SUCCESS('Double path issues fixed!'))