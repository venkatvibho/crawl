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
STNAME = "ASSAM"

stateassemblies = """
<select class="custom-select" id="ctl00_ContentPlaceHolder1_Result1_ddlState" onchange="return GetResult(this)" name="state" style="float: right;"> <option value=""> Select Constituency </option><option value="S0316">ABHAYAPURI - 16</option><option value="S03122">ALGAPUR-KATLICHERRA - 122</option><option value="S03112">AMRI  - 112</option><option value="S0326">BAJALI - 26</option><option value="S0342">BAKSA  - 42</option><option value="S034">BAOKHUNGRI - 4</option><option value="S0366">BARCHALLA - 66</option><option value="S0359">BARHAMPUR - 59</option><option value="S0338">BARKHETRI - 38</option><option value="S0324">BARPETA  - 24</option><option value="S0371">BEHALI  - 71</option><option value="S0345">BHERGAON - 45</option><option value="S0321">BHOWANIPUR-SORBHOG - 21</option><option value="S0373">BIHPURIA - 73</option><option value="S0320">BIJNI - 20</option><option value="S0310">BILASIPARA - 10</option><option value="S0362">BINNAKANDI - 62</option><option value="S039">BIRSING JARUA - 9</option><option value="S0370">BISWANATH - 70</option><option value="S03108">BOKAJAN  - 108</option><option value="S03105">BOKAKHAT - 105</option><option value="S0328">BOKO-CHAYGAON  - 28</option><option value="S0318">BONGAIGAON - 18</option><option value="S03117">BORKHOLA - 117</option><option value="S0387">CHABUA-LAHOWAL - 87</option><option value="S0327">CHAMARIA - 27</option><option value="S0323">CHENGA - 23</option><option value="S0351">DALGAON - 51</option><option value="S0395">DEMOW - 95</option><option value="S03104">DERGAON - 104</option><option value="S0377">DHAKUAKHANA  - 77</option><option value="S0365">DHEKIAJULI - 65</option><option value="S0378">DHEMAJI  - 78</option><option value="S0355">DHING - 55</option><option value="S03120">DHOLAI  - 120</option><option value="S038">DHUBRI - 8</option><option value="S0388">DIBRUGARH - 88</option><option value="S0384">DIGBOI - 84</option><option value="S0334">DIMORIA  - 34</option><option value="S03110">DIPHU  - 110</option><option value="S0333">DISPUR - 33</option><option value="S0382">DOOMDOOMA - 82</option><option value="S032">DOTMA  - 2</option><option value="S0315">DUDHNAI - 15</option><option value="S0390">DULIAJAN - 90</option><option value="S037">GAURIPUR - 7</option><option value="S0314">GOALPARA EAST - 14</option><option value="S0313">GOALPARA WEST - 13</option><option value="S0372">GOHPUR - 72</option><option value="S03103">GOLAGHAT - 103</option><option value="S036">GOLAKGANJ - 6</option><option value="S0344">GORESWAR - 44</option><option value="S031">GOSSAIGAON - 1</option><option value="S0336">GUWAHATI CENTRAL - 36</option><option value="S03113">HAFLONG  - 113</option><option value="S03121">HAILAKANDI - 121</option><option value="S0330">HAJO-SUALKUCHI - 30</option><option value="S0363">HOJAI - 63</option><option value="S03109">HOWRAGHAT  - 109</option><option value="S0352">JAGIROAD  - 52</option><option value="S0312">JALESHWAR - 12</option><option value="S0337">JALUKBARI - 37</option><option value="S0380">JONAI  - 80</option><option value="S03100">JORHAT - 100</option><option value="S0357">KALIABOR - 57</option><option value="S0332">KAMALPUR - 32</option><option value="S03123">KARIMGANJ NORTH - 123</option><option value="S03124">KARIMGANJ SOUTH - 124</option><option value="S03116">KATIGORAH - 116</option><option value="S0389">KHOWANG - 89</option><option value="S03106">KHUMTAI - 106</option><option value="S033">KOKRAJHAR - 3</option><option value="S0353">LAHARIGHAT - 53</option><option value="S0376">LAKHIMPUR - 76</option><option value="S03114">LAKHIPUR - 114</option><option value="S0364">LUMDING - 64</option><option value="S0394">MAHMORA - 94</option><option value="S0398">MAJULI  - 98</option><option value="S0385">MAKUM - 85</option><option value="S0341">MANAS - 41</option><option value="S0322">MANDIA - 22</option><option value="S0350">MANGALDAI - 50</option><option value="S0311">MANKACHAR - 11</option><option value="S0383">MARGHERITA - 83</option><option value="S03101">MARIANI - 101</option><option value="S0347">MAZBAT - 47</option><option value="S0354">MORIGAON - 54</option><option value="S0369">NADUAR - 69</option><option value="S0360">NAGAON-BATADRABA - 60</option><option value="S0392">NAHARKATIA - 92</option><option value="S0339">NALBARI - 39</option><option value="S0397">NAZIRA - 97</option><option value="S0335">NEW GUWAHATI - 35</option><option value="S0375">NOWBOICHA  - 75</option><option value="S0325">PAKABETBARI - 25</option><option value="S0329">PALASBARI - 29</option><option value="S035">PARBATJHORA - 5</option><option value="S03125">PATHARKANDI - 125</option><option value="S0361">RAHA  - 61</option><option value="S03126">RAM KRISHNA NAGAR  - 126</option><option value="S0368">RANGAPARA - 68</option><option value="S0331">RANGIA - 31</option><option value="S03111">RONGKHANG  - 111</option><option value="S0374">RONGONADI - 74</option><option value="S0356">RUPAHIHAT - 56</option><option value="S0381">SADIYA - 81</option><option value="S0358">SAMAGURI - 58</option><option value="S03107">SARUPATHAR - 107</option><option value="S0396">SIBSAGAR - 96</option><option value="S0319">SIDLI CHIRANG  - 19</option><option value="S03118">SILCHAR - 118</option><option value="S0349">SIPAJHAR - 49</option><option value="S0379">SISSIBARGAON - 79</option><option value="S03119">SONAI - 119</option><option value="S0393">SONARI - 93</option><option value="S0317">SRIJANGRAM - 17</option><option value="S0343">TAMULPUR - 43</option><option value="S0348">TANGLA - 48</option><option value="S0399">TEOK - 99</option><option value="S0367">TEZPUR - 67</option><option value="S0340">TIHU - 40</option><option value="S0391">TINGKHONG - 91</option><option value="S0386">TINSUKIA - 86</option><option value="S03102">TITABOR - 102</option><option value="S0346">UDALGURI - 46</option><option value="S03115">UDHARBOND - 115</option></select>
"""


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