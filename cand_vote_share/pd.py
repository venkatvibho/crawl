from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from datetime import datetime

BASE_URL = "https://results.eci.gov.in/ResultAcGenMay2026/"
STNAME = "PUDUCHERRY"

stateassemblies = """<select class="custom-select" id="ctl00_ContentPlaceHolder1_Result1_ddlState" onchange="return GetResult(this)" name="state" style="float: right;"> <option value=""> Select Constituency </option><option value="U0719">ARIANKUPPAM - 19</option><option value="U0723">BAHOUR - 23</option><option value="U0721">EMBALAM - 21</option><option value="U078">INDIRA NAGAR - 8</option><option value="U077">KADIRGAMAM - 7</option><option value="U0712">KALAPET - 12</option><option value="U0710">KAMARAJ NAGAR - 10</option><option value="U0726">KARAIKAL NORTH - 26</option><option value="U0727">KARAIKAL SOUTH - 27</option><option value="U0711">LAWSPET - 11</option><option value="U0729">MAHE - 29</option><option value="U0720">MANAVELY - 20</option><option value="U074">MANGALAM - 4</option><option value="U071">MANNADIPET - 1</option><option value="U0718">MUDALIARPET - 18</option><option value="U0713">MUTHIALPET - 13</option><option value="U0724">NEDUNGADU - 24</option><option value="U0717">NELLITHOPE - 17</option><option value="U0728">NERAVY-T.R.PATTINAM - 28</option><option value="U0722">NETTAPAKKAM - 22</option><option value="U0716">ORLEAMPETH - 16</option><option value="U0715">OUPALAM - 15</option><option value="U073">OUSSUDU - 3</option><option value="U076">OZHUKARAI - 6</option><option value="U0714">RAJ BHAVAN - 14</option><option value="U079">THATTANCHAVADY - 9</option><option value="U072">THIRUBHUVANAI - 2</option><option value="U0725">THIRUNALLAR - 25</option><option value="U075">VILLIANUR - 5</option><option value="U0730">YANAM - 30</option></select>"""


# ✅ Your working driver + anti-detection
def make_driver(headless=True):
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # ✅ anti detection
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    driver.set_page_load_timeout(30)
    return driver


# ✅ MAIN
soup3 = BeautifulSoup(stateassemblies, "html.parser")
all_data = []

driver = make_driver(headless=False)  # 🔥 keep False for stability

for option in soup3.find_all("option"):
    constId = option.get("value")
    constName = option.text.strip()

    # skip empty
    if not constId or not constId.strip():
        continue

    url = f"{BASE_URL}Constituencywise{constId}.htm"
    print("Fetching:", constName, url)

    try:
        driver.get(url)

        # ✅ wait properly
        time.sleep(random.uniform(2, 4))

        page = driver.page_source

        # 🚫 handle block
        if "Access Denied" in page:
            print("🚫 Blocked:", constName)
            continue

        soup = BeautifulSoup(page, "html.parser")

        tables = soup.find_all("table")

        for table in tables:
            tbody = table.find("tbody")
            if not tbody:
                continue

            for row in tbody.find_all("tr"):
                cols = [td.text.strip() for td in row.find_all("td")]

                if len(cols) == 7 and cols[0] != "S.N":
                    all_data.append({
                        "Constituency": constName,
                        "S.N": cols[0],
                        "Candidate": cols[1],
                        "Party": cols[2],
                        "EVM Votes": cols[3],
                        "Postal Votes": cols[4],
                        "Total Votes": cols[5],
                        "% of Votes": cols[6],
                    })

    except Exception as e:
        print("⚠️ Error:", constName, e)

driver.quit()

# ✅ Save
df = pd.DataFrame(all_data)

filename = f"xlsx/{STNAME}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(filename, index=False)

print("✅ Saved:", filename)