# AGENTS.md - Django Portfolio Project Guide

This file contains essential information for agentic coding agents working on this Django portfolio project.

## Project Overview

**Type:** Django 4.2.11 personal portfolio website
**Database:** SQLite3 (development)
**Frontend:** Django templates with Tailwind CSS (CDN)
**Key Features:** Projects showcase, skills, certifications, contact form

## Essential Commands

### Development Commands
```bash
python3 manage.py runserver                    # Start development server (default: 8000)
python3 manage.py runserver 0.0.0.0:8000       # Start server on all interfaces
python3 manage.py migrate                      # Apply database migrations
python3 manage.py makemigrations               # Create new migration files
python3 manage.py collectstatic               # Collect static files for production
python3 manage.py createsuperuser              # Create admin user
```

### Testing Commands
```bash
python3 manage.py test                         # Run all tests
python3 manage.py test portfolio               # Run tests for portfolio app only
python3 manage.py test portfolio.tests.ModelTest  # Run specific test class
python3 manage.py test --verbosity=2           # Run tests with detailed output
```

### Database Management
```bash
python3 manage.py shell                        # Django shell for debugging
python3 manage.py dbshell                      # Direct database shell (SQLite)
python3 manage.py showmigrations               # Show migration status
```

## Code Style Guidelines

### Python/Django Conventions

#### Import Organization
```python
# 1. Standard library imports
import os
from pathlib import Path

# 2. Django imports
from django.db import models
from django.contrib import admin
from django.shortcuts import render, redirect

# 3. Third-party imports
from dotenv import load_dotenv

# 4. Local imports
from .models import Profile, Project
```

#### Naming Conventions
- **Models:** PascalCase (Profile, Project, Skill, Certification)
- **Fields:** snake_case (full_name, tech_stack, created_at)
- **Views/Functions:** snake_case (home_view, project_detail)
- **URL Names:** snake_case (home, about, projects, contact)
- **Templates:** kebab-case (base-template.html, project-detail.html)
- **CSS Classes:** Tailwind utilities with custom components

#### Model Patterns
```python
class ModelName(models.Model):
    field_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Model Name"
        verbose_name_plural = "Model Names"
    
    def __str__(self):
        return f"{self.field_name}"
```

#### View Patterns
```python
def view_name(request):
    if request.method == 'POST':
        # Handle POST data
        return redirect('success_url')
    
    # Handle GET request
    context = {'key': 'value'}
    return render(request, 'template.html', context)
```

### Error Handling Patterns

#### Email/External Services
```python
try:
    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )
    messages.success(request, "Operation completed successfully!")
except Exception as e:
    messages.error(request, f"Error occurred: {str(e)}")
    # Log error if needed
```

#### Database Operations
```python
try:
    object = ModelName.objects.get(pk=pk)
except ModelName.DoesNotExist:
    messages.error(request, "Item not found.")
    return redirect('fallback_url')
```

## File Structure Conventions

### Templates
- Location: `templates/portfolio/`
- Naming: kebab-case.html
- Base template: `base-template.html`
- Always extend base template: `{% extends 'portfolio/base-template.html' %}`

### Static Files
- CSS: `static/css/`
- Images: `static/images/`
- Use Tailwind CSS classes primarily
- Custom CSS for specific animations/components

### Media Files
- User uploads: `media/`
- Profile images: `media/profile_images/`
- Project images: `media/project_images/`

## Database Best Practices

### Model Relationships
```python
# Foreign Keys with proper cascade
project = models.ForeignKey(Project, on_delete=models.CASCADE)

# Many-to-Many with descriptive through
skills = models.ManyToManyField(Skill, blank=True)

# Optional fields
optional_field = models.CharField(max_length=100, blank=True, null=True)
```

### Migration Workflow
1. Create model: `python3 manage.py makemigrations`
2. Review migration file
3. Apply migration: `python3 manage.py migrate`
4. Test in admin interface

## Admin Configuration

### Standard Admin Registration
```python
@admin.register(ModelName)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
```

## Environment Variables

### Required .env Variables
```
DEBUG=True
SECRET_KEY=your-secret-key-here
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Security Notes
- Never commit .env file
- Use app passwords for Gmail, not regular passwords
- Set DEBUG=False in production

## Testing Guidelines

### Test Structure
```python
from django.test import TestCase
from .models import ModelName

class ModelNameTest(TestCase):
    def setUp(self):
        # Create test objects
        pass
    
    def test_model_creation(self):
        # Test model creation
        pass
    
    def test_str_method(self):
        # Test __str__ method
        pass
```

### Test Coverage Priorities
1. Model methods and properties
2. View responses and context
3. Form validation
4. Admin functionality

## Common Patterns

### URL Configuration
```python
# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]
```

### Form Handling
```python
# forms.py
from django import forms
from .models import ModelName

class ModelNameForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = ['field1', 'field2']
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border'}),
        }
```

## Deployment Notes

### Static Files
- Run `python3 manage.py collectstatic` before deployment
- Configure STATIC_ROOT in production settings

### Database
- SQLite for development only
- Consider PostgreSQL for production
- Backup database before major changes

## Common Issues & Solutions

### Migration Conflicts
- Delete migration files except `__init__.py`
- Run `python3 manage.py makemigrations`
- Run `python3 manage.py migrate`

### Static Files Not Loading
- Run `python3 manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT settings
- Verify DEBUG setting affects static file serving

### Email Not Sending
- Verify Gmail app password (not regular password)
- Check EMAIL_HOST and EMAIL_PORT settings
- Ensure less secure apps access is enabled for Gmail

## Development Workflow

1. Make changes to models/views/templates
2. Run `python3 manage.py makemigrations` if model changes
3. Run `python3 manage.py migrate`
4. Test with `python3 manage.py runserver`
5. Check admin interface for model changes
6. Write tests for new functionality
7. Run `python3 manage.py test` before committing