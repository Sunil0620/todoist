# Django Todo List - Deployment Guide

## Quick Deployment Options

Your project is now ready to deploy! Choose one of these platforms:

---

## 🚀 Option 1: Deploy to Render (Recommended - Free Tier Available)

### Steps:
1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Add deployment configuration"
   git push origin main
   ```

2. **Go to [Render](https://render.com)** and sign up/login

3. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select this repository

4. **Configure the service:**
   - **Name:** todoist (or your preferred name)
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn todoist.wsgi:application`

5. **Add Environment Variables:**
   - `DJANGO_SECRET_KEY`: Generate a new secret key (or use the default for testing)
   - `DJANGO_DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
   - `PYTHON_VERSION`: `3.13.5`

6. **Deploy!** Render will automatically build and deploy your app

7. **Access your app** at `https://your-app-name.onrender.com`

---

## 🚂 Option 2: Deploy to Railway

### Steps:
1. **Push code to GitHub**

2. **Go to [Railway.app](https://railway.app)** and sign up/login

3. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

4. **Railway will auto-detect** the `railway.json` configuration

5. **Add Environment Variables** in the Railway dashboard:
   - `DJANGO_SECRET_KEY`: Your secret key
   - `DJANGO_DEBUG`: `False`
   - `ALLOWED_HOSTS`: `${{RAILWAY_PUBLIC_DOMAIN}}`

6. **Deploy!** Railway handles the rest automatically

---

## 🟣 Option 3: Deploy to Heroku

### Steps:
1. **Install Heroku CLI**
   ```bash
   brew install heroku/brew/heroku  # macOS
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set DJANGO_SECRET_KEY='your-secret-key-here'
   heroku config:set DJANGO_DEBUG=False
   heroku config:set PYTHON_VERSION=3.13.5
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

7. **Open your app**
   ```bash
   heroku open
   ```

---

## 🌐 Option 4: Deploy to PythonAnywhere

### Steps:
1. **Sign up** at [PythonAnywhere](https://www.pythonanywhere.com)

2. **Upload your code** via Git or file upload

3. **Create a virtual environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab → "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code directory
   - Set WSGI configuration file to point to `todoist/wsgi.py`

5. **Set environment variables** in WSGI configuration file

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   python manage.py migrate
   ```

7. **Reload** your web app

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure:

- ✅ All dependencies are in `requirements.txt`
- ✅ `DEBUG = False` in production
- ✅ `SECRET_KEY` is set via environment variable
- ✅ `ALLOWED_HOSTS` includes your domain
- ✅ Database migrations are up to date
- ✅ Static files are configured correctly
- ✅ `.gitignore` excludes sensitive files

---

## 🔒 Security Best Practices

1. **Never commit secrets** to Git
   - Use environment variables for sensitive data
   - Keep `.env` files in `.gitignore`

2. **Generate a strong SECRET_KEY** for production:
   ```python
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

3. **Always set `DEBUG = False`** in production

4. **Use HTTPS** (most platforms provide this automatically)

5. **Keep dependencies updated**
   ```bash
   pip list --outdated
   ```

---

## 🗄️ Database Options

### For Production (Optional):

Your app currently uses SQLite (fine for small apps). For larger apps, consider:

1. **PostgreSQL** (Recommended)
   - Render: Built-in PostgreSQL
   - Railway: One-click PostgreSQL
   - Heroku: Heroku Postgres add-on

2. **Configure DATABASE_URL** environment variable:
   ```
   DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

The app will automatically use it (already configured in `settings.py`)

---

## 🆘 Troubleshooting

### Build fails?
- Check Python version matches `runtime.txt`
- Verify all packages in `requirements.txt` are correct
- Check build logs for specific errors

### Static files not loading?
```bash
python manage.py collectstatic --no-input
```

### Database errors?
```bash
python manage.py migrate
```

### 500 errors?
- Check application logs on your platform
- Verify environment variables are set
- Ensure `ALLOWED_HOSTS` includes your domain

---

## 📞 Support

If you encounter issues:
- Check platform-specific documentation
- Review application logs
- Verify environment variables
- Test locally first with production settings

---

**Good luck with your deployment! 🎉**
