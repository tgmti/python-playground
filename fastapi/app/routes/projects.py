# Standard Imports
from typing import List

# PyPi Imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Local Imports
from ..data_schemas import schemas
from ..controllers import projects
from ..utils.main_utils import get_db

###############################################################################
router = APIRouter()

@router.get("/projects/", tags=["projects"], response_model=List[schemas.Project])
async def get_all(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return projects.get_projects(db=db, skip=skip, limit=limit)


@router.get("/projects/{id}", tags=["projects"], response_model=schemas.Project)
async def get_one(
    id: int,
    db: Session = Depends(get_db)
):
    return projects.get_project_by_id(db=db, id=id)

@router.post("/projects/", tags=["projects"], response_model=schemas.Project)
async def add(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db)
):
    return projects.add_project(db=db, project=project)