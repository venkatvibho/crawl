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
STNAME = "WESTBENGAL"

stateassemblies = """<select class="custom-select" id="ctl00_ContentPlaceHolder1_Result1_ddlState" onchange="return GetResult(this)" name="state" style="float: right;"> <option value=""> Select Constituency </option><option value="S2512">ALIPURDUARS - 12</option><option value="S25102">AMDANGA - 102</option><option value="S25181">AMTA - 181</option><option value="S25200">ARAMBAG - 200</option><option value="S25280">ASANSOL DAKSHIN - 280</option><option value="S25281">ASANSOL UTTAR - 281</option><option value="S25101">ASHOKNAGAR - 101</option><option value="S25273">AUSGRAM - 273</option><option value="S2599">BADURIA - 99</option><option value="S2594">BAGDA - 94</option><option value="S25240">BAGHMUNDI - 240</option><option value="S25180">BAGNAN - 180</option><option value="S2572">BAHARAMPUR - 72</option><option value="S2554">BAISNABNAGAR - 54</option><option value="S25191">BALAGARH - 191</option><option value="S25239">BALARAMPUR - 239</option><option value="S25169">BALLY - 169</option><option value="S25161">BALLYGUNGE - 161</option><option value="S2539">BALURGHAT - 39</option><option value="S25238">BANDWAN - 238</option><option value="S2596">BANGAON DAKSHIN - 96</option><option value="S2595">BANGAON UTTAR - 95</option><option value="S25252">BANKURA - 252</option><option value="S25283">BARABANI - 283</option><option value="S25113">BARANAGAR - 113</option><option value="S25119">BARASAT - 119</option><option value="S25260">BARDHAMAN DAKSHIN - 260</option><option value="S25266">BARDHAMAN UTTAR - 266</option><option value="S25253">BARJORA - 253</option><option value="S25108">BARRACKPUR - 108</option><option value="S25140">BARUIPUR PASCHIM - 140</option><option value="S25137">BARUIPUR PURBA - 137</option><option value="S25128">BASANTI - 128</option><option value="S25124">BASIRHAT DAKSHIN - 124</option><option value="S25125">BASIRHAT UTTAR - 125</option><option value="S25154">BEHALA PASCHIM - 154</option><option value="S25153">BEHALA PURBA - 153</option><option value="S2571">BELDANGA - 71</option><option value="S25164">BELEGHATA - 164</option><option value="S25159">BHABANIPUR - 159</option><option value="S25214">BHAGABANPUR - 214</option><option value="S2562">BHAGAWANGOLA - 62</option><option value="S25148">BHANGAR - 148</option><option value="S2569">BHARATPUR - 69</option><option value="S25267">BHATAR - 267</option><option value="S25105">BHATPARA - 105</option><option value="S25116">BIDHANNAGAR - 116</option><option value="S25103">BIJPUR - 103</option><option value="S25237">BINPUR - 237</option><option value="S25146">BISHNUPUR - 146</option><option value="S25255">BISHNUPUR - 255</option><option value="S25286">BOLPUR - 286</option><option value="S25156">BUDGE BUDGE - 156</option><option value="S2567">BURWAN - 67</option><option value="S25138">CANNING PASCHIM - 138</option><option value="S25139">CANNING PURBA - 139</option><option value="S2591">CHAKDAHA - 91</option><option value="S2531">CHAKULIA - 31</option><option value="S25187">CHAMPDANI - 187</option><option value="S2545">CHANCHAL - 45</option><option value="S25189">CHANDANNAGAR - 189</option><option value="S25211">CHANDIPUR - 211</option><option value="S25194">CHANDITALA - 194</option><option value="S25232">CHANDRAKONA - 232</option><option value="S2582">CHAPRA - 82</option><option value="S25248">CHHATNA - 248</option><option value="S2528">CHOPRA - 28</option><option value="S25162">CHOWRANGEE - 162</option><option value="S25190">CHUNCHURA - 190</option><option value="S254">COOCHBEHAR DAKSHIN - 4</option><option value="S253">COOCHBEHAR UTTAR - 3</option><option value="S2519">DABGRAM-FULBARI - 19</option><option value="S25219">DANTAN - 219</option><option value="S2523">DARJEELING - 23</option><option value="S25230">DASPUR - 230</option><option value="S25229">DEBRA - 229</option><option value="S25120">DEGANGA - 120</option><option value="S25197">DHANEKHALI - 197</option><option value="S2515">DHUPGURI - 15</option><option value="S25143">DIAMOND HARBOUR - 143</option><option value="S257">DINHATA - 7</option><option value="S25184">DOMJUR - 184</option><option value="S2575">DOMKAL - 75</option><option value="S25284">DUBRAJPUR - 284</option><option value="S25114">DUM DUM - 114</option><option value="S25110">DUM DUM UTTAR - 110</option><option value="S25277">DURGAPUR PASCHIM - 277</option><option value="S25276">DURGAPUR PURBA - 276</option><option value="S25218">EGRA - 218</option><option value="S2551">ENGLISH BAZAR - 51</option><option value="S25163">ENTALLY - 163</option><option value="S2513">FALAKATA - 13</option><option value="S25144">FALTA - 144</option><option value="S2555">FARAKKA - 55</option><option value="S2597">GAIGHATA - 97</option><option value="S25274">GALSI - 274</option><option value="S2541">GANGARAMPUR - 41</option><option value="S25233">GARBETA - 233</option><option value="S2544">GAZOLE - 44</option><option value="S25231">GHATAL - 231</option><option value="S2530">GOALPOKHAR - 30</option><option value="S25201">GOGHAT - 201</option><option value="S25221">GOPIBALLAVPUR - 221</option><option value="S25127">GOSABA - 127</option><option value="S2543">HABIBPUR - 43</option><option value="S25100">HABRA - 100</option><option value="S25209">HALDIA - 209</option><option value="S25292">HANSAN - 292</option><option value="S2573">HARIHARPARA - 73</option><option value="S2593">HARINGHATA - 93</option><option value="S25196">HARIPAL - 196</option><option value="S2542">HARIRAMPUR - 42</option><option value="S2546">HARISCHANDRAPUR - 46</option><option value="S25121">HAROA - 121</option><option value="S2533">HEMTABAD - 33</option><option value="S25126">HINGALGANJ - 126</option><option value="S25173">HOWRAH DAKSHIN - 173</option><option value="S25171">HOWRAH MADHYA - 171</option><option value="S25170">HOWRAH UTTAR - 170</option><option value="S25257">INDUS - 257</option><option value="S2529">ISLAMPUR - 29</option><option value="S2536">ITAHAR - 36</option><option value="S25150">JADAVPUR - 150</option><option value="S25183">JAGATBALLAVPUR - 183</option><option value="S25106">JAGATDAL - 106</option><option value="S2576">JALANGI - 76</option><option value="S2517">JALPAIGURI - 17</option><option value="S25262">JAMALPUR - 262</option><option value="S25279">JAMURIA - 279</option><option value="S25195">JANGIPARA - 195</option><option value="S2558">JANGIPUR - 58</option><option value="S25136">JAYNAGAR - 136</option><option value="S25222">JHARGRAM - 222</option><option value="S25165">JORASANKO - 165</option><option value="S25241">JOYPUR - 241</option><option value="S25131">KAKDWIP - 131</option><option value="S2511">KALCHINI - 11</option><option value="S2534">KALIAGANJ - 34</option><option value="S2580">KALIGANJ - 80</option><option value="S2522">KALIMPONG - 22</option><option value="S25264">KALNA - 264</option><option value="S2592">KALYANI - 92</option><option value="S25112">KAMARHATI - 112</option><option value="S2568">KANDI - 68</option><option value="S25216">KANTHI DAKSHIN - 216</option><option value="S25213">KANTHI UTTAR - 213</option><option value="S2532">KARANDIGHI - 32</option><option value="S2577">KARIMPUR - 77</option><option value="S25149">KASBA - 149</option><option value="S25244">KASHIPUR - 244</option><option value="S25168">KASHIPUR-BELGACHHIA - 168</option><option value="S25256">KATULPUR - 256</option><option value="S25270">KATWA - 270</option><option value="S25223">KESHIARY - 223</option><option value="S25235">KESHPUR - 235</option><option value="S25271">KETUGRAM - 271</option><option value="S25202">KHANAKUL - 202</option><option value="S25259">KHANDAGHOSH - 259</option><option value="S25228">KHARAGPUR - 228</option><option value="S25224">KHARAGPUR SADAR - 224</option><option value="S25109">KHARDAHA - 109</option><option value="S2566">KHARGRAM - 66</option><option value="S25215">KHEJURI - 215</option><option value="S25158">KOLKATA PORT - 158</option><option value="S2588">KRISHNAGANJ - 88</option><option value="S2585">KRISHNANAGAR DAKSHIN - 85</option><option value="S2583">KRISHNANAGAR UTTAR - 83</option><option value="S25133">KULPI - 133</option><option value="S25129">KULTALI - 129</option><option value="S25282">KULTI - 282</option><option value="S2538">KUMARGANJ - 38</option><option value="S2510">KUMARGRAM - 10</option><option value="S2524">KURSEONG - 24</option><option value="S2537">KUSHMANDI - 37</option><option value="S25288">LABPUR - 288</option><option value="S2561">LALGOLA - 61</option><option value="S2514">MADARIHAT - 14</option><option value="S25118">MADHYAMGRAM - 118</option><option value="S25142">MAGRAHAT PASCHIM - 142</option><option value="S25141">MAGRAHAT PURBA - 141</option><option value="S25155">MAHESHTALA - 155</option><option value="S25208">MAHISADAL - 208</option><option value="S2520">MAL - 20</option><option value="S2547">MALATIPUR - 47</option><option value="S2550">MALDAHA - 50</option><option value="S25243">MANBAZAR - 243</option><option value="S25135">MANDIRBAZAR - 135</option><option value="S25272">MANGALKOT - 272</option><option value="S2549">MANIKCHAK - 49</option><option value="S25167">MANIKTALA - 167</option><option value="S252">MATHABHANGA - 2</option><option value="S2525">MATIGARA-NAXALBARI - 25</option><option value="S2516">MAYNAGURI - 16</option><option value="S25290">MAYURESWAR - 290</option><option value="S25236">MEDINIPUR - 236</option><option value="S251">MEKLIGANJ - 1</option><option value="S25265">MEMARI - 265</option><option value="S25157">METIABURUZ - 157</option><option value="S25122">MINAKHAN - 122</option><option value="S25263">MONTESWAR - 263</option><option value="S2552">MOTHABARI - 52</option><option value="S25206">MOYNA - 206</option><option value="S25294">MURARAI - 294</option><option value="S2564">MURSHIDABAD - 64</option><option value="S2584">NABADWIP - 84</option><option value="S2565">NABAGRAM - 65</option><option value="S2521">NAGRAKATA - 21</option><option value="S25104">NAIHATI - 104</option><option value="S2581">NAKASHIPARA - 81</option><option value="S25293">NALHATI - 293</option><option value="S25207">NANDAKUMAR - 207</option><option value="S25210">NANDIGRAM - 210</option><option value="S25287">NANOOR - 287</option><option value="S25225">NARAYANGARH - 225</option><option value="S258">NATABARI - 8</option><option value="S25220">NAYAGRAM - 220</option><option value="S25107">NOAPARA - 107</option><option value="S2574">NOWDA - 74</option><option value="S25254">ONDA - 254</option><option value="S2579">PALASHIPARA - 79</option><option value="S25175">PANCHLA - 175</option><option value="S25275">PANDABESWAR - 275</option><option value="S25192">PANDUA - 192</option><option value="S25111">PANIHATI - 111</option><option value="S25205">PANSKURA PASCHIM - 205</option><option value="S25204">PANSKURA PURBA - 204</option><option value="S25245">PARA - 245</option><option value="S25212">PATASHPUR - 212</option><option value="S25130">PATHARPRATIMA - 130</option><option value="S2527">PHANSIDEWA - 27</option><option value="S25227">PINGLA - 227</option><option value="S25268">PURBASTHALI DAKSHIN - 268</option><option value="S25269">PURBASTHALI UTTAR - 269</option><option value="S25199">PURSURAH - 199</option><option value="S25242">PURULIA - 242</option><option value="S2559">RAGHUNATHGANJ - 59</option><option value="S25246">RAGHUNATHPUR - 246</option><option value="S25134">RAIDIGHI - 134</option><option value="S2535">RAIGANJ - 35</option><option value="S25261">RAINA - 261</option><option value="S25250">RAIPUR - 250</option><option value="S25117">RAJARHAT  GOPALPUR - 117</option><option value="S25115">RAJARHAT NEW TOWN - 115</option><option value="S2518">RAJGANJ - 18</option><option value="S25217">RAMNAGAR - 217</option><option value="S25291">RAMPURHAT - 291</option><option value="S2590">RANAGHAT DAKSHIN - 90</option><option value="S2587">RANAGHAT UTTAR PASCHIM - 87</option><option value="S2589">RANAGHAT UTTAR PURBA - 89</option><option value="S25249">RANIBANDH - 249</option><option value="S25278">RANIGANJ - 278</option><option value="S2563">RANINAGAR - 63</option><option value="S25160">RASHBEHARI - 160</option><option value="S2548">RATUA - 48</option><option value="S2570">REJINAGAR - 70</option><option value="S25226">SABANG - 226</option><option value="S25132">SAGAR - 132</option><option value="S2560">SAGARDIGHI - 60</option><option value="S25289">SAINTHIA - 289</option><option value="S25234">SALBONI - 234</option><option value="S25247">SALTORA - 247</option><option value="S2556">SAMSERGANJ - 56</option><option value="S25123">SANDESHKHALI - 123</option><option value="S25174">SANKRAIL - 174</option><option value="S2586">SANTIPUR - 86</option><option value="S25193">SAPTAGRAM - 193</option><option value="S25145">SATGACHHIA - 145</option><option value="S25172">SHIBPUR - 172</option><option value="S25166">SHYAMPUKUR - 166</option><option value="S25179">SHYAMPUR - 179</option><option value="S2526">SILIGURI - 26</option><option value="S25188">SINGUR - 188</option><option value="S256">SITAI - 6</option><option value="S255">SITALKUCHI - 5</option><option value="S25258">SONAMUKHI - 258</option><option value="S25147">SONARPUR DAKSHIN - 147</option><option value="S25151">SONARPUR UTTAR - 151</option><option value="S25186">SREERAMPUR - 186</option><option value="S2553">SUJAPUR - 53</option><option value="S25285">SURI - 285</option><option value="S2557">SUTI - 57</option><option value="S2598">SWARUPNAGAR - 98</option><option value="S25251">TALDANGRA - 251</option><option value="S25203">TAMLUK - 203</option><option value="S2540">TAPAN - 40</option><option value="S25198">TARAKESWAR - 198</option><option value="S2578">TEHATTA - 78</option><option value="S25152">TOLLYGANJ - 152</option><option value="S259">TUFANGANJ - 9</option><option value="S25182">UDAYNARAYANPUR - 182</option><option value="S25178">ULUBERIA DAKSHIN - 178</option><option value="S25176">ULUBERIA PURBA - 176</option><option value="S25177">ULUBERIA UTTAR - 177</option><option value="S25185">UTTARPARA - 185</option></select>"""


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