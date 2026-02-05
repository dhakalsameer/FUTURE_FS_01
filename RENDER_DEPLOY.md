# Render Deployment Guide for Django Portfolio

## **🎯 Why Render?**
- ✅ **Free tier** with generous limits
- ✅ **Modern Docker-based deployment**
- ✅ **Automatic HTTPS**
- ✅ **GitHub integration**
- ✅ **Easy updates**
- ✅ **Better performance** than PythonAnywhere

## **📋 Step 1: Prepare Your Project**

### **1. Create render.yaml**
Create this file in your project root:

```yaml
services:
  - type: web
    name: django-portfolio
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio_project.wsgi:application
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: portfolio_project.settings_production
      - key: PYTHON_VERSION
        value: 3.10.12
```

### **2. Update Production Settings**
Make sure your `settings_production.py` has:

```python
# Security
DEBUG = False
ALLOWED_HOSTS = ['your-app-name.onrender.com', 'localhost', '127.0.0.1']

# Database (Render PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
```

### **3. Add Gunicorn to Requirements**
Update your `requirements.txt`:

```
Django==4.2.11
python-dotenv==1.2.1
Pillow==10.2.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

## **📋 Step 2: Deploy to Render**

### **1. Push to GitHub**
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### **2. Sign Up for Render**
1. Go to [render.com](https://render.com)
2. Click **"Sign Up"**
3. Choose **GitHub** (recommended)
4. Authorize Render to access your repositories

### **3. Create New Web Service**
1. Click **"New +"** → **"Web Service"**
2. Select your **FUTURE_FS_01** repository
3. Render will detect your `render.yaml` automatically
4. Click **"Advanced Settings"**
5. Add environment variables (see below)
6. Click **"Create Web Service"**

### **4. Set Environment Variables**
In Render dashboard, add these:

**Required:**
- `DJANGO_SETTINGS_MODULE` = `portfolio_project.settings_production`
- `SECRET_KEY` = `your-secret-key-here`
- `DEBUG` = `False`

**Email (optional):**
- `EMAIL_HOST_USER` = `your-email@gmail.com`
- `EMAIL_HOST_PASSWORD` = `your-app-password`

### **5. Deploy!**
Render will automatically:
- Build your application
- Install dependencies
- Run migrations
- Start your server
- Provide HTTPS

## **🎉 Your Site Will Be Live At:**
`https://your-app-name.onrender.com`

## **🔄 Updates Are Easy:**
1. Make changes to your code
2. `git add . && git commit -m "Update" && git push`
3. Render auto-deploys! 🚀

## **🛠️ Troubleshooting**

### **Common Issues:**
- **Build fails**: Check requirements.txt and render.yaml
- **Database errors**: Ensure PostgreSQL settings are correct
- **Static files**: Check STATIC_ROOT setting

### **Logs:**
- View logs in Render dashboard
- Check build logs and server logs

---

**🎯 Ready to deploy?** Just follow these steps and your portfolio will be live on Render!