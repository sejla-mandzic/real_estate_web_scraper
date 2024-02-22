import time
import os

from playwright.sync_api import sync_playwright

from bs4 import BeautifulSoup
from common.config import HOUSES_MAPPING, HOUSES_URL, APARTMENTS_MAPPING, APARTMENTS_URL


def get_page_items_urls(url, page):
    try:
        page.goto(url)
        page.wait_for_load_state("load")

        content = page.content()

        soup = BeautifulSoup(content, "html.parser")
        links = soup.select("div.cardd a[href]")

        hrefs = [link["href"] for link in links]

        return hrefs
    except Exception as exc:
        print(f"Can't scrape page with url: {url}")
        return None


def scrape_content(page_url: str, mapping: list[any], real_estate: list[any]):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        for page_entry in mapping:
            canton = page_entry["canton"]
            print(f"Currently scraping canton: {canton}")
            urls = []
            for page_number in range(1, page_entry["pages"] + 1):
                url = f"{page_url}&canton={canton}&cities=&page={page_number}"
                urls_of_page = get_page_items_urls(url, page)
                if urls_of_page != None:
                    print(
                        f"Number of urls for page: {page_number} of canton: {canton} is: {len(urls_of_page)}"
                    )
                    urls.extend(urls_of_page)

            urls_of_canton = {"canton": canton, "urls": urls}
            real_estate.append(urls_of_canton)

        browser.close


if __name__ == "__main__":
    apartments = []
    houses = []
    
    start = time.time()
    scrape_content(page_url=APARTMENTS_URL, mapping=APARTMENTS_MAPPING, real_estate=apartments)
    duration = time.time() - start
    print(f"Apartments scraped in: {duration} seconds.")
    
    start = time.time()
    scrape_content(page_url=HOUSES_URL, mapping=HOUSES_MAPPING, real_estate=houses)
    duration = time.time() - start
    print(f"Houses scraped in: {duration} seconds.")

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "apartments.txt"), "w") as file:
        for apartment in apartments:
            for apartment_url in apartment["urls"]:
                file.write(f"{apartment['canton']},{apartment_url}\n")

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "houses.txt"), "w") as file:
        for house in houses:
            for house_url in house["urls"]:
                file.write(f"{house['canton']},{house_url}\n")
