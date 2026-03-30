import httpx
import asyncio
from ..models.users import User
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

def parseHTMLAndExtractData(html: str, username: str):
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
    ratingFl = soup.select_one("div.rating-number").text.strip()
    
    #Calculating division


async def main():
    resp = await getUserDataInHTML("potato167")
    #print(resp)
    parseHTMLAndExtractData(resp, "potato167")

if __name__ == "__main__":
    asyncio.run(main())
