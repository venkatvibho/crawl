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

STATEURL    = "https://affidavit.eci.gov.in/CandidateCustomFilter?electionType=32-AC-GENERAL-3-60&election=32-AC-GENERAL-3-60&states=S25&phase=1&submitName=100&"
BASE_URL    = f"{STATEURL}phase={{phase}}&submitName=100&page={{page}}"
STNAME      = 'WEST BENGAL'
statePhaeid = 1
stateassemblies = """<select id="constId" name="constId" class="form-control">

<option value="12">ALIPURDUARS</option>

<option value="280">ASANSOL DAKSHIN</option>

<option value="281">ASANSOL UTTAR</option>

<option value="240">BAGHMUNDI</option>

<option value="72">BAHARAMPUR</option>

<option value="54">BAISNABNAGAR</option>

<option value="239">BALARAMPUR</option>

<option value="39">BALURGHAT</option>

<option value="238">BANDWAN</option>

<option value="252">BANKURA</option>

<option value="283">BARABANI</option>

<option value="253">BARJORA</option>

<option value="71">BELDANGA</option>

<option value="214">BHAGABANPUR</option>

<option value="62">BHAGAWANGOLA</option>

<option value="69">BHARATPUR</option>

<option value="237">BINPUR</option>

<option value="255">BISHNUPUR</option>

<option value="286">BOLPUR</option>

<option value="67">BURWAN</option>

<option value="31">CHAKULIA</option>

<option value="45">CHANCHAL</option>

<option value="211">CHANDIPUR</option>

<option value="232">CHANDRAKONA</option>

<option value="248">CHHATNA</option>

<option value="28">CHOPRA</option>

<option value="4">COOCHBEHAR DAKSHIN</option>

<option value="3">COOCHBEHAR UTTAR</option>

<option value="19">DABGRAM-FULBARI</option>

<option value="219">DANTAN</option>

<option value="23">DARJEELING</option>

<option value="230">DASPUR</option>

<option value="229">DEBRA</option>

<option value="15">DHUPGURI</option>

<option value="7">DINHATA</option>

<option value="75">DOMKAL</option>

<option value="284">DUBRAJPUR</option>

<option value="277">DURGAPUR PASCHIM</option>

<option value="276">DURGAPUR PURBA</option>

<option value="218">EGRA</option>

<option value="51">ENGLISH BAZAR</option>

<option value="13">FALAKATA</option>

<option value="55">FARAKKA</option>

<option value="41">GANGARAMPUR</option>

<option value="233">GARBETA</option>

<option value="44">GAZOLE</option>

<option value="231">GHATAL</option>

<option value="30">GOALPOKHAR</option>

<option value="221">GOPIBALLAVPUR</option>

<option value="43">HABIBPUR</option>

<option value="209">HALDIA</option>

<option value="292">HANSAN</option>

<option value="73">HARIHARPARA</option>

<option value="42">HARIRAMPUR</option>

<option value="46">HARISCHANDRAPUR</option>

<option value="33">HEMTABAD</option>

<option value="257">INDUS</option>

<option value="29">ISLAMPUR</option>

<option value="36">ITAHAR</option>

<option value="76">JALANGI</option>

<option value="17">JALPAIGURI</option>

<option value="279">JAMURIA</option>

<option value="58">JANGIPUR</option>

<option value="222">JHARGRAM</option>

<option value="241">JOYPUR</option>

<option value="11">KALCHINI</option>

<option value="34">KALIAGANJ</option>

<option value="22">KALIMPONG</option>

<option value="68">KANDI</option>

<option value="216">KANTHI DAKSHIN</option>

<option value="213">KANTHI UTTAR</option>

<option value="32">KARANDIGHI</option>

<option value="244">KASHIPUR</option>

<option value="256">KATULPUR</option>

<option value="223">KESHIARY</option>

<option value="235">KESHPUR</option>

<option value="228">KHARAGPUR</option>

<option value="224">KHARAGPUR SADAR</option>

<option value="66">KHARGRAM</option>

<option value="215">KHEJURI</option>

<option value="282">KULTI</option>

<option value="38">KUMARGANJ</option>

<option value="10">KUMARGRAM</option>

<option value="24">KURSEONG</option>

<option value="37">KUSHMANDI</option>

<option value="288">LABPUR</option>

<option value="61">LALGOLA</option>

<option value="14">MADARIHAT</option>

<option value="208">MAHISADAL</option>

<option value="20">MAL</option>

<option value="47">MALATIPUR</option>

<option value="50">MALDAHA</option>

<option value="243">MANBAZAR</option>

<option value="49">MANIKCHAK</option>

<option value="2">MATHABHANGA</option>

<option value="25">MATIGARA-NAXALBARI</option>

<option value="16">MAYNAGURI</option>

<option value="290">MAYURESWAR</option>

<option value="236">MEDINIPUR</option>

<option value="1">MEKLIGANJ</option>

<option value="52">MOTHABARI</option>

<option value="206">MOYNA</option>

<option value="294">MURARAI</option>

<option value="64">MURSHIDABAD</option>

<option value="65">NABAGRAM</option>

<option value="21">NAGRAKATA</option>

<option value="293">NALHATI</option>

<option value="207">NANDAKUMAR</option>

<option value="210">NANDIGRAM</option>

<option value="287">NANOOR</option>

<option value="225">NARAYANGARH</option>

<option value="8">NATABARI</option>

<option value="220">NAYAGRAM</option>

<option value="74">NOWDA</option>

<option value="254">ONDA</option>

<option value="275">PANDABESWAR</option>

<option value="205">PANSKURA PASCHIM</option>

<option value="204">PANSKURA PURBA</option>

<option value="245">PARA</option>

<option value="212">PATASHPUR</option>

<option value="27">PHANSIDEWA</option>

<option value="227">PINGLA</option>

<option value="242">PURULIA</option>

<option value="59">RAGHUNATHGANJ</option>

<option value="246">RAGHUNATHPUR</option>

<option value="35">RAIGANJ</option>

<option value="250">RAIPUR</option>

<option value="18">RAJGANJ</option>

<option value="217">RAMNAGAR</option>

<option value="291">RAMPURHAT</option>

<option value="249">RANIBANDH</option>

<option value="278">RANIGANJ</option>

<option value="63">RANINAGAR</option>

<option value="48">RATUA</option>

<option value="70">REJINAGAR</option>

<option value="226">SABANG</option>

<option value="60">SAGARDIGHI</option>

<option value="289">SAINTHIA</option>

<option value="234">SALBONI</option>

<option value="247">SALTORA</option>

<option value="56">SAMSERGANJ</option>

<option value="26">SILIGURI</option>

<option value="6">SITAI</option>

<option value="5">SITALKUCHI</option>

<option value="258">SONAMUKHI</option>

<option value="53">SUJAPUR</option>

<option value="285">SURI</option>

<option value="57">SUTI</option>

<option value="251">TALDANGRA</option>

<option value="203">TAMLUK</option>

<option value="40">TAPAN</option>

<option value="9">TUFANGANJ</option>
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