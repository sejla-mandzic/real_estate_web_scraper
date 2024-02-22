import re
import os

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

from common.Estate import Estate
from common.config import CANTONS, CITIES


def scrape_apartment(page, line: str):
    id = int(line)

    page.goto(f"https://olx.ba/artikal/{id}")
    page.wait_for_load_state("load")

    content = page.content()

    soup = BeautifulSoup(content, "html.parser")

    price_element = soup.find("span", {"class": "price-heading"})
    price_text = price_element.get_text(strip=True)
    groups = re.match("([0-9]+)\.([0.9]+) KM", price_text)
    price = None
    if groups:
        price_string = groups.group(1) + groups.group(2)
        price = int(price_string)

    label_div = soup.find("div", {"class": "border-gray-200"})
    label_elements = label_div.find_all("label", {"class": "btn-pill"})
    labels = label_elements[:2]
    city = labels[0].get_text(strip=True)  # city
    state_text = labels[1].get_text(strip=True)
    state = (
        state_text
        if state_text.lower() == "novo" or state_text.lower() == "korišteno"
        else None
    )  # state
    if state:
        state = state.replace("Č", "C").replace("Ć", "C").replace("Ž", "Z").replace("Š", "S").replace("č", "c").replace("ć", "c").replace("ž", "z").replace("š", "s")

    category = "Apartment"
    for canton_cities in CITIES:
        if city in canton_cities["cities"]:
            canton = CANTONS[canton_cities["id"] - 1]
            break
    city = city.replace("Č", "C").replace("Ć", "C").replace("Ž", "Z").replace("Š", "S").replace("č", "c").replace("ć", "c").replace("ž", "z").replace("š", "s")

    apartment_attributes = soup.find("div", {"class": "required-attributes"})
    attrs_apartment = apartment_attributes.find_all("div", {"class": "required-wrap"})
    main_attrs = attrs_apartment[2:]
    area = None
    for attr in main_attrs:
        tds = [text.get_text(strip=True) for text in attr.find_all("td")]
        if len(tds) > 0 and tds[0] == "Kvadrata":
            area = float(tds[1])

    table = soup.find("table", {"class": "w-full"})
    trs = table.find_all("tr")

    terrace = False
    parking = False
    electricity = False
    water = False
    internet = False
    basement = False
    post_date = None
    build_period = None
    floor_type = None
    terrace_area = None
    cable_tv = False
    pantry = False
    phone_line = False
    bathrooms_num = None
    heating_type = None

    for tr in trs:
        tds = tr.find_all("td")
        if tds[1].find("div"):  # bools
            if tds[0].get_text(strip=True).lower() == "balkon":
                terrace = True
            elif tds[0].get_text(strip=True).lower() == "parking":
                parking = True
            elif tds[0].get_text(strip=True).lower() == "struja":
                electricity = True
            elif tds[0].get_text(strip=True).lower() == "voda":
                water = True
            elif tds[0].get_text(strip=True).lower() == "internet":
                internet = True
            elif tds[0].get_text(strip=True).lower() == "podrum/tavan":
                basement = True
            elif tds[0].get_text(strip=True).lower() == "kablovska tv":
                cable_tv = True
            elif tds[0].get_text(strip=True).lower() == "ostava/špajz":
                pantry = True
            elif tds[0].get_text(strip=True).lower() == "telefonski priključak":
                phone_line = True
        else:
            if tds[0].get_text(strip=True).lower() == "datum objave":
                post_date = tds[1].get_text(strip=True)
            elif tds[0].get_text(strip=True).lower() == "godina izgradnje":
                build_period = tds[1].get_text(strip=True)
            elif tds[0].get_text(strip=True).lower() == "vrsta poda":
                floor_type = tds[1].get_text(strip=True)
                floor_type = floor_type.replace("Č", "C").replace("Ć", "C").replace("Ž", "Z").replace("Š", "S").replace("č", "c").replace("ć", "c").replace("ž", "z").replace("š", "s")
            elif tds[0].get_text(strip=True).lower() == "kvadratura balkona":
                terrace_area = float(tds[1].get_text(strip=True))
            elif tds[0].get_text(strip=True).lower() == "broj kupatila":
                bathrooms_num = int(tds[1].get_text(strip=True))
            elif tds[0].get_text(strip=True).lower() == "vrsta grijanja":
                heating_type = tds[1].get_text(strip=True)
                heating_type = heating_type.replace("Č", "C").replace("Ć", "C").replace("Ž", "Z").replace("Š", "S").replace("č", "c").replace("ć", "c").replace("ž", "z").replace("š", "s")

    estate = Estate(
        id,
        category,
        price,
        canton,
        city,
        state,
        area,
        terrace,
        parking,
        electricity,
        water,
        internet,
        basement,
        post_date,
        build_period,
        floor_type,
        terrace_area,
        cable_tv,
        pantry,
        phone_line,
        bathrooms_num,
        heating_type,
    )

    print(f"Processed item: {id}")
    return estate.to_csv_row()


def scrape_apartments():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "apartments.txt"), "r")
        lines = file.readlines()
        file.close()

        apartments = []

        for i, line in enumerate(lines):
            try:
                apartment = scrape_apartment(page, line.strip())
                print(apartment)
                apartments.append(apartment)
            except Exception as exc:
                print(exc)

            if i % 100 == 0:
                context.close()
                context = browser.new_context()
                page = context.new_page()

        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "apartments.csv"), "w") as csv_file:
            csv_file.write(
                "id,category,price,canton,city,state,area,terrace,parking,electricity,water,internet,basement,post_date,build_period,floor_type,terrace_area,cable_tv,pantry,phone_line,bathrooms_num,heating_type\n"
            )
            csv_file.writelines(apartments)

        browser.close


if __name__ == "__main__":
    scrape_apartments()
