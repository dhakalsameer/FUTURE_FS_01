import os
import json
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from portfolio.models import Profile, Project, Skill, Role, Certification, ProfilePhoto


class Command(BaseCommand):
    help = 'Fix media file associations after import'

    def handle(self, *args, **options):
        # Check if data file exists
        if not os.path.exists('portfolio_data.json'):
            self.stdout.write(self.style.ERROR('portfolio_data.json not found'))
            return
        
        # Load data
        with open('portfolio_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Fix Profile resume
        for profile_data in data.get('profiles', []):
            try:
                profile = Profile.objects.get(full_name=profile_data['full_name'])
                if profile_data.get('resume') and not profile.resume:
                    resume_path = f"media/{profile_data['resume']}"
                    if os.path.exists(resume_path):
                        with open(resume_path, 'rb') as f:
                            profile.resume.save(profile_data['resume'], ContentFile(f.read()), save=True)
                        self.stdout.write(f"Fixed resume for {profile.full_name}")
            except Profile.DoesNotExist:
                pass
        
        # Fix Projects images
        for project_data in data.get('projects', []):
            try:
                project = Project.objects.get(title=project_data['title'])
                if project_data.get('image') and not project.image:
                    image_path = f"media/{project_data['image']}"
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as f:
                            project.image.save(project_data['image'], ContentFile(f.read()), save=True)
                        self.stdout.write(f"Fixed image for {project.title}")
            except Project.DoesNotExist:
                pass
        
        # Fix Skills icons
        for skill_data in data.get('skills', []):
            try:
                skill = Skill.objects.get(name=skill_data['name'])
                if skill_data.get('icon') and not skill.icon:
                    icon_path = f"media/{skill_data['icon']}"
                    if os.path.exists(icon_path):
                        with open(icon_path, 'rb') as f:
                            skill.icon.save(skill_data['icon'], ContentFile(f.read()), save=True)
                        self.stdout.write(f"Fixed icon for {skill.name}")
            except Skill.DoesNotExist:
                pass
        
        # Fix Certifications images
        for cert_data in data.get('certifications', []):
            try:
                cert = Certification.objects.get(title=cert_data['title'])
                if cert_data.get('image') and not cert.image:
                    image_path = f"media/{cert_data['image']}"
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as f:
                            cert.image.save(cert_data['image'], ContentFile(f.read()), save=True)
                        self.stdout.write(f"Fixed image for {cert.title}")
            except Certification.DoesNotExist:
                pass
        
        # Fix Profile Photos
        for photo_data in data.get('profile_photos', []):
            try:
                profile = Profile.objects.get(full_name=photo_data['profile_full_name'])
                photo = ProfilePhoto.objects.get(profile=profile, order=photo_data['order'])
                if photo_data.get('image') and not photo.image:
                    image_path = f"media/{photo_data['image']}"
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as f:
                            photo.image.save(photo_data['image'], ContentFile(f.read()), save=True)
                        self.stdout.write(f"Fixed photo for {profile.full_name}")
            except (Profile.DoesNotExist, ProfilePhoto.DoesNotExist):
                pass
        
        self.stdout.write(self.style.SUCCESS('Media file associations fixed!'))