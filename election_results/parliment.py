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

# if __name__ == "__main__":
#     import re
#     driver = make_driver()

#     # State list page
#     driver.get("https://www.indiavotes.com/lok-sabha/2024/")
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     # Find all state links
#     state_links = soup.find_all(
#         "a",
#         class_=lambda c: c and "rounded-lg" in c and "text-sm" in c
#     )
#     for a in state_links:
#         state_name = a.get_text(strip=True).lower()
#         state_url = a.get("href")
#         print(state_name, state_url)
#         print("==========================================")
#         if state_name == "andhra pradesh25":
#             # Open selected state page
#             driver.get(f"https://www.indiavotes.com{state_url}")

#             soup = BeautifulSoup(driver.page_source, "html.parser")

#             # Constituency table
#             tbody = soup.find("tbody")

#             if tbody:
#                 for tr in tbody.find_all("tr"):
#                     tds = tr.find_all("td")

#                     constituency = tds[0].get_text(" ", strip=True)

#                     candidate_span = tds[1].find("span", class_="font-medium")
#                     party_span = tds[1].find("span", class_="text-muted")

#                     candidate = candidate_span.get_text(strip=True) if candidate_span else ""
#                     party = party_span.get_text(strip=True).strip("()") if party_span else ""

#                     vote_share = tds[2].get_text(" ", strip=True)
#                     margin = re.sub(r'\s+vs\s+.*$', '', tds[3].get_text(" ", strip=True))

#                     print([constituency, candidate, party, vote_share, margin])
#     driver.quit()

# if __name__ == "__main__":

#     driver = make_driver()

#     current_date = datetime.now().strftime("%Y-%m-%d")
#     output_dir = "election_results"

#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     driver.get("https://www.indiavotes.com/lok-sabha/2024/")
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     state_links = soup.find_all(
#         "a",
#         class_=lambda c: c and "rounded-lg" in c and "text-sm" in c
#     )

#     for a in state_links:

#         state_name = a.get_text(strip=True).lower()
#         state_url = a.get("href")

#         print(state_name, state_url)

#         if state_name in ["andaman nicobar islands1", "andhra pradesh25"]:

#             driver.get(f"https://www.indiavotes.com{state_url}")

#             soup = BeautifulSoup(driver.page_source, "html.parser")

#             tbody = soup.find("tbody")

#             if tbody:

#                 data = []

#                 for tr in tbody.find_all("tr"):

#                     tds = tr.find_all("td")

#                     if len(tds) < 4:
#                         continue

#                     constituency = tds[0].get_text(" ", strip=True)

#                     candidate_span = tds[1].find("span", class_="font-medium")
#                     party_span = tds[1].find("span", class_="text-muted")

#                     candidate = candidate_span.get_text(strip=True) if candidate_span else ""
#                     party = party_span.get_text(strip=True).strip("()") if party_span else ""

#                     vote_share = tds[2].get_text(" ", strip=True)

#                     margin_text = tds[3].get_text(" ", strip=True)
#                     margin = re.sub(r'\s+vs\s+.*$', '', margin_text)

#                     data.append([
#                         constituency,
#                         candidate,
#                         party,
#                         vote_share,
#                         margin
#                     ])

#                 # Create Excel file
#                 file_name = f"{state_name.replace(' ','_')}_{current_date}.xlsx"
#                 file_path = os.path.join(output_dir, file_name)

#                 wb = Workbook()
#                 ws = wb.active
#                 ws.title = "Winners"

#                 # Header
#                 ws.append([
#                     "Constituency",
#                     "Candidate",
#                     "Party",
#                     "Vote Share",
#                     "Margin"
#                 ])

#                 # Data
#                 for row in data:
#                     ws.append(row)

#                 wb.save(file_path)
#                 print(f"Saved: {file_path}")
#     driver.quit()

from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
import re

if __name__ == "__main__":

    driver = make_driver()
    all_data = []

    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "-2004"

    # Main Lok Sabha 2024 page
    driver.get("https://www.indiavotes.com/lok-sabha/2004/")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract all state links first
    state_links = soup.find_all(
        "a",
        class_=lambda c: c and "rounded-lg" in c and "text-sm" in c
    )

    states = []

    for a in state_links:

        state_span = a.find("span", class_="font-medium")

        if not state_span:
            continue

        state_name = state_span.get_text(strip=True).title()
        state_url = a.get("href")

        states.append({
            "name": state_name,
            "url": state_url
        })


    print("Total States Found:", len(states))


    for state in states:
        print(state["name"])
        if state["name"] != "":
            state_name = state["name"]
            state_url = state["url"]

            print("Processing:", state_url)

            driver.get(f"https://www.indiavotes.com{state_url}")
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, "html.parser")

            tbody = soup.find("tbody")
            print(tbody)
            if not tbody:
                print("No table found:", state_name)
                continue
    # for state in states:

    #     state_name = state["name"]
    #     state_url = state["url"]
    #     print("Processing:", state_name, state_url)

    #     driver.get(f"https://www.indiavotes.com{state_url}")

    #     try:
    #         WebDriverWait(driver, 15).until(
    #             EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    #         )
    #     except:
    #         print("====================================================")
    #         print("Table not loaded:", state_name)
    #         continue

    #     soup = BeautifulSoup(driver.page_source, "html.parser")

    #     tbody = soup.find("tbody")

    #     if tbody is None:
    #         print("No tbody:", state_name)
    #         continue

            for tr in tbody.find_all("tr"):

                tds = tr.find_all("td")

                if len(tds) < 4:
                    continue


                # Constituency
                constituency = tds[0].get_text(" ", strip=True)


                # Candidate
                candidate_span = tds[1].find(
                    "span",
                    class_="font-medium"
                )

                candidate = (
                    candidate_span.get_text(strip=True)
                    if candidate_span else ""
                )


                # Party
                party_span = tds[1].find(
                    "span",
                    class_="text-muted"
                )

                party = (
                    party_span.get_text(strip=True).strip("()")
                    if party_span else ""
                )


                # Vote share
                vote_share = tds[2].get_text(" ", strip=True)


                # Margin remove "vs PARTY"
                margin_text = tds[3].get_text(" ", strip=True)

                margin = re.sub(
                    r'\s+vs\s+.*$',
                    '',
                    margin_text
                )


                all_data.append([
                    state_name,
                    constituency,
                    candidate,
                    party,
                    vote_share,
                    margin
                ])


            print(
                "Completed:",
                state_name,
                "Total Records:",
                len(all_data)
            )


        # Create Excel
        file_name = f"LokSabha_Winners_{current_date}.xlsx"


        wb = Workbook()

        ws = wb.active
        ws.title = "Winners"


        # Header
        ws.append([
            "State Name",
            "Constituency",
            "Candidate",
            "Party",
            "Vote Share",
            "Margin"
        ])


        # Data rows
        for row in all_data:
            ws.append(row)


        # Auto width
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))

            ws.column_dimensions[column_letter].width = max_length + 3


        wb.save(file_name)


        # print("==============================")
        # print("Excel Created:", file_name)
        # print("Total Winners:", len(all_data))
        # print("==============================")
    driver.quit()