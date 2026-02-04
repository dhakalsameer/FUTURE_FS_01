from django.shortcuts import render
from .models import Project
from .forms import ContactForm
# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, "projects.html", {"projects": projects})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {
                "form": ContactForm(),
                "success": True
            })
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
