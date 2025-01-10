# Heroku Hackathon 201 🚀

An advanced FastAPI template with scaling options, database migrations, and production-ready features.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## What's Different in 201? 📚
Heads up, there are real costs associated with this template. If you decidee to build with this template, please be aware of the costs.

This template builds on the basic version with several advanced features:

### 1. Scaling Options 📈
- Multiple dyno configurations for different environments
- Automatic scaling based on traffic patterns
- Worker processes for background tasks
- Script to manage and estimate costs of different configurations

### 2. Database Migrations with Alembic 🔄
- Structured database schema management
- Version control for database changes
- Safe production updates
- Automatic migration running on deployment

### 3. Production Add-ons 🛠️
- Redis for caching and session management
- Papertrail for advanced logging
- Multiple PostgreSQL configurations

### 4. Environment Management 🌍
- Separate configurations for review/staging/production
- Environment-specific scaling
- Secure secrets management

## Quick Deploy Options 🚀

### Minimal Setup (Development/Testing)
```bash
heroku create my-app
heroku addons:create heroku-postgresql:essential-0
git push heroku main
```

### Production Setup
```bash
# Create app with production dynos
./scripts/dyno_manager.py my-app --scale business

# Add production add-ons
heroku addons:create heroku-redis:premium-0
heroku addons:create papertrail:choklad
```

## Database Migrations 📦

Initialize migrations:
```bash
# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Run migrations
alembic upgrade head
```

Create a new migration:
```bash
alembic revision --autogenerate -m "Add user table"
```

## Scaling Guide 📊

This template includes different scaling configurations:

### Minimal 
- 1 web dyno (basic)
- 1 worker dyno (basic)
- Suitable for development/testing

### Starter 
- 2 web dynos (standard-1x)
- 1 worker dyno (standard-1x)
- Good for small production apps

### Business 
- 4 web dynos (standard-2x)
- 2 worker dynos (standard-2x)
- Suitable for medium traffic


### Enterprise 
- 6 web dynos (performance-m)
- 3 worker dynos (performance-m)
- High-traffic applications

Use the dyno manager to apply configurations:
```bash
python scripts/dyno_manager.py my-app --scale business --estimate
```

## Add-ons Usage Guide 🔌

### Redis Configuration
```python
from app.cache import redis_client

# Session management
redis_client.set_session(user_id, session_data)

# Cache expensive operations
@redis_client.cache(ttl=3600)
def expensive_operation():
    pass
```

### Logging with Papertrail
```python
import logging
logger = logging.getLogger(__name__)

# Structured logging
logger.info("User action", extra={
    "user_id": user.id,
    "action": "purchase",
    "amount": amount
})
```

## Environment Variables 🔐

Key variables to configure:

```bash
# Core Settings
ENVIRONMENT=production
WORKER_CONCURRENCY=3
LOG_LEVEL=INFO

# Redis Configuration
REDIS_MAX_CONNECTIONS=10
REDIS_URL=redis://...

# Database
DATABASE_URL=postgresql://...
```

## Local Development 💻

1. Set up Python environment:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up databases:
```bash
createdb heroku_hackathon_201
docker run -d -p 6379:6379 redis
```

4. Run migrations:
```bash
alembic upgrade head
```

5. Start the application:
```bash
uvicorn app.main:app --reload
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Run tests: `pytest`
4. Submit a pull request

## Security Considerations 🔒

- All secrets are managed through environment variables
- Redis connections are limited and pooled
- Database connections use SSL in production
- Worker processes are isolated
- Logging excludes