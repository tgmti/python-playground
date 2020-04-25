from fastapi import APIRouter

router = APIRouter()

db_Fake = [
        {"code": "12346", "name": "tasks 1", "date": "parse-date"},
        {"code": "12345", "name": "tasks 2", "date": "parse-date"},
    ]

@router.get("/tasks/", tags=["tasks"])
async def get_all():
    return db_Fake

@router.get("/tasks/{code}", tags=["tasks"])
async def get_one(code: str):
    return {"code": code, "name": "tasks {code}", "date": "parse-date"}

