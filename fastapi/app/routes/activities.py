from fastapi import APIRouter

router = APIRouter()

db_Fake = [
        {"code": "12346", "resume": "text in activity 1", "date": "parse-date"},
        {"code": "12345", "resume": "text in activity 2", "date": "parse-date"},
    ]

@router.get("/activities/", tags=["activities"])
async def get_all():
    return db_Fake

@router.get("/activities/{code}", tags=["activities"])
async def get_one(code: str):
    return {"code": code, "resume": "text in activity 2", "date": "parse-date"}

