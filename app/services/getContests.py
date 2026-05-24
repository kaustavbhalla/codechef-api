import httpx
import asyncio
from app.models.contests import ContestListResponse

CONTESTS_API = "https://www.codechef.com/api/list/contests/all"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Referer": "https://www.codechef.com/contests",
}

async def fetchContests(mode: str = "all") -> ContestListResponse:
    params = {
        "sort_by": "START",
        "sorting_order": "asc",
        "offset": 0,
        "mode": mode
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get(CONTESTS_API, params=params, headers=HEADERS)
        resp.raise_for_status()
        return ContestListResponse.model_validate(resp.json())

async def main():
    ret = await fetchContests()
    print(ret)

if __name__ == "__main__":
    asyncio.run(main())
