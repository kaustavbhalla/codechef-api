from fastapi import APIRouter, HTTPException
from app.services.getContests import fetchContests
from app.models.contests import Contest

router = APIRouter()

@router.get("/")
async def getAllContests():
    data = await fetchContests()
    return {
        "present": data.present_contests,
        "upcoming": data.future_contests,
        "past": data.past_contests
    }

@router.get("/present")
async def getPresentContests():
    data = await fetchContests()
    return {
        "contests": data.present_contests,
        "count": len(data.present_contests)
    }

@router.get("/upcoming")
async def getUpcomingContests():
    data = await fetchContests()
    return {
        "contests": data.present_contests,
        "count": len(data.present_contests)
    }

@router.get("/past")
async def getPastContests():
    data = await fetchContests()
    return {
        "contests": data.present_contests,
        "count": len(data.present_contests)
    }

@router.get("/{code}")
async def getContestByCode(code: str):
    data = await fetchContests()
    allContests = (data.present_contests + data.past_contests + data.future_contests)

    match = next((c for c in allContests if c.contest_code == code), None)
    if not match:
        raise HTTPException(status_code=404, detail=f"Contest {code} not found")

    return match


