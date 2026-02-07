import json
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from portfolio.models import Profile, Project, Skill, Role, Certification, ProfilePhoto


class Command(BaseCommand):
    help = 'Import portfolio data from JSON file (for production deployment)'

    def handle(self, *args, **options):
        # Check if data file exists
        if not os.path.exists('portfolio_data.json'):
            self.stdout.write(self.style.ERROR('portfolio_data.json not found'))
            return
        
        # Load data
        with open('portfolio_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Clear existing data
        ProfilePhoto.objects.all().delete()
        Certification.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Role.objects.all().delete()
        Profile.objects.all().delete()
        
        # Import Profiles
        for profile_data in data.get('profiles', []):
            profile = Profile.objects.create(
                full_name=profile_data['full_name'],
                title=profile_data['title'],
                bio=profile_data['bio'],
                about=profile_data['about'],
                email=profile_data['email'],
                linkedin=profile_data.get('linkedin'),
                github=profile_data.get('github'),
                facebook=profile_data.get('facebook'),
            )
            
            # Handle resume file if mentioned
            if profile_data.get('resume'):
                self.stdout.write(f"Note: Resume file '{profile_data['resume']}' needs to be uploaded manually")
        
        # Import Roles
        for role_data in data.get('roles', []):
            Role.objects.create(title=role_data['title'])
        
        # Import Skills
        for skill_data in data.get('skills', []):
            skill = Skill.objects.create(name=skill_data['name'])
            if skill_data.get('icon'):
                self.stdout.write(f"Note: Skill icon '{skill_data['icon']}' needs to be uploaded manually")
        
        # Import Projects
        for project_data in data.get('projects', []):
            project = Project.objects.create(
                title=project_data['title'],
                description=project_data['description'],
                tech_stack=project_data.get('tech_stack', ''),
                github_link=project_data['github_link'],
                live_link=project_data.get('live_link'),
            )
            
            if project_data.get('image'):
                self.stdout.write(f"Note: Project image '{project_data['image']}' needs to be uploaded manually")
        
        # Import Certifications
        for cert_data in data.get('certifications', []):
            certification = Certification.objects.create(
                title=cert_data['title'],
                description=cert_data['description'],
                issuer=cert_data['issuer'],
                date_awarded=datetime.strptime(cert_data['date_awarded'], '%Y-%m-%d').date(),
                certificate_url=cert_data.get('certificate_url'),
            )
            
            if cert_data.get('image'):
                self.stdout.write(f"Note: Certification image '{cert_data['image']}' needs to be uploaded manually")
        
        # Import Profile Photos
        for photo_data in data.get('profile_photos', []):
            try:
                profile = Profile.objects.get(full_name=photo_data['profile_full_name'])
                photo = ProfilePhoto.objects.create(
                    profile=profile,
                    order=photo_data['order']
                )
                
                if photo_data.get('image'):
                    self.stdout.write(f"Note: Profile photo '{photo_data['image']}' needs to be uploaded manually")
            except Profile.DoesNotExist:
                self.stdout.write(f"Warning: Profile '{photo_data['profile_full_name']}' not found for photo")
        
        self.stdout.write(
            self.style.SUCCESS(f'Imported {len(data.get("profiles", []))} profiles, '
                             f'{len(data.get("projects", []))} projects, '
                             f'{len(data.get("skills", []))} skills, '
                             f'{len(data.get("roles", []))} roles, '
                             f'{len(data.get("certifications", []))} certifications')
        )