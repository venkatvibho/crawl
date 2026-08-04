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

    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "-2024"

    # Create Excel
    file_name = f"LokSabha_Winners_{current_date}.xlsx"

    wb = Workbook()

    ws = wb.active
    ws.append([
        "SUMMERY","JSONDATA"
    ])
    ws.title = "Winners"

    # Main Lok Sabha 2024 page
    driver.get("https://www.indiavotes.com/lok-sabha/2024")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract all state links first
    state_links = soup.find_all(
        "a",
        class_=lambda c: c and "rounded-lg" in c and "text-sm" in c
    )
    summary = {}
    for card in soup.find_all("div", class_="card p-4"):

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

    states = []

    for a in state_links:

        state_span = a.find("span", class_="font-medium")

        if not state_span:
            continue
        state_name = state_span.get_text(strip=True).title()
        state_url = a.get("href")
        states.append({
            "name": state_name,
            "url": state_url,
            "summary":summary
        })
    # print(states)
    print("Total States Found:", len(states))
    for state in states:
        print(state["name"])
        # if state["name"] == "Andaman Nicobar Islands":
        if state["name"] != "":
            state_name = state["name"]
            state_url = state["url"]
            summery  = json.dumps(state["summary"], ensure_ascii=False)
            print("Processing: 22222", state_url)
            driver.get(f"https://www.indiavotes.com{state_url}")
            time.sleep(3)
            soup1 = BeautifulSoup(driver.page_source, "html.parser")
            tbody = soup1.find("table",id="iv-full-results").find("tbody")
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
                    time.sleep(3)
                    soup2 = BeautifulSoup(driver.page_source, "html.parser")
                    script = soup2.find("script", {"id": "iv-page-context"})
                    print(script)
                    if script:
                        data = json.loads(script.string)
                        print(data)
                        ws.append([
                            summery,
                            json.dumps(data, ensure_ascii=False)
                        ])
    print(
        "Completed:",
        "Total Records:",
        len(all_data)
    )
    wb.save(file_name)
    driver.quit()