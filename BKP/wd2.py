# file: eci_contesting_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
import pandas as pd
from deep_translator import GoogleTranslator
import time
from datetime import datetime
import math
import requests

STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=S25&phase=1&submitName=100&"
STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=S25&phase=3&constId=102&submitName=100"
BASE_URL    = f"{STATEURL}phase={{phase}}&submitName=100&page={{page}}"
STNAME      = 'WEST BENGAL'
statePhaeid = 2
# 🔹 Change this dynamically
TARGET_LANG = "bn"   # hi, te, mr, ta, bn etc.

LANG_MAP = {
    "hindi": "hi",
    "bengali": "bn",
    "telugu": "te",
    "marathi": "mr",
    "tamil": "ta",
    "gujarati": "gu",
    "kannada": "kn",
    "malayalam": "ml",
    "punjabi": "pa",
    "urdu": "ur",
    "odia": "or",
    "assamese": "as"
}

stateassemblies = """<select id="constId" name="constId" class="form-control">
              <option value="" selected="selected">Select Constituency</option>
                            
                                          <option value="102" selected="selected">AMDANGA</option>
                                          
                                          <option value="181">AMTA</option>
                                          
                                          <option value="200">ARAMBAG</option>
                                          
                                          <option value="101">ASHOKNAGAR</option>
                                          
                                          <option value="273">AUSGRAM</option>
                                          
                                          <option value="99">BADURIA</option>
                                          
                                          <option value="94">BAGDA</option>
                                          
                                          <option value="180">BAGNAN</option>
                                          
                                          <option value="191">BALAGARH</option>
                                          
                                          <option value="169">BALLY</option>
                                          
                                          <option value="161">BALLYGUNGE</option>
                                          
                                          <option value="96">BANGAON DAKSHIN</option>
                                          
                                          <option value="95">BANGAON UTTAR</option>
                                          
                                          <option value="113">BARANAGAR</option>
                                          
                                          <option value="119">BARASAT</option>
                                          
                                          <option value="260">BARDHAMAN DAKSHIN</option>
                                          
                                          <option value="266">BARDHAMAN UTTAR</option>
                                          
                                          <option value="108">BARRACKPUR</option>
                                          
                                          <option value="140">BARUIPUR PASCHIM</option>
                                          
                                          <option value="137">BARUIPUR PURBA</option>
                                          
                                          <option value="128">BASANTI</option>
                                          
                                          <option value="124">BASIRHAT DAKSHIN</option>
                                          
                                          <option value="125">BASIRHAT UTTAR</option>
                                          
                                          <option value="154">BEHALA PASCHIM</option>
                                          
                                          <option value="153">BEHALA PURBA</option>
                                          
                                          <option value="164">BELEGHATA</option>
                                          
                                          <option value="159">BHABANIPUR</option>
                                          
                                          <option value="148">BHANGAR</option>
                                          
                                          <option value="267">BHATAR</option>
                                          
                                          <option value="105">BHATPARA</option>
                                          
                                          <option value="116">BIDHANNAGAR</option>
                                          
                                          <option value="103">BIJPUR</option>
                                          
                                          <option value="146">BISHNUPUR</option>
                                          
                                          <option value="156">BUDGE BUDGE</option>
                                          
                                          <option value="138">CANNING PASCHIM</option>
                                          
                                          <option value="139">CANNING PURBA</option>
                                          
                                          <option value="91">CHAKDAHA</option>
                                          
                                          <option value="187">CHAMPDANI</option>
                                          
                                          <option value="189">CHANDANNAGAR</option>
                                          
                                          <option value="194">CHANDITALA</option>
                                          
                                          <option value="82">CHAPRA</option>
                                          
                                          <option value="162">CHOWRANGEE</option>
                                          
                                          <option value="190">CHUNCHURA</option>
                                          
                                          <option value="120">DEGANGA</option>
                                          
                                          <option value="197">DHANEKHALI</option>
                                          
                                          <option value="143">DIAMOND HARBOUR</option>
                                          
                                          <option value="184">DOMJUR</option>
                                          
                                          <option value="114">DUM DUM</option>
                                          
                                          <option value="110">DUM DUM UTTAR</option>
                                          
                                          <option value="163">ENTALLY</option>
                                          
                                          <option value="144">FALTA</option>
                                          
                                          <option value="97">GAIGHATA</option>
                                          
                                          <option value="274">GALSI</option>
                                          
                                          <option value="201">GOGHAT</option>
                                          
                                          <option value="127">GOSABA</option>
                                          
                                          <option value="100">HABRA</option>
                                          
                                          <option value="93">HARINGHATA</option>
                                          
                                          <option value="196">HARIPAL</option>
                                          
                                          <option value="121">HAROA</option>
                                          
                                          <option value="126">HINGALGANJ</option>
                                          
                                          <option value="173">HOWRAH DAKSHIN</option>
                                          
                                          <option value="171">HOWRAH MADHYA</option>
                                          
                                          <option value="170">HOWRAH UTTAR</option>
                                          
                                          <option value="150">JADAVPUR</option>
                                          
                                          <option value="183">JAGATBALLAVPUR</option>
                                          
                                          <option value="106">JAGATDAL</option>
                                          
                                          <option value="262">JAMALPUR</option>
                                          
                                          <option value="195">JANGIPARA</option>
                                          
                                          <option value="136">JAYNAGAR</option>
                                          
                                          <option value="165">JORASANKO</option>
                                          
                                          <option value="131">KAKDWIP</option>
                                          
                                          <option value="80">KALIGANJ</option>
                                          
                                          <option value="264">KALNA</option>
                                          
                                          <option value="92">KALYANI</option>
                                          
                                          <option value="112">KAMARHATI</option>
                                          
                                          <option value="77">KARIMPUR</option>
                                          
                                          <option value="149">KASBA</option>
                                          
                                          <option value="168">KASHIPUR-BELGACHHIA</option>
                                          
                                          <option value="270">KATWA</option>
                                          
                                          <option value="271">KETUGRAM</option>
                                          
                                          <option value="202">KHANAKUL</option>
                                          
                                          <option value="259">KHANDAGHOSH</option>
                                          
                                          <option value="109">KHARDAHA</option>
                                          
                                          <option value="158">KOLKATA PORT</option>
                                          
                                          <option value="88">KRISHNAGANJ</option>
                                          
                                          <option value="85">KRISHNANAGAR DAKSHIN</option>
                                          
                                          <option value="83">KRISHNANAGAR UTTAR</option>
                                          
                                          <option value="133">KULPI</option>
                                          
                                          <option value="129">KULTALI</option>
                                          
                                          <option value="118">MADHYAMGRAM</option>
                                          
                                          <option value="142">MAGRAHAT PASCHIM</option>
                                          
                                          <option value="141">MAGRAHAT PURBA</option>
                                          
                                          <option value="155">MAHESHTALA</option>
                                          
                                          <option value="135">MANDIRBAZAR</option>
                                          
                                          <option value="272">MANGALKOT</option>
                                          
                                          <option value="167">MANIKTALA</option>
                                          
                                          <option value="265">MEMARI</option>
                                          
                                          <option value="157">METIABURUZ</option>
                                          
                                          <option value="122">MINAKHAN</option>
                                          
                                          <option value="263">MONTESWAR</option>
                                          
                                          <option value="84">NABADWIP</option>
                                          
                                          <option value="104">NAIHATI</option>
                                          
                                          <option value="81">NAKASHIPARA</option>
                                          
                                          <option value="107">NOAPARA</option>
                                          
                                          <option value="79">PALASHIPARA</option>
                                          
                                          <option value="175">PANCHLA</option>
                                          
                                          <option value="192">PANDUA</option>
                                          
                                          <option value="111">PANIHATI</option>
                                          
                                          <option value="130">PATHARPRATIMA</option>
                                          
                                          <option value="268">PURBASTHALI DAKSHIN</option>
                                          
                                          <option value="269">PURBASTHALI UTTAR</option>
                                          
                                          <option value="199">PURSURAH</option>
                                          
                                          <option value="134">RAIDIGHI</option>
                                          
                                          <option value="261">RAINA</option>
                                          
                                          <option value="117">RAJARHAT  GOPALPUR</option>
                                          
                                          <option value="115">RAJARHAT NEW TOWN</option>
                                          
                                          <option value="90">RANAGHAT DAKSHIN</option>
                                          
                                          <option value="87">RANAGHAT UTTAR PASCHIM</option>
                                          
                                          <option value="89">RANAGHAT UTTAR PURBA</option>
                                          
                                          <option value="160">RASHBEHARI</option>
                                          
                                          <option value="132">SAGAR</option>
                                          
                                          <option value="123">SANDESHKHALI</option>
                                          
                                          <option value="174">SANKRAIL</option>
                                          
                                          <option value="86">SANTIPUR</option>
                                          
                                          <option value="193">SAPTAGRAM</option>
                                          
                                          <option value="145">SATGACHHIA</option>
                                          
                                          <option value="172">SHIBPUR</option>
                                          
                                          <option value="166">SHYAMPUKUR</option>
                                          
                                          <option value="179">SHYAMPUR</option>
                                          
                                          <option value="188">SINGUR</option>
                                          
                                          <option value="147">SONARPUR DAKSHIN</option>
                                          
                                          <option value="151">SONARPUR UTTAR</option>
                                          
                                          <option value="186">SREERAMPUR</option>
                                          
                                          <option value="98">SWARUPNAGAR</option>
                                          
                                          <option value="198">TARAKESWAR</option>
                                          
                                          <option value="78">TEHATTA</option>
                                          
                                          <option value="152">TOLLYGANJ</option>
                                          
                                          <option value="182">UDAYNARAYANPUR</option>
                                          
                                          <option value="178">ULUBERIA DAKSHIN</option>
                                          
                                          <option value="176">ULUBERIA PURBA</option>
                                          
                                          <option value="177">ULUBERIA UTTAR</option>
                                          
                                          <option value="185">UTTARPARA</option>
                                                                    </select>"""

# ================= TRANSLATION =================
def translate_text(text, target_lang):
    try:
        if text:
            return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
    return text

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
                
                candt_hd = translate_text(candidate_name, TARGET_LANG)
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
                data["CANDIDATE NAME(HINDI)"] = candt_hd
                data["CANDIDATE NAME(LOCAL LANGUAGE)"] = candt_hd

                data["PARTY SHORT NAME(ENGLISH)"] = partyName
                # data["PARTY SHORT NAME(HINDI)"] = party_local
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