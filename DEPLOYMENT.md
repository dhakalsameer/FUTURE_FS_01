# PythonAnywhere Deployment Guide

This guide will help you deploy your Django portfolio to PythonAnywhere with free tier and dynamic content updates.

## 🚀 Quick Start

### 1. Sign Up for PythonAnywhere
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for a **Free** account
3. Verify your email address

### 2. Set Up Your Account
1. Go to the **Dashboard** → **Account**
2. Note your username (e.g., `yourusername.pythonanywhere.com`)

## 📁 Project Setup

### 1. Upload Your Project
**Option A: Using Git (Recommended)**
```bash
# On PythonAnywhere console
git clone https://github.com/yourusername/FUTURE_FS_01.git
cd FUTURE_FS_01
```

**Option B: Using Web Upload**
1. Go to **Files** tab in PythonAnywhere
2. Upload your project files
3. Extract if uploaded as ZIP

### 2. Set Up Virtual Environment
```bash
# On PythonAnywhere console
mkvirtualenv --python=/usr/bin/python3.10 portfolioenv
workon portfolioenv
pip install -r requirements.txt
```

### 3. Configure Environment Variables
1. Copy `.env.production` to `.env`
2. Update with your values:
```bash
cp .env.production .env
nano .env  # Edit with your details
```

**Important variables to update:**
- `SECRET_KEY`: Generate a new secret key
- `ALLOWED_HOSTS`: Set to `yourusername.pythonanywhere.com`
- `EMAIL_HOST_USER`: Your Gmail address
- `EMAIL_HOST_PASSWORD`: Your Gmail app password

## 🌐 Web App Configuration

### 1. Create Web App
1. Go to **Web** tab in PythonAnywhere
2. Click **"Add a new web app"**
3. Choose **"Manual Configuration"**
4. Select **"Python 3.10"**
5. Click **Next**

### 2. Configure Web App
**Source Code:**
- Path: `/home/yourusername/FUTURE_FS_01`

**Working Directory:**
- Path: `/home/yourusername/FUTURE_FS_01`

**Virtual Environment:**
- Path: `/home/yourusername/.virtualenvs/portfolioenv`

**WSGI Configuration File:**
- Path: `/home/yourusername/FUTURE_FS_01/wsgi_pythonanywhere.py`

### 3. Update WSGI File
Edit `/home/yourusername/FUTURE_FS_01/wsgi_pythonanywhere.py`:
```python
# Replace 'yourusername' with your actual PythonAnywhere username
project_home = '/home/yourusername/FUTURE_FS_01'
activate_this = '/home/yourusername/.virtualenvs/portfolioenv/bin/activate'
```

### 4. Update Production Settings
Edit `/home/yourusername/FUTURE_FS_01/portfolio_project/settings_production.py`:
```python
# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]
```

## 🎨 Static Files Configuration

### 1. Set Static Files URL
In the **Web** tab:
- **Static files URL**: `/static/`
- **Directory**: `/home/yourusername/FUTURE_FS_01/staticfiles`

### 2. Set Media Files URL
- **Static files URL**: `/media/`
- **Directory**: `/home/yourusername/FUTURE_FS_01/media`

## 🗄️ Database Setup

### 1. Run Migrations
```bash
cd /home/yourusername/FUTURE_FS_01
workon portfolioenv
python manage.py migrate --settings=portfolio_project.settings_production
```

### 2. Create Superuser
```bash
python manage.py createsuperuser --settings=portfolio_project.settings_production
```

### 3. Collect Static Files
```bash
python manage.py collectstatic --noinput --settings=portfolio_project.settings_production
```

## 🔄 Deployment & Updates

### 1. Initial Deployment
```bash
cd /home/yourusername/FUTURE_FS_01
chmod +x deploy.sh
./deploy.sh
```

### 2. Update Your Site
When you make changes to your code:

**Option A: Using Git (Easy)**
```bash
cd /home/yourusername/FUTURE_FS_01
git pull origin main
./deploy.sh
```

**Option B: Manual Update**
1. Upload changed files
2. Run deployment script:
```bash
cd /home/yourusername/FUTURE_FS_01
./deploy.sh
```

### 3. Restart Web App
In the **Web** tab, click the **🔄 Reload** button or run:
```bash
touch /var/www/www_yourusername_pythonanywhere_com_wsgi.py
```

## 📧 Email Configuration

### 1. Gmail App Password
1. Enable 2-factor authentication on Gmail
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Create a new app password
4. Use this password in your `.env` file

### 2. Test Email
1. Go to your site's contact form
2. Send a test message
3. Check your Gmail inbox

## 🛠️ Troubleshooting

### Common Issues:

**1. 502 Bad Gateway**
- Check if virtual environment is activated
- Verify WSGI file paths are correct
- Restart web app

**2. Static Files Not Loading**
- Run `collectstatic` again
- Check static file paths in Web tab
- Verify `STATIC_ROOT` setting

**3. Database Errors**
- Run migrations: `python manage.py migrate`
- Check file permissions on `db.sqlite3`

**4. Email Not Sending**
- Verify Gmail app password
- Check email settings in `.env`
- Ensure `EMAIL_HOST_USER` is set

### Debug Mode:
To enable debug mode temporarily:
```bash
# In .env file
DEBUG=True
```
Then reload your web app.

## 📊 Monitoring

### 1. Access Logs
In the **Web** tab, click **Logs** to see:
- Access logs
- Error logs
- Server logs

### 2. Django Admin
Access your admin panel:
`https://yourusername.pythonanywhere.com/admin/`

## 🔄 Dynamic Content Updates

Your portfolio supports dynamic updates through:

### 1. Django Admin Panel
- Add/edit projects
- Update skills
- Manage certifications
- Change profile information

### 2. Contact Form
- Messages sent to your email
- Real-time notifications

### 3. Media Uploads
- Upload new project images
- Update profile photos
- Add certification images

## 🎯 Next Steps

1. **Custom Domain** (Optional)
   - Upgrade to paid account
   - Point your domain to PythonAnywhere

2. **SSL Certificate** (Free)
   - Enable HTTPS in Web tab
   - PythonAnywhere provides free SSL

3. **Performance Optimization**
   - Use Django caching
   - Optimize images
   - Monitor resource usage

## 📞 Support

- **PythonAnywhere Docs**: [docs.pythonanywhere.com](https://docs.pythonanywhere.com)
- **Django Docs**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Community Forum**: [pythonanywhere.com/forums](https://www.pythonanywhere.com/forums)

---

**🎉 Congratulations!** Your Django portfolio is now live on PythonAnywhere with free hosting and dynamic content updates!