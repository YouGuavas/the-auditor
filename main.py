
import asyncio
import argparse
from bs4 import BeautifulSoup


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    args = parser.parse_args()
    url = args.url
    print(url)
    

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())