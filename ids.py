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
from bs4 import BeautifulSoup

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

soup3 = BeautifulSoup(stateassemblies, "html.parser")

constIds = []   # array to store results

for option in soup3.find_all("option"):
    constIds.append(option.get("value"))

print(constIds)

stateassemblies2 = """<select id="constId" name="constId" class="form-control">

<option value="102">AMDANGA</option>

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

soup3 = BeautifulSoup(stateassemblies2, "html.parser")

constIds2 = []   # array to store results

for option in soup3.find_all("option"):
    constIds2.append(option.get("value"))

print(constIds2)


print("Phase-1 => ", len(constIds))
print("Phase-2 => ", len(constIds2))
print("TOTAL => ", len(constIds + constIds2))