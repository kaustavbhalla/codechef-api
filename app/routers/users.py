from fastapi import APIRouter, HTTPException
from app.models.users import User
from app.services.getUsers import getUserDataInHTML, parseHTMLAndExtractData
from pydantic import ValidationError

router = APIRouter()

@router.get("/users/{username}", response_model=User)
async def getUserbyUserName(username: str):
    try:
        html = await getUserDataInHTML(username=username)
        return parseHTMLAndExtractData(html, username)
    except ValidationError as e:
        raise HTTPException(status_code=502, detail=f"Upstream data changed, parsing failed - {e}")
    except Exception as e:
        import traceback
        raise HTTPException(status_code=500, detail=traceback.format_exc())
