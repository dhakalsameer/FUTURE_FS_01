# Django Portfolio - Sameer Dhakal

A modern, responsive portfolio website built with Django 4.2.11, featuring dynamic content management, beautiful animations, and deployment-ready configuration.

## 🌟 Features

- **Dynamic Portfolio Management**: Admin panel for managing projects, skills, certifications, and profile information
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Modern UI/UX**: Smooth animations, dark/light theme toggle, interactive elements
- **Media Management**: Image uploads for projects, skills, certifications, and profile photos
- **Contact Form**: Functional contact form with email integration
- **Resume Display**: Embedded PDF resume viewer with download option
- **Production Ready**: Docker containerized with Render deployment configuration

## 🛠️ Tech Stack

- **Backend**: Django 4.2.11, Python 3.10+
- **Frontend**: Tailwind CSS (CDN), Vanilla JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Docker, Render
- **Email**: Gmail SMTP (for contact form)

## 📁 Project Structure

```
FUTURE_FS_01/
├── portfolio/                    # Main Django app
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # App URLs
│   ├── admin.py                 # Admin configuration
│   ├── forms.py                 # Django forms
│   ├── management/              # Custom management commands
│   │   ├── commands/
│   │   │   ├── create_sample_data.py
│   │   │   ├── export_data.py
│   │   │   ├── import_data.py
│   │   │   ├── fix_media_files.py
│   │   │   └── fix_double_paths.py
│   └── migrations/              # Database migrations
├── portfolio_project/           # Django project settings
│   ├── settings.py             # Development settings
│   ├── settings_production.py  # Production settings
│   └── settings_render.py      # Render-specific settings
├── templates/                   # HTML templates
│   └── portfolio/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── contact.html
│       └── health.html
├── media/                       # User uploaded files
│   ├── projects/
│   ├── skills/
│   ├── certifications/
│   ├── profile_photos/
│   └── resume/
├── static/                      # Static files (if needed)
├── Dockerfile                   # Docker configuration
├── render.yaml                  # Render deployment config
├── start.sh                     # Production startup script
├── requirements.txt             # Python dependencies
└── manage.py                    # Django management script
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip and virtualenv
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhakalsameer/FUTURE_FS_01.git
   cd FUTURE_FS_01
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create sample data (or import your own)**
   ```bash
   # Option 1: Create sample data
   python manage.py create_sample_data
   
   # Option 2: Import real data (if you have portfolio_data.json)
   python manage.py import_data
   python manage.py fix_media_files
   python manage.py fix_double_paths
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Health check: http://127.0.0.1:8000/health/

### Admin Panel Access

Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit `/admin/` to manage your portfolio content.

## 📊 Database Models

### Profile
- Personal information (name, title, bio, email)
- Social media links (LinkedIn, GitHub, Facebook)
- Resume file upload

### Project
- Project details (title, description, tech stack)
- GitHub and live demo links
- Project image upload

### Skill
- Skill name and icon upload
- Progress tracking

### Role
- Professional roles/titles

### Certification
- Certification details (title, description, issuer)
- Date awarded and certificate URL
- Certificate image upload

### ProfilePhoto
- Profile photos with order management

## 🎨 Customization

### Adding Your Own Data

1. **Via Admin Panel**: Easiest method - use `/admin/` to add your content
2. **Via Management Commands**: Use the provided commands for bulk operations

#### Export/Import Commands
```bash
# Export current data
python manage.py export_data

# Import data from JSON
python manage.py import_data

# Fix media file associations
python manage.py fix_media_files
python manage.py fix_double_paths
```

### Customizing Styles

The template uses Tailwind CSS with custom CSS variables for theming:

```css
[data-theme="dark"] {
  --bg: #0f172a;
  --accent: #3b82f6;
  /* ... */
}

[data-theme="light"] {
  --bg: #ffffff;
  --accent: #3b82f6;
  /* ... */
}
```

## 🌐 Deployment

### Render Deployment

The project is pre-configured for Render deployment:

1. **Connect your GitHub repository** to Render
2. **Render will automatically detect** the Docker configuration
3. **Environment variables** are set in `render.yaml`
4. **The deployment will**:
   - Build the Docker image
   - Run migrations
   - Import your portfolio data
   - Fix media file associations
   - Start the application

### Manual Deployment

1. **Build Docker image**
   ```bash
   docker build -t django-portfolio .
   ```

2. **Run with environment variables**
   ```bash
   docker run -p 8000:8000 \
     -e DJANGO_SETTINGS_MODULE=portfolio_project.settings_render \
     -e ALLOWED_HOSTS=yourdomain.com \
     django-portfolio
   ```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SETTINGS_MODULE` | Django settings module | `portfolio_project.settings_render` |
| `ALLOWED_HOSTS` | Allowed hosts for Django | `localhost,127.0.0.1` |
| `DEBUG` | Django debug mode | `False` |
| `SECRET_KEY` | Django secret key | Auto-generated |
| `EMAIL_HOST_*` | Email configuration for contact form | Gmail SMTP |

## 📧 Email Configuration

Configure the contact form by setting these environment variables:

```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

**Note**: Use an App Password for Gmail, not your regular password.

## 🔧 Management Commands

### Data Management
- `create_sample_data`: Create sample portfolio data
- `export_data`: Export all data to JSON
- `import_data`: Import data from JSON
- `fix_media_files`: Associate media files with database records
- `fix_double_paths`: Fix double path issues in media files

### Django Built-in
- `migrate`: Run database migrations
- `collectstatic`: Collect static files for production
- `createsuperuser`: Create admin user
- `runserver`: Start development server

## 🐛 Troubleshooting

### Common Issues

1. **Images not showing**
   ```bash
   python manage.py fix_media_files
   python manage.py fix_double_paths
   ```

2. **Static files not loading**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Database errors**
   ```bash
   python manage.py migrate --noinput
   ```

4. **Permission errors**
   ```bash
   chmod +x start.sh
   ```

### Health Check

Visit `/health/` to check:
- Database connection status
- Object counts in database
- Overall application health

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

- **Portfolio**: https://future-fs-01-a6ek.onrender.com
- **Email**: sameerdhakal1234@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/sameer-dhakal-712b69301/
- **GitHub**: https://github.com/dhakalsameer

---

⭐ **Star this repository if it helped you!**