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
import traceback

STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=S03&"
BASE_URL    = f"{STATEURL}phase={{phase}}&submitName=100&page={{page}}"
STNAME      = 'ASSAM'
statePhaeid = 1
stateassemblies = """<select id="constId" name="constId" class="form-control">
<option value="16" selected="selected">ABHAYAPURI</option>

<option value="122">ALGAPUR-KATLICHERRA</option>

<option value="112">AMRI </option>

<option value="26">BAJALI</option>

<option value="42">BAKSA </option>

<option value="4">BAOKHUNGRI</option>

<option value="66">BARCHALLA</option>

<option value="59">BARHAMPUR</option>

<option value="38">BARKHETRI</option>

<option value="24">BARPETA </option>

<option value="71">BEHALI </option>

<option value="45">BHERGAON</option>

<option value="21">BHOWANIPUR-SORBHOG</option>

<option value="73">BIHPURIA</option>

<option value="20">BIJNI</option>

<option value="10">BILASIPARA</option>

<option value="62">BINNAKANDI</option>

<option value="9">BIRSING-JARUA</option>

<option value="70">BISWANATH</option>

<option value="108">BOKAJAN </option>

<option value="105">BOKAKHAT</option>

<option value="28">BOKO-CHAYGAON </option>

<option value="18">BONGAIGAON</option>

<option value="117">BORKHOLA</option>

<option value="87">CHABUA-LAHOWAL</option>

<option value="27">CHAMARIA</option>

<option value="23">CHENGA</option>

<option value="51">DALGAON</option>

<option value="95">DEMOW</option>

<option value="104">DERGAON</option>

<option value="77">DHAKUAKHANA </option>

<option value="65">DHEKIAJULI</option>

<option value="78">DHEMAJI </option>

<option value="55">DHING</option>

<option value="120">DHOLAI </option>

<option value="8">DHUBRI</option>

<option value="88">DIBRUGARH</option>

<option value="84">DIGBOI</option>

<option value="34">DIMORIA </option>

<option value="110">DIPHU </option>

<option value="33">DISPUR</option>

<option value="82">DOOMDOOMA</option>

<option value="2">DOTMA </option>

<option value="15">DUDHNOI </option>

<option value="90">DULIAJAN</option>

<option value="7">GAURIPUR</option>

<option value="14">GOALPARA EAST</option>

<option value="13">GOALPARA WEST</option>

<option value="72">GOHPUR</option>

<option value="103">GOLAGHAT</option>

<option value="6">GOLAKGANJ</option>

<option value="44">GORESWAR</option>

<option value="1">GOSSAIGAON</option>

<option value="36">GUWAHATI CENTRAL</option>

<option value="113">HAFLONG </option>

<option value="121">HAILAKANDI</option>

<option value="30">HAJO-SUALKUCHI</option>

<option value="63">HOJAI</option>

<option value="109">HOWRAGHAT </option>

<option value="52">JAGIROAD </option>

<option value="12">JALESWAR</option>

<option value="37">JALUKBARI</option>

<option value="80">JONAI </option>

<option value="100">JORHAT</option>

<option value="57">KALIABOR</option>

<option value="32">KAMALPUR</option>

<option value="123">KARIMGANJ NORTH</option>

<option value="124">KARIMGANJ SOUTH</option>

<option value="116">KATIGORAH</option>

<option value="89">KHOWANG</option>

<option value="106">KHUMTAI</option>

<option value="3">KOKRAJHAR</option>

<option value="53">LAHARIGHAT</option>

<option value="76">LAKHIMPUR</option>

<option value="114">LAKHIPUR</option>

<option value="64">LUMDING</option>

<option value="94">MAHMORA</option>

<option value="98">MAJULI </option>

<option value="85">MAKUM</option>

<option value="41">MANAS</option>

<option value="22">MANDIA</option>

<option value="50">MANGALDAI</option>

<option value="11">MANKACHAR</option>

<option value="83">MARGHERITA</option>

<option value="101">MARIANI</option>

<option value="47">MAZBAT</option>

<option value="54">MORIGAON</option>

<option value="69">NADUAR</option>

<option value="60">NAGAON-BATADRABA</option>

<option value="92">NAHARKATIA</option>

<option value="39">NALBARI</option>

<option value="97">NAZIRA</option>

<option value="35">NEW GUWAHATI</option>

<option value="75">NOWBOICHA </option>

<option value="25">PAKABETBARI</option>

<option value="29">PALASBARI</option>

<option value="5">PARBATJHORA</option>

<option value="125">PATHARKANDI</option>

<option value="61">RAHA </option>

<option value="126">RAM KRISHNA NAGAR </option>

<option value="68">RANGAPARA</option>

<option value="31">RANGIA</option>

<option value="111">RONGKHANG </option>

<option value="74">RONGONADI</option>

<option value="56">RUPAHIHAT</option>

<option value="81">SADIYA</option>

<option value="58">SAMAGURI</option>

<option value="107">SARUPATHAR</option>

<option value="96">SIBSAGAR</option>

<option value="19">SIDLI CHIRANG </option>

<option value="118">SILCHAR</option>

<option value="49">SIPAJHAR</option>

<option value="79">SISSIBORGAON</option>

<option value="119">SONAI</option>

<option value="93">SONARI</option>

<option value="17">SRIJANGRAM</option>

<option value="43">TAMULPUR</option>

<option value="48">TANGLA</option>

<option value="99">TEOK</option>

<option value="67">TEZPUR</option>

<option value="40">TIHU</option>

<option value="91">TINGKHONG</option>

<option value="86">TINSUKIA</option>

<option value="102">TITABOR</option>

<option value="46">UDALGURI</option>

<option value="115">UDHARBOND</option>
</select>"""

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

# def extract_contesting_from_page_source(html,constId):
#     # print(constId)
#     from bs4 import BeautifulSoup
#     soup = BeautifulSoup(html, "html.parser")
#     try:
#         # Find the table body
#         tbody = soup.find("table", id="data-tab").find("tbody")

#         all_candidates = []  # store all rows

#         # Loop through each row (candidate)
#         for tr in tbody.find_all("tr"):

#             # link_div = tr.find("div", class_="img-bx")  # find div with class
#             # if link_div:
#             #     link_tag = link_div.find("a")  # find <a> inside that div
#             #     link_url = link_tag["href"] if link_tag and link_tag.has_attr("href") else None
#             # else:
#             #     link_url = None

#             # driver = make_driver()
#             # driver.get(link_url)
#             # link_url_html = driver.page_source
#             # soup_html = BeautifulSoup(link_url_html, "html.parser")
#             # party_blocks = soup_html.find_all("div", class_="party")
#             # party_hd = ''
#             # candt_hd = ''
#             # for block in party_blocks:
#             #     col_items = block.find_all("div", class_="col-sm-6")

#             #     if len(col_items) >= 4:
#             #         party       = col_items[3]
#             #         party_hd    = (party.get_text(strip=True))
#             #         cand        = col_items[7]
#             #         candt_hd    = (cand.get_text(strip=True))

#             img_tag = tr.find("img")
#             photo_url = img_tag["src"] if img_tag else None

#             name_tag = tr.find("div", class_="details-name")
#             candidate_name = None

#             if name_tag:
#                 h4_tag = name_tag.find("h4")
#                 if h4_tag:
#                     candidate_name = h4_tag.get_text(strip=True)

#             data = {}
#             constName = ""
#             partyName = ""
#             stausValue = ""
#             for p in tr.find_all("p"):
#                 strong = p.find("strong")
#                 if strong:
#                     key = strong.get_text(strip=True).replace(":", "").strip()
#                     value = p.get_text(strip=True).replace(strong.get_text(strip=True), "").strip()
#                     if key == "Constituency":
#                         constName = value
#                     elif key == "Party":
#                         partyName = value
#                     elif key == "Status":
#                         stausValue = value
#                     else:     
#                         pass
#             soup3 = BeautifulSoup(stateassemblies, "html.parser")
#             option = soup3.find("option", string=constName)
#             constId = option["value"]
#             print("constId",constId)
#             if(stausValue.lower() == "accepted"):
#                 print("Status Value:", candidate_name)
#                 data["STATE NAME(ENGLISH)"] = STNAME
#                 # data["STATE NAME(HINDI)"] = ""
#                 data["STATE NAME(LOCAL LANGUAGE)"] = ""

#                 data["REGION CODE"] = ""
#                 data["REGION NAME(ENGLISH)"] = ""
#                 # data["REGION NAME(HINDI)"] = ""
#                 data["REGION NAME(LOCAL LANGUAGE)"] = ""

#                 data["DISTRICT CODE"] = ""
#                 data["DISTRICT NAME(ENGLISH)"] = ""
#                 # data["DISTRICT NAME(HINDI)"] = ""
#                 data["DISTRICT NAME(LOCAL LANGUAGE)"] = ""

#                 data["LOKSABHA CODE"] = ""
#                 data["LOKSABHA NAME(ENGLISH)"] = ""
#                 # data["LOKSABHA NAME(HINDI)"] = ""
#                 data["LOKSABHA NAME(LOCAL LANGUAGE)"] = ""

#                 data["ASSEMBLY CODE"] = int(constId)
#                 data["ASSEMBLY NAME(ENGLISH)"] = constName
#                 # data["ASSEMBLY NAME(HINDI)"] = ""
#                 data["ASSEMBLY NAME(LOCAL LANGUAGE)"] = ""

#                 data["CANDIDATE NAME(ENGLISH)"] = candidate_name
#                 # data["CANDIDATE NAME(HINDI)"] = candt_hd
#                 data["CANDIDATE NAME(LOCAL LANGUAGE)"] = ""

#                 data["PARTY SHORT NAME(ENGLISH)"] = partyName
#                 # data["PARTY SHORT NAME(HINDI)"] = party_hd
#                 data["PARTY SHORT NAME(LOCAL LANGUAGE)"] = ""

#                 data["PARTY FULL NAME(ENGLISH)"] = partyName
#                 # data["PARTY FULL NAME(HINDI)"] = party_hd
#                 data["PARTY FULL NAME(LOCAL LANGUAGE)"] = ""

#                 data["IS VIP(YES/NO)"] = ""
#                 data["CANDIDATE PHOTO"] = photo_url
#                 data["PHASE NUMBER"] = 1
#                 all_candidates.append(data)

#         return all_candidates
#     except:
#         print("An exception occurred")

def extract_contesting_from_page_source(html, stateassemblies, STNAME):
    from bs4 import BeautifulSoup
    import traceback

    soup = BeautifulSoup(html, "html.parser")

    # ✅ Parse assemblies ONCE (performance fix)
    soup3 = BeautifulSoup(stateassemblies, "html.parser")
    const_map = {}
    for option in soup3.find_all("option"):
        name = option.text.strip()
        value = option.get("value")
        if name and value:
            const_map[name] = value

    all_candidates = []

    try:
        # ✅ Safe table handling
        table = soup.find("table", id="data-tab")
        if not table:
            print("⚠️ Table not found")
            return []

        tbody = table.find("tbody")
        if not tbody:
            print("⚠️ Tbody not found")
            return []

        # ✅ Loop rows
        for tr in tbody.find_all("tr"):
            try:
                # --- Photo ---
                img_tag = tr.find("img")
                photo_url = img_tag["src"] if img_tag else None

                # --- Candidate Name ---
                candidate_name = None
                name_tag = tr.find("div", class_="details-name")
                if name_tag:
                    h4_tag = name_tag.find("h4")
                    if h4_tag:
                        candidate_name = h4_tag.get_text(strip=True)

                # --- Extract fields ---
                constName = ""
                partyName = ""
                statusValue = ""

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
                            statusValue = value

                # ✅ Validate constituency mapping
                constId = const_map.get(constName)
                if not constId:
                    print(f"⚠️ Constituency not found: {constName}")
                    continue

                # ✅ Filter only accepted
                if statusValue.lower() != "accepted":
                    continue

                # --- Build Data ---
                data = {
                    "STATE NAME(ENGLISH)": STNAME,
                    "STATE NAME(LOCAL LANGUAGE)": "",

                    "REGION CODE": "",
                    "REGION NAME(ENGLISH)": "",
                    "REGION NAME(LOCAL LANGUAGE)": "",

                    "DISTRICT CODE": "",
                    "DISTRICT NAME(ENGLISH)": "",
                    "DISTRICT NAME(LOCAL LANGUAGE)": "",

                    "LOKSABHA CODE": "",
                    "LOKSABHA NAME(ENGLISH)": "",
                    "LOKSABHA NAME(LOCAL LANGUAGE)": "",

                    "ASSEMBLY CODE": int(constId),
                    "ASSEMBLY NAME(ENGLISH)": constName,
                    "ASSEMBLY NAME(LOCAL LANGUAGE)": "",

                    "CANDIDATE NAME(ENGLISH)": candidate_name,
                    "CANDIDATE NAME(LOCAL LANGUAGE)": "",

                    "PARTY SHORT NAME(ENGLISH)": partyName,
                    "PARTY SHORT NAME(LOCAL LANGUAGE)": "",

                    "PARTY FULL NAME(ENGLISH)": partyName,
                    "PARTY FULL NAME(LOCAL LANGUAGE)": "",

                    "IS VIP(YES/NO)": "",
                    "CANDIDATE PHOTO": photo_url,
                    "PHASE NUMBER": 1
                }

                all_candidates.append(data)

            except Exception as row_error:
                print("❌ Error in row processing")
                print("Row HTML:", tr)
                print("Error:", row_error)
                traceback.print_exc()
                continue

        return all_candidates

    except Exception as e:
        print("❌ Main extraction error:", e)
        traceback.print_exc()
        return []

# def crawl_with_selenium(start=1, end=3,constId=1,phase=1,headless=True, delay=2.0):
#     driver = make_driver(headless=headless)
#     results = []
#     try:
#         for page in range(end):
#             page = page+start
#             if page > 0 and page >= start:
#                 url = BASE_URL.format(page=page,constId=constId,phase=phase)
#                 print(url)
#                 try:
#                     driver.get(url)
#                 except TimeoutException:
#                     print("Page load timeout, continuing.")
#                 # wait a little for JS to render (tune as necessary)
#                 time.sleep(delay)

#                 html = driver.page_source
#                 objData = extract_contesting_from_page_source(html,constId)
#                 try:
#                     for item in objData:
#                         results.append(item)
#                 except TypeError:
#                     print("No data found on this page.")
#     finally:
#         driver.quit()
#     return results

def crawl_with_selenium(start=1, end=3, constId=1, phase=1, headless=True, delay=2.0):
    driver = make_driver(headless=headless)
    results = []

    try:
        # ✅ Correct loop
        for page in range(start, end + 1):

            url = BASE_URL.format(page=page, constId=constId, phase=phase)
            print(f"🔗 Fetching Page {page}: {url}")

            try:
                driver.get(url)
            except TimeoutException:
                print("⚠️ Page load timeout, continuing...")

            # ✅ wait for JS render
            time.sleep(delay)

            html = driver.page_source

            try:
                objData = extract_contesting_from_page_source(html, stateassemblies, STNAME)

                # ✅ handle empty data
                if not objData:
                    print(f"⚠️ No data found on page {page}")
                    break   # 🚀 stop pagination if no data

                results.extend(objData)

            except Exception as e:
                print(f"❌ Error extracting page {page}: {e}")
                traceback.print_exc()
                continue

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
    filename = f"{STNAME}_PHASE_{statePhaeid}___{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Saved {filename}")