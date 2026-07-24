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
STNAME = "TAMIL NADU"

stateassemblies = """<select class="custom-select" id="ctl00_ContentPlaceHolder1_Result1_ddlState" onchange="return GetResult(this)" name="state" style="float: right;"> <option value=""> Select Constituency </option><option value="S2228">ALANDUR - 28</option><option value="S22182">ALANGUDI - 182</option><option value="S22223">ALANGULAM - 223</option><option value="S22225">AMBASAMUDRAM - 225</option><option value="S228">AMBATTUR - 8</option><option value="S2248">AMBUR - 48</option><option value="S2244">ANAIKATTU - 44</option><option value="S22198">ANDIPATTI - 198</option><option value="S2221">ANNA NAGAR - 21</option><option value="S22105">ANTHIYUR - 105</option><option value="S2238">ARAKKONAM - 38</option><option value="S2267">ARANI - 67</option><option value="S22183">ARANTHANGI - 183</option><option value="S22134">ARAVAKURICHI - 134</option><option value="S2242">ARCOT - 42</option><option value="S22149">ARIYALUR - 149</option><option value="S22207">ARUPPUKKOTTAI - 207</option><option value="S22129">ATHOOR - 129</option><option value="S2282">ATTUR - 82</option><option value="S226">AVADI - 6</option><option value="S22112">AVANASHI - 112</option><option value="S2252">BARGUR - 52</option><option value="S22104">BHAVANI - 104</option><option value="S22107">BHAVANISAGAR - 107</option><option value="S22157">BHUVANAGIRI - 157</option><option value="S22200">BODINAYAKANUR - 200</option><option value="S2232">CHENGALPATTU - 32</option><option value="S2262">CHENGAM - 62</option><option value="S2219">CHEPAUK-THIRUVALLIKENI - 19</option><option value="S2268">CHEYYAR - 68</option><option value="S2234">CHEYYUR - 34</option><option value="S22158">CHIDAMBARAM - 158</option><option value="S22118">COIMBATORE (NORTH) - 118</option><option value="S22120">COIMBATORE (SOUTH) - 120</option><option value="S22231">COLACHAL - 231</option><option value="S22110">COONOOR - 110</option><option value="S22155">CUDDALORE - 155</option><option value="S22201">CUMBUM - 201</option><option value="S22101">DHARAPURAM - 101</option><option value="S2259">DHARMAPURI - 59</option><option value="S22132">DINDIGUL - 132</option><option value="S2211">DR.RADHAKRISHNAN NAGAR - 11</option><option value="S2286">EDAPPADI - 86</option><option value="S2216">EGMORE - 16</option><option value="S2298">ERODE (EAST) - 98</option><option value="S2299">ERODE (WEST) - 99</option><option value="S22178">GANDHARVAKOTTAI - 178</option><option value="S2281">GANGAVALLI - 81</option><option value="S2270">GINGEE - 70</option><option value="S22106">GOBICHETTIPALAYAM - 106</option><option value="S22109">GUDALUR - 109</option><option value="S2246">GUDIYATTAM - 46</option><option value="S221">GUMMIDIPOONDI - 1</option><option value="S2218">HARBOUR - 18</option><option value="S2261">HARUR - 61</option><option value="S2255">HOSUR - 55</option><option value="S22150">JAYANKONDAM - 150</option><option value="S2249">JOLARPET - 49</option><option value="S22221">KADAYANALLUR - 221</option><option value="S2265">KALASAPAKKAM - 65</option><option value="S2280">KALLAKURICHI - 80</option><option value="S2237">KANCHEEPURAM - 37</option><option value="S22102">KANGAYAM - 102</option><option value="S22229">KANNIYAKUMARI - 229</option><option value="S22184">KARAIKUDI - 184</option><option value="S22135">KARUR - 135</option><option value="S2240">KATPADI - 40</option><option value="S22159">KATTUMANNARKOIL - 159</option><option value="S22117">KAVUNDAMPALAYAM - 117</option><option value="S22234">KILLIYOOR - 234</option><option value="S2264">KILPENNATHUR - 64</option><option value="S2245">KILVAITHINANKUPPAM - 45</option><option value="S22164">KILVELUR - 164</option><option value="S22122">KINATHUKADAVU - 122</option><option value="S2213">KOLATHUR - 13</option><option value="S22218">KOVILPATTI - 218</option><option value="S2253">KRISHNAGIRI - 53</option><option value="S22136">KRISHNARAYAPURAM - 136</option><option value="S22137">KULITHALAI - 137</option><option value="S2297">KUMARAPALAYAM - 97</option><option value="S22171">KUMBAKONAM - 171</option><option value="S22148">KUNNAM - 148</option><option value="S22156">KURINJIPADI - 156</option><option value="S22143">LALGUDI - 143</option><option value="S22126">MADATHUKULAM - 126</option><option value="S229">MADAVARAM - 9</option><option value="S22193">MADURAI CENTRAL - 193</option><option value="S22189">MADURAI EAST - 189</option><option value="S22191">MADURAI NORTH - 191</option><option value="S22192">MADURAI SOUTH - 192</option><option value="S22194">MADURAI WEST - 194</option><option value="S2235">MADURANTAKAM - 35</option><option value="S227">MADURAVOYAL - 7</option><option value="S2271">MAILAM - 71</option><option value="S22144">MANACHANALLUR - 144</option><option value="S22187">MANAMADURAI - 187</option><option value="S22138">MANAPPARAI - 138</option><option value="S22167">MANNARGUDI - 167</option><option value="S22161">MAYILADUTHURAI - 161</option><option value="S22188">MELUR - 188</option><option value="S22111">METTUPPALAYAM - 111</option><option value="S2285">METTUR - 85</option><option value="S22100">MODAKKURICHI - 100</option><option value="S22212">MUDHUKULATHUR - 212</option><option value="S22145">MUSIRI - 145</option><option value="S2225">MYLAPORE - 25</option><option value="S22163">NAGAPATTINAM - 163</option><option value="S22230">NAGERCOIL - 230</option><option value="S2294">NAMAKKAL - 94</option><option value="S22227">NANGUNERI - 227</option><option value="S22169">NANNILAM - 169</option><option value="S22131">NATHAM - 131</option><option value="S22153">NEYVELI - 153</option><option value="S22130">NILAKKOTTAI - 130</option><option value="S22128">ODDANCHATRAM - 128</option><option value="S2284">OMALUR - 84</option><option value="S22175">ORATHANADU - 175</option><option value="S22217">OTTAPIDARAM - 217</option><option value="S22232">PADMANABHAPURAM - 232</option><option value="S2257">PALACODU - 57</option><option value="S22127">PALANI - 127</option><option value="S22226">PALAYAMKOTTAI - 226</option><option value="S22115">PALLADAM - 115</option><option value="S2230">PALLAVARAM - 30</option><option value="S22154">PANRUTI - 154</option><option value="S22172">PAPANASAM - 172</option><option value="S2260">PAPPIREDDIPATTI - 60</option><option value="S22209">PARAMAKUDI - 209</option><option value="S2295">PARAMATHI-VELUR - 95</option><option value="S22176">PATTUKKOTTAI - 176</option><option value="S2258">PENNAGARAM - 58</option><option value="S22147">PERAMBALUR - 147</option><option value="S2212">PERAMBUR - 12</option><option value="S22177">PERAVURANI - 177</option><option value="S22199">PERIYAKULAM - 199</option><option value="S22103">PERUNDURAI - 103</option><option value="S22123">POLLACHI - 123</option><option value="S2266">POLUR - 66</option><option value="S222">PONNERI - 2</option><option value="S22162">POOMPUHAR - 162</option><option value="S225">POONAMALLEE - 5</option><option value="S22180">PUDUKKOTTAI - 180</option><option value="S22228">RADHAPURAM - 228</option><option value="S22202">RAJAPALAYAM - 202</option><option value="S22211">RAMANATHAPURAM - 211</option><option value="S2241">RANIPET - 41</option><option value="S2292">RASIPURAM - 92</option><option value="S2278">RISHIVANDIYAM - 78</option><option value="S2217">ROYAPURAM - 17</option><option value="S2223">SAIDAPET - 23</option><option value="S2289">SALEM (NORTH) - 89</option><option value="S2290">SALEM (SOUTH) - 90</option><option value="S2288">SALEM (WEST) - 88</option><option value="S22219">SANKARANKOVIL - 219</option><option value="S2279">SANKARAPURAM - 79</option><option value="S2287">SANKARI - 87</option><option value="S22204">SATTUR - 204</option><option value="S2293">SENTHAMANGALAM - 93</option><option value="S22190">SHOLAVANDAN - 190</option><option value="S2239">SHOLINGUR - 39</option><option value="S2227">SHOZHINGANALLUR - 27</option><option value="S22121">SINGANALLUR - 121</option><option value="S22160">SIRKAZHI - 160</option><option value="S22186">SIVAGANGA - 186</option><option value="S22205">SIVAKASI - 205</option><option value="S2229">SRIPERUMBUDUR - 29</option><option value="S22139">SRIRANGAM - 139</option><option value="S22216">SRIVAIKUNTAM - 216</option><option value="S22203">SRIVILLIPUTHUR - 203</option><option value="S22116">SULUR - 116</option><option value="S2231">TAMBARAM - 31</option><option value="S22222">TENKASI - 222</option><option value="S2256">THALLI - 56</option><option value="S22174">THANJAVUR - 174</option><option value="S2215">THIRU-VI-KA-NAGAR - 15</option><option value="S22196">THIRUMANGALAM - 196</option><option value="S22181">THIRUMAYAM - 181</option><option value="S22195">THIRUPARANKUNDRAM - 195</option><option value="S2233">THIRUPORUR - 33</option><option value="S22166">THIRUTHURAIPOONDI - 166</option><option value="S22173">THIRUVAIYARU - 173</option><option value="S224">THIRUVALLUR - 4</option><option value="S22168">THIRUVARUR - 168</option><option value="S22142">THIRUVERUMBUR - 142</option><option value="S22170">THIRUVIDAIMARUDUR - 170</option><option value="S2210">THIRUVOTTIYUR - 10</option><option value="S2224">THIYAGARAYANAGAR - 24</option><option value="S22119">THONDAMUTHUR - 119</option><option value="S22214">THOOTHUKKUDI - 214</option><option value="S2220">THOUSAND LIGHTS - 20</option><option value="S22146">THURAIYUR - 146</option><option value="S2272">TINDIVANAM - 72</option><option value="S22215">TIRUCHENDUR - 215</option><option value="S2296">TIRUCHENGODU - 96</option><option value="S22141">TIRUCHIRAPPALLI (EAST) - 141</option><option value="S22140">TIRUCHIRAPPALLI (WEST) - 140</option><option value="S22208">TIRUCHULI - 208</option><option value="S2276">TIRUKKOYILUR - 76</option><option value="S22224">TIRUNELVELI - 224</option><option value="S2250">TIRUPPATTUR - 50</option><option value="S22185">TIRUPPATTUR - 185</option><option value="S22113">TIRUPPUR (NORTH) - 113</option><option value="S22114">TIRUPPUR (SOUTH) - 114</option><option value="S223">TIRUTTANI - 3</option><option value="S22210">TIRUVADANAI - 210</option><option value="S2263">TIRUVANNAMALAI - 63</option><option value="S22151">TITTAKUDI - 151</option><option value="S22108">UDHAGAMANDALAM - 108</option><option value="S22125">UDUMALAIPETTAI - 125</option><option value="S2277">ULUNDURPETTAI - 77</option><option value="S22197">USILAMPATTI - 197</option><option value="S2251">UTHANGARAI - 51</option><option value="S2236">UTHIRAMERUR - 36</option><option value="S22124">VALPARAI - 124</option><option value="S2269">VANDAVASI - 69</option><option value="S2247">VANIYAMBADI - 47</option><option value="S2273">VANUR - 73</option><option value="S22220">VASUDEVANALLUR - 220</option><option value="S22165">VEDARANYAM - 165</option><option value="S22133">VEDASANDUR - 133</option><option value="S2291">VEERAPANDI - 91</option><option value="S2226">VELACHERY - 26</option><option value="S2243">VELLORE - 43</option><option value="S2254">VEPPANAHALLI - 54</option><option value="S2275">VIKRAVANDI - 75</option><option value="S22213">VILATHIKULAM - 213</option><option value="S22233">VILAVANCODE - 233</option><option value="S2214">VILLIVAKKAM - 14</option><option value="S2274">VILUPPURAM - 74</option><option value="S22179">VIRALIMALAI - 179</option><option value="S22206">VIRUDHUNAGAR - 206</option><option value="S2222">VIRUGAMPAKKAM - 22</option><option value="S22152">VRIDDHACHALAM - 152</option><option value="S2283">YERCAUD - 83</option></select>"""


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