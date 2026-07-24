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

STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=S11&"
BASE_URL    = f"{STATEURL}phase={{phase}}&page={{page}}"
STNAME      = 'KERALAM'
statePhaeid = 1

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

def extract_contesting_from_page_source(html,constId):
    # print(constId)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    try:
        # Find the table body
        tbody = soup.find("table", id="data-tab").find("tbody")

        all_candidates = []  # store all rows

        # Loop through each row (candidate)
        for tr in tbody.find_all("tr"):

            # link_div = tr.find("div", class_="img-bx")  # find div with class
            # if link_div:
            #     link_tag = link_div.find("a")  # find <a> inside that div
            #     link_url = link_tag["href"] if link_tag and link_tag.has_attr("href") else None
            # else:
            #     link_url = None

            # driver = make_driver()
            # driver.get(link_url)
            # link_url_html = driver.page_source
            # soup_html = BeautifulSoup(link_url_html, "html.parser")
            # party_blocks = soup_html.find_all("div", class_="party")
            # party_hd = ''
            # candt_hd = ''
            # for block in party_blocks:
            #     col_items = block.find_all("div", class_="col-sm-6")

            #     if len(col_items) >= 4:
            #         party       = col_items[3]
            #         party_hd    = (party.get_text(strip=True))
            #         cand        = col_items[7]
            #         candt_hd    = (cand.get_text(strip=True))

            img_tag = tr.find("img")
            photo_url = img_tag["src"] if img_tag else None

            name_tag = tr.find("div", class_="details-name")
            candidate_name = None

            if name_tag:
                h4_tag = name_tag.find("h4")
                if h4_tag:
                    candidate_name = h4_tag.get_text(strip=True)

            data = {}
            constName = ""
            partyName = ""
            stausValue = ""
            for p in tr.find_all("p"):
                strong = p.find("strong")
                if strong:
                    key = strong.get_text(strip=True).replace(":", "").strip()
                    value = p.get_text(strip=True).replace(strong.get_text(strip=True), "").strip()
                    if key == "Constituency":
                        constName = value
                    elif key == "Party":
                        partyName = value
                    elif key == "Status":
                        stausValue = value
                    else:     
                        pass
            if(stausValue.lower() == "accepted"):
                print("Status Value:", candidate_name)
                data["PARTY"] = partyName
                all_candidates.append(data)

        return all_candidates
    except:
        print("An exception occurred")

def crawl_with_selenium(start=1, end=3,constId=1,phase=1,headless=True, delay=2.0):
    driver = make_driver(headless=headless)
    results = []
    try:
        for page in range(end):
            page = page+start
            if page > 0 and page >= start:
                url = BASE_URL.format(page=page,constId=constId,phase=phase)
                print(url)
                try:
                    driver.get(url)
                except TimeoutException:
                    print("Page load timeout, continuing.")
                # wait a little for JS to render (tune as necessary)
                time.sleep(delay)

                html = driver.page_source
                objData = extract_contesting_from_page_source(html,constId)
                try:
                    for item in objData:
                        results.append(item)
                except TypeError:
                    print("No data found on this page.")
    finally:
        driver.quit()
    return results

if __name__ == "__main__":
    from bs4 import BeautifulSoup

    # soup1 = BeautifulSoup(html, "html.parser")
    # options1 = [
    #     {"phase": 1, "id": int(opt["value"])}
    #     for opt in soup1.find_all("option")
    #     if opt.get("value") and opt["value"].isdigit()
    # ]
    # merged = options1 + options2
    # merged = options1
    all_data = []
    merged = [{'phase':1,'id':1}]
    # print(len(merged))
    for objData in merged:
        driver = make_driver()
        driver.get(
            # f"{STATEURL}phase={statePhaeid}&submitName=100"
            f"{STATEURL}phase={statePhaeid}"
        )
        link_url_html = driver.page_source
        soup = BeautifulSoup(link_url_html, "html.parser")
        divs = soup.find_all("div", class_="box-inner bg-dark-blu")
        # divs = soup.find_all("div", class_="bg-blu")
        # print(f"ALL {divs}")
        number = 0
        for d in divs:
            if (span := d.find("span")):
                number = int(span.text)
        print(f"ALL {number}")
        if number > 0:
            page_count = math.ceil(number / 10)
            print("Total",page_count)
            data = crawl_with_selenium(1, page_count, objData['id'],objData['phase'], headless=True, delay=1)
            all_data.extend(data)

    df = pd.DataFrame(all_data)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{STNAME}_PHASE_{statePhaeid}___{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Saved {filename}")