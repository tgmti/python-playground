# Standard Imports

# PyPi Imports
from sqlalchemy.orm import Session

# Local Imports
from ..database import models
from ..data_schemas import schemas

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Projects).offset(skip).limit(limit).all()

def get_project_by_id(db: Session, id: int):
    return db.query(models.Projects).filter(models.Projects.id == id).first()

def add_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Projects(name=project.name, project_super_id=project.project_super_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project