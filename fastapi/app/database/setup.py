'''
    My Tasks API - FastAPI Tests

    Database setup
'''

# Standard Imports

# PyPi Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Local Imports


###############################################################################
#TODO: Change Config to production environment, view model on https://github.com/christopherthompson81/fastapi_demo/blob/master/database/setup.py
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
###############################################################################

engine = create_engine(SQLALCHEMY_DATABASE_URL) #pylint: disable=invalid-name

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine) #pylint: disable=invalid-name

Base = declarative_base() #pylint: disable=invalid-name
