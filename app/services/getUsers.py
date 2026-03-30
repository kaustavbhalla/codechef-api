import httpx
import asyncio
from ..models.users import User, typeOfUser
from bs4 import BeautifulSoup

async def getUserDataInHTML(username: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://www.codechef.com/users/{username}", headers=headers, follow_redirects=True)
        
        response.raise_for_status()

    return response.text

def parseHTMLAndExtractData(html: str, username: str) -> User:
    soup = BeautifulSoup(html, "lxml")
    
    #Getting users name
    nameFl = soup.select_one("div.breadcrumb")
    name = nameFl.get_text().split("»")[-1].strip()


    #Getting users country
    countryFl = soup.select_one("span.user-country-name").text.strip()

    #Getting users type & institution
    globalinstiFl = ""
    globaltypeFl = ""

    for li in soup.select("section.user-details ul.side-nav li"):
        label = li.select_one("label")
        
        if label and "Institution:" in label.text:
            instiFl = li.select_one("span:last-child").text.strip()
            globalinstiFl = instiFl
            
    

    for li in soup.select("section.user-details ul.side-nav li"):
        label = li.select_one("label")
        
        if label and "Student/Professional:" in label.text:
            typeFl = li.select_one("span:last-child").text.strip()
            globaltypeFl = typeFl

    
    #Getting user rating
    rating = soup.select_one("div.rating-number")
    ratingFl = int(rating.text.strip()) if rating else 0
    
    #Calculating division
    divFl = ""
    if ratingFl >= 2000:
        divFl = "Division 1"
    elif ratingFl < 2000 and ratingFl >= 1600:
        divFl = "Division 2"
    elif ratingFl < 1600 and ratingFl >= 1400:
        divFl = "Division 3"
    elif ratingFl < 1400:
        divFl = "Division 4"

    #calculating stars
    stars = soup.select_one("span.rating")
    stars_text = stars.text.strip() if stars else "0"
    starsFl = int(stars_text.replace("★", "").strip())

    ranks = {}
    for li in soup.select("div.rating-ranks ul.inline-list li"):
        value = li.select_one("strong").text.strip()
        text = li.get_text(strip=True)
        if "Global Rank" in text:
            ranks["global_rank"] = int(value)
        elif "Country Rank" in text:
            ranks["country_rank"] = int(value)

    globalRankFl = ranks.get("global_rank", None) 
    countryRankFl = ranks.get("country_rank", None)

    #contests participated
    noOfContests = soup.select_one("div.contest-participated-count b")
    noOfContestsFl = noOfContests.text.strip() if noOfContests else None
    print(noOfContestsFl)



    #final return

    return User(
        name=name,
        userName=username,
        country=countryFl,
        typeOf=typeOfUser(globaltypeFl) if globaltypeFl else typeOfUser.Other,
        institution=globalinstiFl,
        rating=ratingFl,
        division=divFl,
        stars=starsFl,
        globalRank=globalRankFl,
        countryRank=countryRankFl,
        contestsParticipated=noOfContestsFl
    )

async def main():
    resp = await getUserDataInHTML("potato167")
    #print(resp)
    parseHTMLAndExtractData(resp, "potato167")

if __name__ == "__main__":
    asyncio.run(main())
