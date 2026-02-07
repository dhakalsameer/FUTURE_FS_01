from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Profile, Project, Skill, Role, ProfilePhoto, Certification


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    roles = Role.objects.all()
    certifications = Certification.objects.all()

    photos = ProfilePhoto.objects.filter(profile=profile).order_by('order') if profile else []


    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "photos": photos,
        "roles": roles,
        "certifications": certifications,
        'is_linux': False,
    }

    return render(request, "portfolio/home.html", context)

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')


def health_check(request):
    """Simple health check endpoint for debugging"""
    from django.db import connection
    from portfolio.models import Profile, Project, Skill, Role, Certification
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
    
    # Count objects
    try:
        profile_count = Profile.objects.count()
        project_count = Project.objects.count()
        skill_count = Skill.objects.count()
        role_count = Role.objects.count()
        cert_count = Certification.objects.count()
        data_status = "OK"
    except Exception as e:
        profile_count = project_count = skill_count = role_count = cert_count = 0
        data_status = f"ERROR: {str(e)}"
    
    context = {
        'status': 'healthy',
        'database': db_status,
        'data': data_status,
        'counts': {
            'profiles': profile_count,
            'projects': project_count,
            'skills': skill_count,
            'roles': role_count,
            'certifications': cert_count,
        }
    }
    
    return render(request, 'portfolio/health.html', context)


# ================= CONTACT FORM =================
def contact_send_email(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Portfolio Contact Form: {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,  # From (your email)
                [settings.DEFAULT_FROM_EMAIL],  # To (your email)
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {str(e)}")

        # Redirect to Home page
        return redirect(request.META.get("HTTP_REFERER", "home"))


    # If someone accesses this URL via GET
    return redirect("home")