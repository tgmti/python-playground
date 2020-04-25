from fastapi import APIRouter

router = APIRouter()

db_Fake = [
        {"code": "12346", "name": "schedules 1", "date": "parse-date"},
        {"code": "12345", "name": "schedules 2", "date": "parse-date"},
    ]

@router.get("/schedules/", tags=["schedules"])
async def get_all():
    return db_Fake

@router.get("/schedules/{code}", tags=["schedules"])
async def get_one(code: str):
    return {"code": code, "name": "schedules {code}", "date": "parse-date"}

