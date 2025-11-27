# Netlify Deployment Guide

## Prerequisites
- Netlify account (https://netlify.com)
- Git repository (sudah ada ✅)
- GitHub/GitLab/Bitbucket account terhubung

## Opsi 1: Deployment via Netlify UI (Recommended untuk Pemula)

### Step 1: Push ke GitHub
```bash
git push origin main
```

### Step 2: Login ke Netlify
1. Buka https://app.netlify.com
2. Klik "Sign up" atau "Log in"
3. Pilih GitHub, GitLab, atau Bitbucket

### Step 3: Connect Repository
1. Klik "New site from Git"
2. Pilih repository provider (GitHub)
3. Authorize Netlify
4. Select repository "sosmed"

### Step 4: Configure Build Settings
1. Build command: `pip install -r requirements.txt`
2. Publish directory: `.`
3. Klik "Deploy site"

### Step 5: Set Environment Variables
1. Buka "Site settings" → "Build & deploy"
2. Klik "Environment"
3. Add environment variables:
   - `DATABASE_URL`: Your database connection string
   - `SECRET_KEY`: Your secret key
   - `FLASK_ENV`: `production`

### Step 6: Redeploy
1. Setelah set environment variables, klik "Trigger deploy"
2. Pilih "Deploy site"

---

## Opsi 2: Deployment via Netlify CLI (Advanced)

### Step 1: Install Netlify CLI
```bash
npm install -g netlify-cli
```

### Step 2: Login ke Netlify
```bash
netlify login
```

### Step 3: Link Repository
```bash
netlify link
```

### Step 4: Set Environment Variables
```bash
netlify env:set DATABASE_URL "your-database-url"
netlify env:set SECRET_KEY "your-secret-key"
netlify env:set FLASK_ENV "production"
```

### Step 5: Deploy
```bash
netlify deploy --prod
```

---

## Opsi 3: Continuous Deployment (GitHub Integration)

### Step 1: Push Code ke GitHub
```bash
git add .
git commit -m "Setup Netlify deployment"
git push origin main
```

### Step 2: Connect ke Netlify
1. Go to https://app.netlify.com/sites
2. Click "New site from Git"
3. Select GitHub and your repository
4. Configure build settings (already in netlify.toml ✅)

### Step 3: Auto Deploy
Setiap kali Anda push ke main branch:
- Netlify otomatis build dan deploy
- Tidak perlu manual deploy lagi!

---

## Database Configuration

### Menggunakan Database Eksternal

Pilihan database untuk Netlify:

#### 1. **Supabase (Recommended)**
```bash
# Buat akun di https://supabase.com
# Dapatkan connection string
# Set di Netlify env
netlify env:set DATABASE_URL "postgresql://user:password@host/database"
```

#### 2. **Railway**
```bash
# Buat akun di https://railway.app
# Deploy database
# Copy connection string ke Netlify
```

#### 3. **Render**
```bash
# Buat akun di https://render.com
# Deploy PostgreSQL
# Set environment variable
```

#### 4. **JawsDB (MySQL)**
```bash
# URL format: mysql+pymysql://user:password@host:port/database
# Set sebagai DATABASE_URL di Netlify
```

---

## Project Structure untuk Netlify

```
sosmed/
├── netlify/
│   └── functions/
│       └── server.py          # Serverless function entry point
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── controllers/
│   └── views/
├── config/
├── .env                        # Local only
├── netlify.toml               # Netlify configuration ✅
├── requirements.txt           # ✅ Updated with gunicorn
├── run.py
└── init_db.py
```

---

## Troubleshooting

### Error: "No module named 'app'"
**Solution:**
```bash
# Update requirements.txt
pip freeze > requirements.txt
```

### Error: "Database connection failed"
**Solution:**
```bash
# Check DATABASE_URL
netlify env:list

# Verify format (for MySQL):
# mysql+pymysql://user:password@host:port/database
```

### Build fails
**Solution:**
1. Cek logs di Netlify dashboard
2. Pastikan requirements.txt lengkap
3. Run locally: `python run.py`

### Functions returning 404
**Solution:**
1. Check netlify/functions folder exists
2. Verify netlify.toml redirects configuration
3. Check build logs for Python errors

---

## Useful Netlify CLI Commands

```bash
# Login
netlify login

# Link repository
netlify link

# Deploy preview
netlify deploy

# Deploy production
netlify deploy --prod

# View environment variables
netlify env:list

# Set environment variable
netlify env:set KEY value

# Remove environment variable
netlify env:unset KEY

# View logs
netlify logs:tail

# View site info
netlify sites:list
```

---

## Performance Tips

1. **Optimize Dependencies**
   ```bash
   pip install pipdeptree
   pipdeptree
   ```

2. **Use Production Config**
   - Set `FLASK_ENV=production`
   - Set `DEBUG=False`

3. **Monitor Build Time**
   - Netlify free plan: max 300 minutes/month
   - Optimize requirements.txt

4. **Database Connection**
   - Use connection pooling
   - Add timeouts

---

## Domain & SSL

### Connect Custom Domain
1. Netlify Dashboard → "Domain settings"
2. Add custom domain
3. Follow DNS instructions
4. SSL auto-generated ✅

### Enable HTTPS
- Automatic with Let's Encrypt ✅
- No additional configuration needed

---

## Continuous Deployment Workflow

```
Local Development
    ↓
git commit
    ↓
git push origin main
    ↓
GitHub receives push
    ↓
Netlify webhook triggered
    ↓
Build (npm/pip install)
    ↓
Deploy
    ↓
Site live at https://your-site.netlify.app
```

---

## Check Deployment Status

```bash
# Via CLI
netlify status

# Via Dashboard
# https://app.netlify.com
```

---

## Next Steps

1. ✅ Setup files created (netlify.toml, functions/server.py)
2. Push to GitHub: `git push origin main`
3. Login ke Netlify: `netlify login` atau visit app.netlify.com
4. Connect repository
5. Set environment variables
6. Deploy! 🚀

---

## Quick Deploy Steps

```bash
# 1. Install CLI
npm install -g netlify-cli

# 2. Login
netlify login

# 3. Link site (first time)
netlify link

# 4. Set environment variables
netlify env:set DATABASE_URL "your-db-url"
netlify env:set SECRET_KEY "your-secret"
netlify env:set FLASK_ENV "production"

# 5. Deploy
netlify deploy --prod

# 6. Initialize database (if needed)
# Run once: python init_db.py
```
