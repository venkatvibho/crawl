# file: eci_contesting_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
import math
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import re
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")  # or "--headless" depending on chrome
        chrome_options.add_argument("--disable-gpu")
    # common options to avoid detection and speed
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    # optional: set user agent
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.set_page_load_timeout(30)
    return driver

from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
import re

if __name__ == "__main__":

    driver = make_driver()
    all_data = []

    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "-GOA"

    indiastates = [
        # {"name": "GOA", "url": "https://www.indiavotes.com/vidhan-sabha/goa/"},
        # {"name": "ANDHRA PRADESH", "url": "https://www.indiavotes.com/vidhan-sabha/andhra-pradesh/"},
        # {"name": "ARUNACHAL PRADESH", "url": "https://www.indiavotes.com/vidhan-sabha/arunachal-pradesh/"},
        # {"name": "ASSAM", "url": "https://www.indiavotes.com/vidhan-sabha/assam/"},
        # {"name": "BIHAR", "url": "https://www.indiavotes.com/vidhan-sabha/bihar/"},
        # {"name": "CHHATTISGARH", "url": "https://www.indiavotes.com/vidhan-sabha/chhattisgarh/"},
        # {"name": "KARNATAKA", "url": "https://www.indiavotes.com/vidhan-sabha/karnataka/"},
        # {"name": "KERALA", "url": "https://www.indiavotes.com/vidhan-sabha/kerala/"},
        # {"name": "TAMIL NADU", "url": "https://www.indiavotes.com/vidhan-sabha/tamil-nadu/"},
        # {"name": "TELANGANA", "url": "https://www.indiavotes.com/vidhan-sabha/telangana/"},
        # {"name": "MAHARASHTRA", "url": "https://www.indiavotes.com/vidhan-sabha/maharashtra/"},
        # {"name": "DELHI", "url": "https://www.indiavotes.com/vidhan-sabha/delhi/"},
        # {"name": "GUJARAT", "url": "https://www.indiavotes.com/vidhan-sabha/gujarat/"},
        # {"name": "HARYANA", "url": "https://www.indiavotes.com/vidhan-sabha/haryana/"},
        # {"name": "HIMACHAL PRADESH", "url": "https://www.indiavotes.com/vidhan-sabha/himachal-pradesh/"},
        # {"name": "JAMMU & KASHMIR", "url": "https://www.indiavotes.com/vidhan-sabha/jammu-kashmir/"},
        # {"name": "JHARKHAND", "url": "https://www.indiavotes.com/vidhan-sabha/jharkhand/"},
        # {"name": "MADHYA PRADESH", "url": "https://www.indiavotes.com/vidhan-sabha/madhya-pradesh/"},
        # {"name": "MANIPUR", "url": "https://www.indiavotes.com/vidhan-sabha/manipur/"},
        # {"name": "MEGHALAYA", "url": "https://www.indiavotes.com/vidhan-sabha/meghalaya/"},
        # {"name": "MIZORAM", "url": "https://www.indiavotes.com/vidhan-sabha/mizoram/"},
        # {"name": "NAGALAND", "url": "https://www.indiavotes.com/vidhan-sabha/nagaland/"},
        # {"name": "ODISHA", "url": "https://www.indiavotes.com/vidhan-sabha/orissa/"},
        # {"name": "PUDUCHERRY", "url": "https://www.indiavotes.com/vidhan-sabha/pondicherry/"},
        # {"name": "PUNJAB", "url": "https://www.indiavotes.com/vidhan-sabha/punjab/"},
        # {"name": "RAJASTHAN", "url": "https://www.indiavotes.com/vidhan-sabha/rajasthan/"},
        # {"name": "SIKKIM", "url": "https://www.indiavotes.com/vidhan-sabha/sikkim/"},
        # {"name": "TRIPURA", "url": "https://www.indiavotes.com/vidhan-sabha/tripura/"},
        # {"name": "UTTAR PRADESH", "url": "https://www.indiavotes.com/vidhan-sabha/uttar-pradesh/"},
        # {"name": "UTTARAKHAND", "url": "https://www.indiavotes.com/vidhan-sabha/uttarakhand/"},
        {"name": "WEST BENGAL", "url": "https://www.indiavotes.com/vidhan-sabha/west-bengal/"},
    ]
    # indiastates = [
    #     {"name": "Goa Daman And Diu", "url": "https://www.indiavotes.com/vidhan-sabha/goa-daman-and-diu/"}
    # ]
    for indst in indiastates:
        indststate_name = indst["name"]
        driver.get(indst["url"])
        print(indststate_name, indst["url"])

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract all state links first
        state_links = soup.find_all(
            "a",
            class_=lambda c: c and "rounded-lg" in c and "text-sm" in c
        )

        states = []

        tbody = soup.find("tbody")

        for row in tbody.find_all("tr", class_="row-link"):
            cols = row.find_all("td")
            print("================================================================")
            year = cols[0].get_text(strip=True)
            winning_party = cols[1].find("span", class_="font-semibold").get_text(strip=True)
            total_seats = cols[2].get_text(strip=True)
            turnout = cols[3].get_text(strip=True)
            print(year)
            url = cols[0].find("a")["href"]
            try:
                year = int(year)
                # if year >= 2000:
                if year in [2016,2011,2006,2001]:
                    states.append({
                        "year": year,
                        "url": url,
                        "winning_party": winning_party,
                        "total_seats": total_seats,
                        "turnout": turnout,
                        "state_name":indststate_name
                    })
            except ValueError:
                pass
        print(states)
        print("Total Years Found:", len(states))
        for state in states:

            state_name = state["state_name"]
            state_url = state["url"]
            year = state["year"]

            current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            os.makedirs(state_name, exist_ok=True)
            file_name = os.path.join(
                state_name,
                f"{state_name}_{current_date}_{year}.xlsx"
            )

            all_data = []          # Reset for this state
            constituencies = []    # Reset for this state

            # -------------------------
            # Get Constituencies
            # -------------------------
            driver.get(f"https://www.indiavotes.com{state_url}")
            time.sleep(3)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            section = soup.find("h2", string=lambda s: s and "Constituencies" in s)

            if section:
                grid = section.find_next("div")

                for a in grid.find_all("a", href=True):
                    constituencies.append({
                        "name": a.find("span").get_text(strip=True),
                        "url": a["href"]
                    })

            print(constituencies)
            print("Total Constituencies Found:", len(constituencies))
            # -------------------------
            # Process Constituencies
            # -------------------------
            for constituency in constituencies:

                driver.get(f"https://www.indiavotes.com{constituency['url']}")
                time.sleep(2)

                soup = BeautifulSoup(driver.page_source, "html.parser")

                tbody = soup.find("tbody")

                if not tbody:
                    continue
                # print(tbody)
                for tr in tbody.find_all("tr")[:1]:

                    if not tr.select_one("span.ml-2.pill.pill-accent.text-2xs"):
                        continue

                    tds = tr.find_all("td")

                    if len(tds) < 4:
                        continue

                    print(tds)
                    # Candidate
                    candidate_td = tds[1]

                    # Name
                    name_span = candidate_td.find("span", class_="font-medium")
                    name = name_span.get_text(strip=True) if name_span else ""

                    # Winner status
                    winner_span = candidate_td.find("span", class_="pill")
                    winner = winner_span.get_text(strip=True) if winner_span else ""

                    # Gender
                    gender_div = candidate_td.find("div", class_="text-xs text-muted")
                    gender = gender_div.get_text(strip=True) if gender_div else ""


                    # Party
                    party_link = tds[2].find("a")

                    if party_link:
                        party = party_link.get_text(strip=True)
                    else:
                        party = tds[2].get_text(" ", strip=True)

                    # Vote share
                    vote_share = tds[3].get_text(" ", strip=True)


                    # Margin remove "vs PARTY"
                    margin_text = tds[4].get_text(" ", strip=True)

                    margin = re.sub(
                        r'\s+vs\s+.*$',
                        '',
                        margin_text
                    )

                    all_data.append([
                        state_name,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        constituency["name"],
                        "",
                        name,
                        "",
                        party,
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        gender,
                        vote_share,
                        margin
                    ])

            # -------------------------
            # Create Excel FOR THIS STATE
            # -------------------------
            wb = Workbook()
            ws = wb.active

            ws.append([
                    "STATE NAME(ENGLISH)",
                    "STATE NAME(LOCAL LANGUAGE)",
                    "REGION CODE",
                    "REGION NAME(ENGLISH)",
                    "REGION NAME(LOCAL LANGUAGE)",
                    "DISTRICT CODE",
                    "DISTRICT NAME(ENGLISH)",
                    "DISTRICT NAME(LOCAL LANGUAGE)",
                    "LOKSABHA CODE",
                    "LOKSABHA NAME(ENGLISH)",
                    "LOKSABHA NAME(LOCAL LANGUAGE)",
                    "ASSEMBLY CODE",
                    "ASSEMBLY NAME(ENGLISH)",
                    "ASSEMBLY NAME(LOCAL LANGUAGE)",
                    "CANDIDATE NAME(ENGLISH)",
                    "CANDIDATE NAME(LOCAL LANGUAGE)",
                    "PARTY SHORT NAME(ENGLISH)",
                    "PARTY SHORT NAME(LOCAL LANGUAGE)",
                    "PARTY FULL NAME(ENGLISH)",
                    "PARTY FULL NAME(LOCAL LANGUAGE)",
                    "IS VIP(YES/NO)",
                    "CANDIDATE PHOTO",
                    "PHASE NUMBER",
                    "CANDIDATE DATABASE ID",
                    "GENDER",
                    "VOTES",
                    "SHARE"
                ])
            for sno, row in enumerate(all_data, start=1):
                row[11] = sno          # ASSEMBLY CODE column
                ws.append(row)

            wb.save(file_name)

            print(f"{state_name} -> {file_name}")