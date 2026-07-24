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
STNAME = "KERALA"

stateassemblies = """<select class="custom-select" id="ctl00_ContentPlaceHolder1_Result1_ddlState" onchange="return GetResult(this)" name="state" style="float: right;"> <option value=""> Select Constituency </option><option value="S11115">ADOOR  - 115</option><option value="S11104">ALAPPUZHA - 104</option><option value="S1160">ALATHUR - 60</option><option value="S1176">ALUVA - 76</option><option value="S11105">AMBALAPPUZHA - 105</option><option value="S1175">ANGAMALY - 75</option><option value="S11113">ARANMULA - 113</option><option value="S11102">AROOR - 102</option><option value="S11136">ARUVIKKARA - 136</option><option value="S11128">ATTINGAL  - 128</option><option value="S1110">AZHIKODE - 10</option><option value="S1125">BALUSSERI - 25</option><option value="S1129">BEYPORE - 29</option><option value="S11122">CHADAYAMANGALAM - 122</option><option value="S1172">CHALAKUDY - 72</option><option value="S1199">CHANGANASSERY - 99</option><option value="S11126">CHATHANNOOR - 126</option><option value="S11117">CHAVARA - 117</option><option value="S1161">CHELAKKARA - 61</option><option value="S11110">CHENGANNUR - 110</option><option value="S11103">CHERTHALA - 103</option><option value="S11129">CHIRAYINKEEZHU - 129</option><option value="S1158">CHITTUR - 58</option><option value="S1188">DEVIKULAM  - 88</option><option value="S1112">DHARMADAM - 12</option><option value="S1126">ELATHUR - 26</option><option value="S1182">ERANAKULAM - 82</option><option value="S11125">ERAVIPURAM - 125</option><option value="S1134">ERNAD - 34</option><option value="S1196">ETTUMANOOR - 96</option><option value="S1163">GURUVAYOOR - 63</option><option value="S11107">HARIPAD - 107</option><option value="S1191">IDUKKI - 91</option><option value="S119">IRIKKUR - 9</option><option value="S1170">IRINJALAKUDA - 70</option><option value="S1194">KADUTHURUTHY - 94</option><option value="S1169">KAIPAMANGALAM - 69</option><option value="S1177">KALAMASSERY - 77</option><option value="S117">KALLIASSERI - 7</option><option value="S1119">KALPETTA - 19</option><option value="S114">KANHANGAD - 4</option><option value="S11100">KANJIRAPPALLY - 100</option><option value="S1111">KANNUR - 11</option><option value="S11116">KARUNAGAPPALLY - 116</option><option value="S112">KASARAGOD - 2</option><option value="S11138">KATTAKKADA - 138</option><option value="S11108">KAYAMKULAM - 108</option><option value="S11132">KAZHAKOOTTAM - 132</option><option value="S1180">KOCHI - 80</option><option value="S1173">KODUNGALLUR - 73</option><option value="S1131">KODUVALLY - 31</option><option value="S11124">KOLLAM - 124</option><option value="S1133">KONDOTTY - 33</option><option value="S1153">KONGAD - 53</option><option value="S11114">KONNI - 114</option><option value="S1187">KOTHAMANGALAM - 87</option><option value="S1146">KOTTAKKAL - 46</option><option value="S11119">KOTTARAKKARA - 119</option><option value="S1197">KOTTAYAM - 97</option><option value="S11139">KOVALAM - 139</option><option value="S1127">KOZHIKODE NORTH - 27</option><option value="S1128">KOZHIKODE SOUTH - 28</option><option value="S11123">KUNDARA - 123</option><option value="S1130">KUNNAMANGALAM - 30</option><option value="S1162">KUNNAMKULAM - 62</option><option value="S1184">KUNNATHUNAD  - 84</option><option value="S11118">KUNNATHUR  - 118</option><option value="S1114">KUTHUPARAMBA - 14</option><option value="S11106">KUTTANAD - 106</option><option value="S1121">KUTTIADI - 21</option><option value="S1155">MALAMPUZHA - 55</option><option value="S1140">MALAPPURAM - 40</option><option value="S1164">MANALUR - 64</option><option value="S1117">MANANTHAVADY - 17</option><option value="S1137">MANJERI - 37</option><option value="S111">MANJESHWAR - 1</option><option value="S1139">MANKADA - 39</option><option value="S1154">MANNARKKAD - 54</option><option value="S1115">MATTANNUR - 15</option><option value="S11109">MAVELIKKARA  - 109</option><option value="S1186">MUVATTUPUZHA - 86</option><option value="S1122">NADAPURAM - 22</option><option value="S1168">NATTIKA - 68</option><option value="S11130">NEDUMANGAD - 130</option><option value="S1159">NEMMARA - 59</option><option value="S11135">NEMOM - 135</option><option value="S11140">NEYYATTINKARA - 140</option><option value="S1135">NILAMBUR - 35</option><option value="S1166">OLLUR - 66</option><option value="S1152">OTTAPPALAM - 52</option><option value="S1193">PALA - 93</option><option value="S1156">PALAKKAD - 56</option><option value="S11137">PARASSALA - 137</option><option value="S1178">PARAVUR - 78</option><option value="S11120">PATHANAPURAM - 120</option><option value="S1150">PATTAMBI - 50</option><option value="S116">PAYYANNUR - 6</option><option value="S1192">PEERUMADE - 92</option><option value="S1124">PERAMBRA - 24</option><option value="S1116">PERAVOOR - 16</option><option value="S1138">PERINTHALMANNA - 38</option><option value="S1174">PERUMBAVOOR - 74</option><option value="S1185">PIRAVOM - 85</option><option value="S1148">PONNANI - 48</option><option value="S11101">POONJAR - 101</option><option value="S1171">PUDUKKAD - 71</option><option value="S11121">PUNALUR - 121</option><option value="S1198">PUTHUPPALLY - 98</option><option value="S1123">QUILANDY - 23</option><option value="S11112">RANNI - 112</option><option value="S1151">SHORNUR - 51</option><option value="S1118">SULTHANBATHERY - 18</option><option value="S118">TALIPARAMBA - 8</option><option value="S1144">TANUR - 44</option><option value="S1157">TARUR - 57</option><option value="S1113">THALASSERY - 13</option><option value="S1147">THAVANUR - 47</option><option value="S11111">THIRUVALLA - 111</option><option value="S1132">THIRUVAMBADI - 32</option><option value="S11134">THIRUVANANTHAPURAM - 134</option><option value="S1190">THODUPUZHA - 90</option><option value="S1183">THRIKKAKARA - 83</option><option value="S1181">THRIPUNITHURA - 81</option><option value="S1167">THRISSUR - 67</option><option value="S1149">THRITHALA - 49</option><option value="S1145">TIRUR - 45</option><option value="S1143">TIRURANGADI - 43</option><option value="S115">TRIKARIPUR - 5</option><option value="S113">UDMA - 3</option><option value="S1189">UDUMBANCHOLA - 89</option><option value="S1120">VADAKARA - 20</option><option value="S1195">VAIKOM - 95</option><option value="S1142">VALLIKUNNU - 42</option><option value="S11131">VAMANAPURAM - 131</option><option value="S11127">VARKALA - 127</option><option value="S11133">VATTIYOORKAVU - 133</option><option value="S1141">VENGARA - 41</option><option value="S1179">VYPEN - 79</option><option value="S1165">WADAKKANCHERY - 65</option><option value="S1136">WANDOOR - 36</option></select>"""


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