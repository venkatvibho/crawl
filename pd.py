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

STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=U07&"
BASE_URL    = f"{STATEURL}phase={{phase}}&submitName=100&page={{page}}"
STNAME      = 'PUDUCHERRY'
statePhaeid = 1
stateassemblies = """<select id="constId" name="constId" class="form-control">

<option value="19">ARIANKUPPAM</option>

<option value="23">BAHOUR</option>

<option value="21">EMBALAM</option>

<option value="8">INDIRA NAGAR</option>

<option value="7">KADIRGAMAM</option>

<option value="12">KALAPET</option>

<option value="10">KAMARAJ NAGAR</option>

<option value="26">KARAIKAL NORTH</option>

<option value="27">KARAIKAL SOUTH</option>

<option value="11">LAWSPET</option>

<option value="29">MAHE</option>

<option value="20">MANAVELY</option>

<option value="4">MANGALAM</option>

<option value="1">MANNADIPET</option>

<option value="18">MUDALIARPET</option>

<option value="13">MUTHIALPET</option>

<option value="24">NEDUNGADU</option>

<option value="17">NELLITHOPE</option>

<option value="28">NERAVY-T.R.PATTINAM</option>

<option value="22">NETTAPAKKAM</option>

<option value="16">ORLEAMPETH</option>

<option value="15">OUPALAM</option>

<option value="3">OUSSUDU</option>

<option value="6">OZHUKARAI</option>

<option value="14">RAJ BHAVAN</option>

<option value="9">THATTANCHAVADY</option>

<option value="2">THIRUBHUVANAI</option>

<option value="25">THIRUNALLAR</option>

<option value="5">VILLIANUR</option>

<option value="30">YANAM</option>
</select>"""

def get_candidate_hd(link_url):
    try:
        response = requests.get(link_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        party_blocks = soup.find_all("div", class_="party")

        for block in party_blocks:
            col_items = block.find_all("div", class_="col-sm-6")

            if len(col_items) >= 8:
                candt_hd = col_items[7].get_text(strip=True)
                return candt_hd

    except Exception as e:
        print(f"❌ Error fetching {link_url}: {e}")

    return None

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

            link_div = tr.find("div", class_="img-bx")  # find div with class
            if link_div:
                link_tag = link_div.find("a")  # find <a> inside that div
                link_url = link_tag["href"] if link_tag and link_tag.has_attr("href") else None
            else:
                link_url = None

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

            candt_hd = None

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
                # print(strong)
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
            try:
                soup3 = BeautifulSoup(stateassemblies, "html.parser")

                constId = None
                constName_clean = constName.strip().upper()

                for option in soup3.find_all("option"):
                    opt_text = option.text.strip().upper()

                    if opt_text == constName_clean:
                        constId = option.get("value")
                        break

                if not constId:
                    print(f"⚠️ No constId found for: {constName}")
                else:
                    print("✅ constId:", constId)

            except Exception as e:
                print("❌ Error:", e)
            if(stausValue.lower() == "accepted"):
                print("Status Value:", candidate_name)
                data["STATE NAME(ENGLISH)"] = STNAME
                # data["STATE NAME(HINDI)"] = ""
                data["STATE NAME(LOCAL LANGUAGE)"] = ""

                data["REGION CODE"] = ""
                data["REGION NAME(ENGLISH)"] = ""
                # data["REGION NAME(HINDI)"] = ""
                data["REGION NAME(LOCAL LANGUAGE)"] = ""

                data["DISTRICT CODE"] = ""
                data["DISTRICT NAME(ENGLISH)"] = ""
                # data["DISTRICT NAME(HINDI)"] = ""
                data["DISTRICT NAME(LOCAL LANGUAGE)"] = ""

                data["LOKSABHA CODE"] = ""
                data["LOKSABHA NAME(ENGLISH)"] = ""
                # data["LOKSABHA NAME(HINDI)"] = ""
                data["LOKSABHA NAME(LOCAL LANGUAGE)"] = ""

                data["ASSEMBLY CODE"] = int(constId)
                data["ASSEMBLY NAME(ENGLISH)"] = constName
                # data["ASSEMBLY NAME(HINDI)"] = ""
                data["ASSEMBLY NAME(LOCAL LANGUAGE)"] = ""

                data["CANDIDATE NAME(ENGLISH)"] = candidate_name
                # data["CANDIDATE NAME(HINDI)"] = candt_hd
                data["CANDIDATE NAME(LOCAL LANGUAGE)"] = candt_hd

                data["PARTY SHORT NAME(ENGLISH)"] = partyName
                # data["PARTY SHORT NAME(HINDI)"] = party_hd
                data["PARTY SHORT NAME(LOCAL LANGUAGE)"] = ""

                data["PARTY FULL NAME(ENGLISH)"] = partyName
                # data["PARTY FULL NAME(HINDI)"] = party_hd
                data["PARTY FULL NAME(LOCAL LANGUAGE)"] = ""

                data["IS VIP(YES/NO)"] = ""
                data["CANDIDATE PHOTO"] = photo_url
                data["PHASE NUMBER"] = 1
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
            # f"{STATEURL}phase={objData['phase']}&submitName=100&constId={objData['id']}"
            f"{STATEURL}phase={statePhaeid}&submitName=100"
        )
        link_url_html = driver.page_source
        soup = BeautifulSoup(link_url_html, "html.parser")
        # divs = soup.find_all("div", class_="box-inner bg-dark-blu")
        divs = soup.find_all("div", class_="bg-blu")
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
    filename = f"xlsx/{STNAME}_PHASE_{statePhaeid}___{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Saved {filename}")