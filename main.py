
import asyncio
import httpx
import json
from bs4 import BeautifulSoup


async def fetch_urls(client, url):
    response = await client.get(url)
    return response.text

async def main():
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_urls(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
    for html_content in results:
        soup = BeautifulSoup(html_content, 'html.parser')
        if soup.a:
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                print(f"Link Title: {link.text}. Href: {href}")


    

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())