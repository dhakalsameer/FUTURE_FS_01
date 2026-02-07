from django.core.management.base import BaseCommand
from portfolio.models import Profile, Project, Skill, Role, Certification


class Command(BaseCommand):
    help = 'Create sample data for the portfolio if it does not exist'

    def handle(self, *args, **options):
        # Check if data already exists
        if Profile.objects.exists():
            self.stdout.write(self.style.SUCCESS('Sample data already exists'))
            return

        # Create Profile
        profile = Profile.objects.create(
            full_name="Sameer Dhakal",
            title="Web Developer",
            bio="A backend-focused Web Developer & Web3 Enthusiast from Nepal 🇳🇵.",
            about="I'm Sameer Dhakal, a backend-focused Web Developer and Web3 enthusiast with a passion for building scalable, functional, and production-ready web applications.",
            email="sameerdhakal1234@gmail.com",
            linkedin="https://linkedin.com/in/sameerdhakal",
            github="https://github.com/dhakalsameer"
        )
        
        # Create Roles
        roles = [
            Role.objects.create(title="Full Stack Developer"),
            Role.objects.create(title="Backend Developer"),
            Role.objects.create(title="Web3 Developer"),
            Role.objects.create(title="Python Developer")
        ]
        
        # Create Skills
        skills = [
            Skill.objects.create(name="Python"),
            Skill.objects.create(name="Django"),
            Skill.objects.create(name="JavaScript"),
            Skill.objects.create(name="React"),
            Skill.objects.create(name="PostgreSQL")
        ]
        
        # Create Projects
        Project.objects.create(
            title="Django Reservation System",
            description="A comprehensive reservation system built with Django, featuring user authentication, booking management, and payment integration.",
            tech_stack="Django, PostgreSQL, Bootstrap, Stripe",
            github_link="https://github.com/dhakalsameer/django-reservation"
        )
        
        Project.objects.create(
            title="Local Services Marketplace",
            description="A platform connecting local service providers with customers, featuring reviews, booking system, and real-time chat.",
            tech_stack="Django, WebSocket, React, PostgreSQL",
            github_link="https://github.com/dhakalsameer/local-marketplace",
            live_link="https://local-services-demo.com"
        )
        
        Project.objects.create(
            title="PHP Blog Project",
            description="A feature-rich blogging platform built with PHP, including markdown support, user management, and SEO optimization.",
            tech_stack="PHP, MySQL, JavaScript, Bootstrap",
            github_link="https://github.com/dhakalsameer/php-blog"
        )
        
        # Create Certifications
        Certification.objects.create(
            title="Django Web Development",
            description="Advanced Django development including REST APIs, authentication, and deployment strategies.",
            issuer="Coursera",
            date_awarded="2024-01-15",
            certificate_url="https://coursera.org/verify/django-cert"
        )
        
        Certification.objects.create(
            title="Python Programming Expert",
            description="Comprehensive Python programming course covering data structures, algorithms, and best practices.",
            issuer="Udemy",
            date_awarded="2023-12-01",
            certificate_url="https://udemy.com/certificate/python-cert"
        )
        
        Certification.objects.create(
            title="Web3 Blockchain Development",
            description="Complete blockchain development course covering smart contracts, DApps, and Web3 integration.",
            issuer="Consensys",
            date_awarded="2024-02-01",
            certificate_url="https://consensys.org/verify/web3-cert"
        )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully'))