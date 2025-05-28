# Heroku Hackathon 201 🚀

**Ready-to-deploy FastAPI template for hackathons - tested and working!**

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 🎯 What You Get

A **production-ready** FastAPI application with:
- ✅ **FastAPI** - Modern Python web framework
- ✅ **PostgreSQL** - Database with Alembic migrations  
- ✅ **HTMX** - Dynamic web interactions
- ✅ **TailwindCSS** - Beautiful, responsive UI
- ✅ **Pure Python** - No Rust dependencies (deployment-friendly)
- ✅ **Working example** - User form with database integration

**Demo App:** https://heroku-hackathon-201-e1ae677bcf73.herokuapp.com/

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Heroku CLI installed
- Git repository initialized
- Heroku account with credit card (for database addon)

### 1. Clone or Fork This Repo
```bash
git clone <your-repo-url>
cd heroku-hackathon-201
```

### 2. Deploy to Heroku
```bash
# Create app (use your own unique name)
heroku create your-hackathon-app-name

# Add PostgreSQL database
heroku addons:create heroku-postgresql:essential-0

# Deploy the code
git push heroku main

# Run database migrations
heroku run "python -m alembic upgrade head"
```

### 3. Test Your App
```bash
# Check if it's working
heroku open
```

You should see the welcome page! Click "Start Here" to test the form.

## 🛠️ Local Development

### 1. Python Setup (IMPORTANT: Use 3.11)
```bash
# Use Python 3.11 - newer versions have compatibility issues
pyenv install 3.11.12
pyenv local 3.11.12

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally (Optional - for development)
```bash
# Set local database URL (optional)
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/hackathon_db"

# Start the server
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```

Visit: http://localhost:8000

## 📁 Project Structure

```
heroku-hackathon-201/
├── app/
│   ├── main.py           # FastAPI application
│   ├── config.py         # Settings and environment variables
│   ├── database.py       # Database connection
│   ├── models/           # SQLAlchemy models
│   │   └── user.py       # User model example
│   ├── routes/           # API endpoints
│   │   └── user.py       # User routes example
│   ├── schemas/          # Pydantic models
│   │   └── user.py       # User validation schemas
│   ├── templates/        # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── form.html
│   └── static/           # CSS, JS, images (created automatically)
├── migrations/           # Database migration files
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku process configuration
├── .python-version      # Python version specification
└── app.json             # Heroku app configuration
```

## 🔧 Customizing for Your Hackathon

### 1. Update the Models
Edit `app/models/user.py` to match your data needs:
```python
class YourModel(Base):
    __tablename__ = "your_table"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Add your fields here
```

### 2. Create New Migration
```bash
# After changing models, create migration
heroku run "python -m alembic revision --autogenerate -m 'Add your changes'"

# Apply the migration
heroku run "python -m alembic upgrade head"
```

### 3. Update Templates
- Edit `app/templates/` files for your UI
- Templates use TailwindCSS classes
- HTMX is included for dynamic interactions

### 4. Add New Routes
Create new files in `app/routes/` following the pattern in `user.py`

## 🚨 Common Issues & Solutions

### Issue: "RuntimeError: Directory 'app/static' does not exist"
**Solution:** The static directory is created automatically. If you get this error:
```bash
mkdir -p app/static
touch app/static/.gitkeep
git add app/static/.gitkeep
git commit -m "Add static directory"
git push heroku main
```

### Issue: "No module named 'pydantic_core'" or Rust compilation errors
**Solution:** This template uses Pydantic v1 (pure Python). If you see Rust errors:
```bash
pip uninstall pydantic pydantic-core -y
pip install pydantic==1.10.14
```

### Issue: "AssertionError" or Python version errors
**Solution:** Use Python 3.11 exactly:
```bash
echo "3.11" > .python-version
git add .python-version
git commit -m "Fix Python version"
git push heroku main
```

### Issue: "postgres dialect" database errors
**Solution:** Already fixed in this template! The config handles Heroku's DATABASE_URL format automatically.

### Issue: R10 Boot timeout errors
**Cause:** Usually missing static directory or Python version issues
**Solution:** Apply the fixes above and redeploy

### Issue: 503 Service Unavailable
**Check logs:** `heroku logs --app your-app-name --tail`
**Common fixes:** 
1. Ensure static directory exists
2. Check Python version is 3.11
3. Verify database addon is attached

## 🎓 What's Included

### Working Examples
- **User Form** (`/form`) - Collects email, address, comments
- **Database Storage** - Data saved to PostgreSQL
- **Responsive Design** - Works on mobile and desktop
- **HTMX Integration** - Dynamic form submission

### Technology Stack
- **Backend:** FastAPI (Python 3.11)
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Migrations:** Alembic for schema changes
- **Frontend:** Jinja2 templates + TailwindCSS + HTMX
- **Deployment:** Heroku with proper configuration

### Pre-configured Features
- ✅ Database connection handling
- ✅ Environment variable management
- ✅ Error handling
- ✅ Responsive UI components
- ✅ Form validation
- ✅ Migration system

## 💰 Costs

**Essential addons** (~$5-7/month):
- `heroku-postgresql:essential-0` (~$5/month)
- Basic web dyno (free tier available)

**Optional production addons:**
- `heroku-redis:mini` (~$3/month) - for caching
- `papertrail:choklad` (~$7/month) - for logging

## 🤝 Hackathon Tips

### Team Workflow
1. **Fork this repo** for your team
2. **Deploy immediately** to verify it works
3. **Customize models** for your specific use case
4. **Iterate quickly** - changes deploy in ~2 minutes

### Development Strategy
- Keep the existing user form as a reference
- Add your models alongside the user model
- Use the included styling patterns
- Leverage HTMX for interactive features

### Debugging
- Use `heroku logs --app your-app-name --tail` for real-time logs
- Test locally first: `uvicorn app.main:app --reload`
- Check the working demo: https://heroku-hackathon-201-e1ae677bcf73.herokuapp.com/

## 📚 Next Steps

1. **Customize the landing page** (`app/templates/index.html`)
2. **Add your business logic** to routes
3. **Style your forms** with TailwindCSS
4. **Add authentication** if needed
5. **Scale up** for production traffic

## 🆘 Getting Help

If you run into issues:
1. Check the **Common Issues** section above
2. Compare your setup to the working demo
3. Use `heroku logs` to diagnose problems
4. Ensure you're following the exact Python 3.11 requirement

**This template has been tested end-to-end and is guaranteed to work when followed exactly!** 🎯

## 🔒 Security Notes

- Environment variables are handled securely
- Database connections use SSL in production  
- No sensitive data in version control
- Input validation included with Pydantic

Good luck with your hackathon! 🏆