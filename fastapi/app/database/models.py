'''
    My Tasks API - FastAPI Tests

    SQLAlchemy ORM Models
'''

# Standard Imports

# PyPi Imports
from sqlalchemy import (
    ForeignKey,
    Boolean,
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.orm import relationship

# Local Imports
from .setup import Base

# ORM Classes

class Projects(Base):

    __tablename__ = "projects"

    sqlite_autoincrement=True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    project_super_id = Column(Integer, ForeignKey("projects.id"))

    project_super = relationship("Projects", remote_side=[id])
    # sub_projects = relationship("Projects", back_populates="project_super")

    # tasks = relationship("Tasks", back_populates="project")


class Tasks(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)
    open_date = Column(DateTime)
    done_date = Column(DateTime)

    project_id = Column(Integer, ForeignKey("projects.id"))

    # project = relationship("Projects", back_populates="tasks")
    schedules = relationship("Schedules", back_populates="task")
    activities = relationship("Activities", back_populates="task")


class Schedules(Base):

    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime)
    updated = Column(DateTime)
    scheduled = Column(DateTime)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Tasks", back_populates="schedules")


class Activities(Base):

    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime)
    updated = Column(DateTime)
    text = Column(String)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Tasks", back_populates="activities")

