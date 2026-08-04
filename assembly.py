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
import json

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
    #     {"name": "GOA", "url": "https://www.indiavotes.com/vidhan-sabha/goa/"}
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
            year = url = cols[0].find("a").get_text(strip=True)
            year = int(year)
            url = cols[0].find("a")["href"]
            try:
                # if year >= 2000:
                if year in [2001,2006,2011]:
                # if year == 2005 and url == "/vidhan-sabha/bihar/2005-oct/":
                    states.append({
                        "year": year,
                        "url": url
                    })
                    print(year)
            except ValueError:
                pass
        # print(states)
        print("Total Years Found:", len(states))
        for state in states:
            state_name = indststate_name
            state_url = state["url"]
            year = state["year"]
            current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            os.makedirs(state_name, exist_ok=True)
            file_name = os.path.join(
                state_name,
                f"{state_name}_{current_date}_{year}.xlsx"
            )
        
            wb = Workbook()
            ws = wb.active
            ws.append([
                "DISTRICT","LOKSABHA","YEAR-SUMMERY","JSONDATA"
            ])
            all_data = []          # Reset for this state
            constituencies = []    # Reset for this state

            # -------------------------
            # Get Constituencies
            # -------------------------
            print("Processing: 222222222", year, url)
            driver.get(f"https://www.indiavotes.com{state_url}")
            time.sleep(3)
            soup1 = BeautifulSoup(driver.page_source, "html.parser")
            tbody = soup1.find("table",id="iv-full-results").find("tbody")
            summary = {}
            for card in soup1.find_all("div", class_="card p-4"):
                label = card.find(
                    "div",
                    class_="text-xs uppercase tracking-wider text-muted mb-1"
                )

                value = card.find(
                    "div",
                    class_="text-2xl font-semibold num"
                )

                if label and value:
                    summary[
                        label.get_text(strip=True)
                    ] = value.get_text(strip=True)
            summary  = json.dumps(summary, ensure_ascii=False)
            # print(tbody)
            if not tbody:
                print("No table found:", state_name)
                continue
            for tr in tbody.find_all("tr"):
                first_td = tr.find("td")
                a = first_td.find("a")
                if a:
                    constituency = a.get_text(strip=True)
                    url = a["href"]
                    print("Processing: 33333", url)
                    driver.get(f"https://www.indiavotes.com{url}")
                    # driver.get("https://www.indiavotes.com/vidhan-sabha/goa/2022/santa-cruz/")
                    time.sleep(3)
                    soup2 = BeautifulSoup(driver.page_source, "html.parser")
                    script = soup2.find("script", {"id": "iv-page-context"})
                    DISTRICT =''
                    LOKSABHA =''
                    DISTRICT = ""
                    LOKSABHA = ""

                    # District
                    p1 = soup2.find(
                        "p",
                        class_=lambda c: c and
                            "text-muted" in c and
                            "mb-2" in c
                    )

                    if p1:
                        a = p1.find("a")
                        if a:
                            DISTRICT = a.get_text(strip=True)


                    # Lok Sabha - get last matching p
                    p2_list = soup2.find_all(
                        "p",
                        class_=lambda c: c and
                            "text-sm" in c and
                            "text-muted" in c and
                            "mb-1" in c
                    )

                    if p2_list:
                        p2 = p2_list[-1]

                        a = p2.find("a")
                        if a:
                            LOKSABHA = a.get_text(strip=True)


                    print("DISTRICT:", DISTRICT)
                    print("LOKSABHA:", LOKSABHA)
                    print("CONST:", url)
                    # print(script)
                    if script:
                        data = json.loads(script.string)
                        # print([
                        #    DISTRICT,
                        #     LOKSABHA,
                        #     summary,
                        #     json.dumps(data, ensure_ascii=False)
                        # ])
                        ws.append([
                            DISTRICT,
                            LOKSABHA,
                            summary,
                            json.dumps(data, ensure_ascii=False)
                        ])
            # -------------------------
            # Create Excel FOR THIS STATE
            # -------------------------
            wb.save(file_name)
            print(f"{state_name} -> {file_name}")