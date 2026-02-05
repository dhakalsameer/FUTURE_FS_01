# 🚀 Sameer07's PythonAnywhere Deployment

## **Step 1: Upload Your Project**
1. Log into PythonAnywhere
2. Go to **Files** tab
3. Click **"Upload a file"**
4. Upload your entire project as a ZIP file
5. Right-click the ZIP → **"Extract here"**

## **Step 2: Open Console**
1. Go to **Consoles** tab
2. Click **"Bash"**
3. Run these commands:

```bash
cd FUTURE_FS_01
mkvirtualenv --python=/usr/bin/python3.10 portfolioenv
pip install -r requirements.txt
```

## **Step 3: Set Up Web App**
1. Go to **Web** tab
2. Click **"Add a new web app"**
3. Choose **"Manual Configuration"**
4. Select **"Python 3.10"**
5. Click **Next**

## **Step 4: Configure Web App**
**Source code:** `/home/sameer07/FUTURE_FS_01`  
**Working directory:** `/home/sameer07/FUTURE_FS_01`  
**Virtualenv:** `/home/sameer07/.virtualenvs/portfolioenv`  
**WSGI file:** `/home/sameer07/FUTURE_FS_01/wsgi_pythonanywhere.py`

## **Step 5: Set Static Files**
In the **Static files** section:
- **URL:** `/static/` → **Directory:** `/home/sameer07/FUTURE_FS_01/staticfiles`
- **URL:** `/media/` → **Directory:** `/home/sameer07/FUTURE_FS_01/media`

## **Step 6: Deploy!**
In the Bash console:
```bash
cd /home/sameer07/FUTURE_FS_01
chmod +x deploy.sh
./deploy.sh
```

## **Step 7: Go Live!**
1. In **Web** tab, click **🔄 Reload**
2. Visit: **https://sameer07.pythonanywhere.com**
3. 🎉 **Your portfolio is LIVE!**

---

**Need help?** I'm here! Just tell me what step you're on!