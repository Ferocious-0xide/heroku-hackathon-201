from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import user

app = FastAPI(title="Heroku Hackathon")
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(user.router)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
