# Heroku Hackathon 201 🚀

**Ready-to-deploy FastAPI template for hackathons - tested and working!**

## 🎯 What You Get

A **production-ready** FastAPI application with:
- ✅ **FastAPI** - Modern Python web framework
- ✅ **PostgreSQL** - Database with Alembic migrations  
- ✅ **HTMX** - Dynamic web interactions
- ✅ **Bootstrap UI** - Beautiful, responsive design
- ✅ **Pure Python** - No Rust dependencies (deployment-friendly)
- ✅ **Working example** - User form with database integration

**Live Demo:** https://heroku-hackathon-201-ff8cc9e77841.herokuapp.com/

## ⚡ Quick Environment Check

Run these commands to verify you're ready to deploy:

```bash
python --version   # Should show 3.11+
git --version     # Should work
heroku --version  # Should work
```

✅ **All working?** → Continue to Quick Deploy  
❌ **Missing something?** → Check [Complete Setup Guide](#complete-setup-guide) below

## 🚀 Quick Deploy (5 Minutes)

```bash
# 1. Get the code (fork first on GitHub, then clone your fork)
git clone https://github.com/YOUR-USERNAME/heroku-hackathon-201.git
cd heroku-hackathon-201

# 2. Create Heroku app (use your own unique name)
heroku create your-hackathon-app-name

# 3. Add PostgreSQL database  
heroku addons:create heroku-postgresql:essential-0

# 4. Deploy the code
git push heroku main

# 5. Set up database
heroku run "python -m alembic upgrade head"

# 6. Open your app
heroku open
```

🎉 **That's it!** Your app should be live and ready for customization.

---

<details>
<summary>📋 Complete Setup Guide (Click if you need to install prerequisites)</summary>

## Complete Setup Guide

### Step 1: Install Python 3.11

**⚠️ Important:** Use Python 3.11 specifically - newer versions have compatibility issues.

#### Windows
```bash
# Option A: Download from python.org
# Go to https://www.python.org/downloads/ and download Python 3.11.x

# Option B: Using Chocolatey
choco install python --version=3.11.0
```

#### macOS
```bash
# Option A: Using Homebrew (recommended)
brew install python@3.11

# Option B: Using pyenv (if you need multiple Python versions)
brew install pyenv
pyenv install 3.11.12
pyenv global 3.11.12
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev
```

### Step 2: Install Git
```bash
# Windows (Chocolatey)
choco install git

# macOS (Homebrew)
brew install git

# Linux
sudo apt install git
```

### Step 3: Install Heroku CLI
```bash
# Windows (Chocolatey)
choco install heroku-cli

# macOS (Homebrew)
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 4: Set up Accounts
1. **GitHub Account** - Sign up at https://github.com (free)
2. **Heroku Account** - Sign up at https://heroku.com
3. **Add Credit Card** to Heroku (required for PostgreSQL addon ~$5/month)

### Step 5: Configure Git (First time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 6: Login to Heroku
```bash
heroku login
```

### Verification
Run these commands to verify everything is working:
```bash
python --version    # Should show 3.11.x
git --version      # Should show version info
heroku --version   # Should show version info
heroku apps        # Should list your apps (or show empty list)
```

</details>

<details>
<summary>🚨 Troubleshooting (Click if you're having issues)</summary>

## Troubleshooting Guide

### ❌ Python Version Issues

**Problem:** `python --version` shows wrong version or "command not found"

**Solutions:**
```bash
# Try python3 instead
python3 --version

# Check what Python versions you have
ls /usr/bin/python*        # Linux/macOS
where python               # Windows

# Use specific Python version
python3.11 -m venv venv    # Create venv with Python 3.11
```

### ❌ "RuntimeError: Directory 'app/static' does not exist"

**Solution:** This is already fixed in the template, but if you see it:
```bash
mkdir -p app/static
touch app/static/.gitkeep
git add app/static/.gitkeep
git commit -m "Add static directory"
git push heroku main
```

### ❌ "No module named 'pydantic_core'" or Rust compilation errors

**Solution:** This template uses Pydantic v1 (pure Python). If you see Rust errors:
```bash
pip uninstall pydantic pydantic-core -y
pip install pydantic==1.10.14
```

### ❌ R10 Boot timeout / 503 Service Unavailable

**Check logs first:**
```bash
heroku logs --app your-app-name --tail
```

**Common fixes:**
1. **Missing static directory** (see solution above)
2. **Wrong Python version** - ensure you're using Python 3.11
3. **Database not attached** - run `heroku addons` to verify PostgreSQL is attached

### ❌ "postgres dialect" database errors

**Solution:** Already fixed in this template! The config automatically handles Heroku's `postgres://` URLs.

### ❌ Permission denied / Access errors

**Windows users:**
```bash
# Use virtual environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS/Linux users:**
```bash
# Use virtual environment
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ Heroku CLI not found

**Check PATH:**
```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="/usr/local/bin:$PATH"

# Then reload your shell
source ~/.bashrc  # or ~/.zshrc
```

### ❌ "App name already taken"

**Solution:** App names must be unique globally. Try:
```bash
heroku create your-unique-app-name-$(date +%s)
```

### ❌ Git push fails

**Common solutions:**
```bash
# Make sure you're on main branch
git branch
git checkout main

# Check git remote
git remote -v

# If heroku remote is missing
heroku git:remote -a your-app-name
```

### 🆘 Still stuck?

1. **Check the working demo:** https://heroku-hackathon-201-ff8cc9e77841.herokuapp.com/
2. **Compare your setup** to the working example
3. **Use `heroku logs --app your-app-name --tail`** for real-time debugging
4. **Ensure you're following the exact Python 3.11 requirement**

</details>

<details>
<summary>🛠️ Local Development (Optional)</summary>

## Local Development Setup

### Quick Local Setup
```bash
# After cloning (from step 1 above)
# Create virtual environment with Python 3.11
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set local database URL (optional)
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/hackathon_db"

# Start the development server
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```

### Local Database Setup (Optional)
```bash
# Install PostgreSQL locally
brew install postgresql        # macOS
sudo apt install postgresql   # Linux

# Create local database
createdb hackathon_db

# Run migrations
alembic upgrade head
```

### Development Workflow
1. **Make changes** to code
2. **Test locally** with `uvicorn app.main:app --reload`
3. **Commit changes** with `git add . && git commit -m "Your message"`
4. **Deploy to Heroku** with `git push heroku main`

</details>

## 📁 Project Structure

```
your-hackathon-app/
├── app/
│   ├── main.py           # FastAPI application
│   ├── config.py         # Settings and environment variables
│   ├── database.py       # Database connection
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API endpoints
│   ├── schemas/          # Pydantic validation
│   ├── templates/        # HTML templates
│   └── static/           # CSS, JS, images
├── migrations/           # Database migration files
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku process configuration
├── .python-version      # Python version specification
└── app.json             # Heroku app configuration
```

## 🔧 Customizing for Your Hackathon

### 1. Update Models
Edit `app/models/user.py` for your data structure:
```python
class YourModel(Base):
    __tablename__ = "your_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Add your fields here
```

### 2. Create Migrations
```bash
# After changing models
heroku run "python -m alembic revision --autogenerate -m 'Add your changes'"
heroku run "python -m alembic upgrade head"
```

### 3. Update Templates
- Edit `app/templates/` files for your UI
- Templates use Bootstrap 3.4.1 classes
- HTMX included for dynamic interactions

## 💰 Costs

**Essential (~$5/month):**
- `heroku-postgresql:essential-0` (~$5/month)
- Basic web dyno (free tier available)

**Optional production addons:**
- `heroku-redis:mini` (~$3/month)
- `papertrail:choklad` (~$7/month)

## 🎓 What's Included

### Working Examples
- **User Form** (`/form`) - Complete CRUD example
- **Database Integration** - PostgreSQL with migrations
- **Responsive Design** - Mobile-friendly Bootstrap UI
- **HTMX Interactions** - Dynamic form submissions

### Technology Stack
- **Backend:** FastAPI (Python 3.11)
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Migrations:** Alembic for schema management
- **Frontend:** Bootstrap + HTMX
- **Deployment:** Heroku-optimized configuration

## 🤝 Hackathon Tips

1. **Deploy immediately** to verify everything works
2. **Keep the user form** as a reference for your models
3. **Use Bootstrap classes** for consistent styling
4. **Leverage HTMX** for dynamic interactions without JavaScript
5. **Changes deploy in ~2 minutes** - iterate quickly!

## 🔒 Security Notes

- Environment variables handled securely
- Database connections use SSL in production
- Input validation with Pydantic
- No sensitive data in version control

**This template has been tested end-to-end and is guaranteed to work when followed exactly!** 🎯

Good luck with your hackathon! 🏆


# How This App Works

This is a FastAPI-based web application designed as a ready-to-deploy template for hackathons. Here's how it works:

🏗️ Application Architecture

Backend Framework: FastAPI (Python 3.11)
•  Modern, fast web framework with automatic API documentation
•  Built-in data validation with Pydantic
•  Async support for high performance

Database Layer:
•  PostgreSQL for data storage
•  SQLAlchemy ORM for database interactions
•  Alembic for database migrations
•  Models defined in app/models/user.py with User table (id, email, address, comments)

Frontend:
•  Jinja2 templates for server-side rendering
•  Bootstrap 3.4.1 for responsive UI styling
•  HTMX for dynamic interactions without writing JavaScript
•  Templates in app/templates/ (base.html, index.html, form.html)

🔄 Data Flow

1. User visits the homepage (/) → Shows feature overview and "Start Building" button
2. User clicks to /form → Displays a demo form with email, address, and comments fields
3. Form submission → HTMX sends AJAX POST to /submit endpoint
4. Backend processing:
•  FastAPI validates form data using Pydantic schemas
•  SQLAlchemy creates new User record in PostgreSQL
•  Success message returned and displayed dynamically
5. Database persistence → All form data stored in users table

📁 Project Structure
🚀 Deployment Ready

Heroku Configuration:
•  Procfile defines web server: uvicorn app.main:app --host=0.0.0.0 --port=${PORT}
•  app.json configures PostgreSQL addon and environment variables
•  Automatic database migrations on deploy: python -m alembic upgrade head

Key Features:
•  ✅ Production-ready FastAPI setup
•  ✅ Working database integration with migrations
•  ✅ Form validation and error handling
•  ✅ Responsive Bootstrap UI
•  ✅ HTMX for dynamic user interactions
•  ✅ No Rust dependencies (deployment-friendly)

💡 Perfect For
•  Hackathons: Get a full-stack app running in 5 minutes
•  Prototypes: Complete foundation ready to customize
•  Learning: Modern Python web development patterns

The app demonstrates a complete data flow from HTML form → FastAPI backend → PostgreSQL database, making it an excellent starting point for building web applications quickly.