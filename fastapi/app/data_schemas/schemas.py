from typing import List

from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str = None
    project_super_id: int


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class ProjectWithChilds(Project):
    project: Project
    childs: List[Project] = []
