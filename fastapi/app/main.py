'''
    My Tasks API - FastAPI Tests

    Main Application
'''

# PyPi Imports
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

# Local Imports
from .database.setup import (
    session_local,
    engine
)

from .database import models as models

from .routes import projects, tasks, schedules, activities


# Database config
models.Base.metadata.create_all(bind=engine)

# App Config
app = FastAPI(
    title="My Tasks - FastAPI Tests",
    description="This is a demo application for FastAPI",
    version="0.0.1"
)

###############################################################################

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
	'''Function to populate requests with a database session'''
	response = Response("Internal server error", status_code=500)
	try:
		request.state.db = session_local()
		response = await call_next(request)
	finally:
		request.state.db.close()
	return response

###############################################################################

# App Routes
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(schedules.router)
app.include_router(activities.router)

