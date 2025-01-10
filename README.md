# Heroku Hackathon

A FastAPI and HTMX project template ready for Heroku deployment.

## Local Development Setup

1. Set up Python environment:
```bash
# Install pyenv if not already installed
curl https://pyenv.run | bash

# Install and set Python version
pyenv install 3.11.5
pyenv local 3.11.5

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up PostgreSQL:
```bash
createdb heroku_hackathon
```

4. Set environment variables:
```bash
echo "DATABASE_URL=postgresql://postgres:postgres@localhost:5432/heroku_hackathon" > .env
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## Heroku Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL:
```bash
heroku addons:create heroku-postgresql:mini
```

4. Deploy:
```bash
git push heroku main
```

Visit your app at the URL provided by Heroku!
