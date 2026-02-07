import json
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from portfolio.models import Profile, Project, Skill, Role, Certification, ProfilePhoto


class Command(BaseCommand):
    help = 'Export all portfolio data to JSON file'

    def handle(self, *args, **options):
        data = {}
        
        # Export Profile
        profiles = Profile.objects.all()
        data['profiles'] = []
        for profile in profiles:
            profile_data = {
                'full_name': profile.full_name,
                'title': profile.title,
                'bio': profile.bio,
                'about': profile.about,
                'email': profile.email,
                'linkedin': profile.linkedin,
                'github': profile.github,
                'facebook': profile.facebook,
                'resume': profile.resume.name if profile.resume else None,
            }
            data['profiles'].append(profile_data)
        
        # Export Projects
        projects = Project.objects.all()
        data['projects'] = []
        for project in projects:
            project_data = {
                'title': project.title,
                'description': project.description,
                'tech_stack': project.tech_stack,
                'github_link': project.github_link,
                'live_link': project.live_link,
                'image': project.image.name if project.image else None,
                'created_at': project.created_at.isoformat(),
            }
            data['projects'].append(project_data)
        
        # Export Skills
        skills = Skill.objects.all()
        data['skills'] = []
        for skill in skills:
            skill_data = {
                'name': skill.name,
                'icon': skill.icon.name if skill.icon else None,
            }
            data['skills'].append(skill_data)
        
        # Export Roles
        roles = Role.objects.all()
        data['roles'] = []
        for role in roles:
            data['roles'].append({
                'title': role.title,
            })
        
        # Export Certifications
        certifications = Certification.objects.all()
        data['certifications'] = []
        for cert in certifications:
            cert_data = {
                'title': cert.title,
                'description': cert.description,
                'issuer': cert.issuer,
                'date_awarded': cert.date_awarded.isoformat(),
                'certificate_url': cert.certificate_url,
                'image': cert.image.name if cert.image else None,
            }
            data['certifications'].append(cert_data)
        
        # Export Profile Photos
        photos = ProfilePhoto.objects.all()
        data['profile_photos'] = []
        for photo in photos:
            photo_data = {
                'profile_full_name': photo.profile.full_name,
                'image': photo.image.name if photo.image else None,
                'order': photo.order,
            }
            data['profile_photos'].append(photo_data)
        
        # Save to file
        with open('portfolio_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, cls=DjangoJSONEncoder)
        
        self.stdout.write(
            self.style.SUCCESS(f'Exported {len(profiles)} profiles, {len(projects)} projects, '
                             f'{len(skills)} skills, {len(roles)} roles, '
                             f'{len(certifications)} certifications, {len(photos)} photos')
        )
        self.stdout.write(self.style.SUCCESS('Data saved to portfolio_data.json'))