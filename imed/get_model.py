import re
import shutil
from concurrent.futures.thread import ThreadPoolExecutor

import pymongo
import requests
from bs4 import BeautifulSoup

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
general = db['getGeneral']
companyDB = db['company']

url = 'http://report.imed.ir/Additionals/Reg_qualityconfirmedreport.aspx'
session = requests.Session()
page = session.get(url)
soup = BeautifulSoup(page.text, "html.parser")
viewstate = soup.select("#__VIEWSTATE")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']
IMG = session.get('http://report.imed.ir/Piclogin.aspx', stream=True)
with open('imgs.png', 'wb') as out_file:
    shutil.copyfileobj(IMG.raw, out_file)
CaptchaIMG = input('IMG :')

CompanyList = companyDB.find()
CompanyList = list(CompanyList)

start = int(input("start: "))
# end = int(input("end: "))
Company = companyDB.find({})
Company = list(Company)
Company = Company[start:]

row = 1
row_irc = 1


for company in Company:
    print("Company ", CompanyList.index(company))
    item_request_body = {
        "ctl00_MainContent_ScriptManager1_TSM": ";;AjaxControlToolkit,+Version=4.1.60919.0,+Culture=neutral,+PublicKeyToken=28f01b0e84b6d53e:en-US:ee051b62-9cd6-49a5-87bb-93c07bc43d63:ea597d4b:b25378d2;Telerik.Web.UI,+Version=2016.2.504.0,+Culture=neutral,+PublicKeyToken=29ac1a93ec063d92:en-US:5e8fbefe-888b-4407-b221-396581adc527:16e4e7cd:ed16cbdc:33715776:58366029",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATEGENERATOR": "D3644843",
        "__VIEWSTATE": viewstate,
        "ctl00$MainContent$Drp_UMDNSGroup1": "",
        "ctl00$MainContent$Drp_UMDNSGroup2": "",
        "ctl00$MainContent$btn_search": "جستجو",
        "ctl00$MainContent$txt_asker": company['name'],
        "ctl00$MainContent$txtIRC": "",
        "ctl00$MainContent$txtVerifyCode": CaptchaIMG,
        # "__EVENTVALIDATION": eventvalidation
    }
    response = session.post(url=url, data=item_request_body)
    list_0 = re.findall(r'''RadGrid1_ctl00__(.*\n\s.*)type="button"\sname="(.*?)" value=((.*\n*\s*\d*)*?)</tr''',
                        response.text)
    print("products: ", len(list_0))
    endPoint = 0

    for item in list_0:
        number = re.findall(r'''/></td><td>\s*(\d*)''', item[2])[0]
        print(company['name'], number)
        fields = re.findall(
            r'''</td><td>(.*?)</td><td><a title="(.*)\s?">(.*?)\s?</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>''',
            item[2])[0]
        product = {
            "company": company['name'], "faName": fields[0], "enName": fields[2], "category": fields[3],
            "UMDNS": fields[4], "manuName": fields[5], "countryLegal": fields[6], "eqType": fields[7], "models": []
        }
        # ..................... START LEVEL ONE ........................... #
        soup = BeautifulSoup(response.text, "html.parser")
        viewstate_1 = soup.select("#__VIEWSTATE")[0]['value']
        params = {
            "ctl00$MainContent$ScriptManager1": "ctl00$MainContent$ctl00$MainContent$RadGrid1Panel|ctl00$MainContent$RadGrid1$ctl00$ctl04$GECBtnExpandColumn",
            "ctl00_MainContent_ScriptManager1_TSM": ";;AjaxControlToolkit, Version=4.1.60919.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:ee051b62-9cd6-49a5-87bb-93c07bc43d63:ea597d4b:b25378d2;Telerik.Web.UI, Version=2016.2.504.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92:en-US:5e8fbefe-888b-4407-b221-396581adc527:16e4e7cd:ed16cbdc:33715776:58366029;",
            "ctl00$MainContent$txt_kala": "",
            "ctl00$MainContent$Drp_CompanyType": "",
            "ctl00$MainContent$txt_UMDNS": "",
            "ctl00$MainContent$txt_asker": company['name'],
            "ctl00$MainContent$txtIRC": "",
            "ctl00$MainContent$txtVerifyCode": "",
            "ctl00_MainContent_RadGrid1_ClientState": "",
            "ctl00$MainContent$Drp_UMDNSGroup1": "",
            "ctl00$MainContent$Drp_UMDNSGroup2": "",
            "__EVENTTARGET": item[1],
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "__VIEWSTATE": viewstate_1,
            "__ASYNCPOST": "true",
            "__VIEWSTATEGENERATOR": "D3644843",
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "32322",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "cookiesession1=5B6DD9C3ATAASTC3NCUJHCRKG4OD8217; ASP.NET_SessionId=siujuktfflnenee5ny4peaqn",
            "Referer": "http://report.imed.ir/Additionals/Reg_qualityconfirmedreport.aspx",
            "Host": "report.imed.ir",
            "Origin": "http://report.imed.ir",
            "X-MicrosoftAjax": "Delta=true",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        }
        level_1 = session.post(url=url, headers=headers, data=params, cookies=response.request._cookies)
        models = re.findall(r'''RadGrid1_ctl00_ctl\d*_Detail\d*__\d*:((.*?\n*?\s*?)*)</tr''', level_1.text)
        viewstate_2 = re.findall(r'''__VIEWSTATE(.*)hiddenField''', level_1.text)
        # ..................... END LEVEL ONE ........................... #`
        print('start l_2')
        # ..................... START LEVEL TWO ........................... #
        enName = fields[2]
        insertProduct = general.find_one({"company": company['name'], "enName": fields[2]})
        if not insertProduct:
            general.insert_one(product)
            insertProduct = general.find_one({"company": company['name'], "enName": fields[2]})

        modelCount = len(insertProduct["models"])

        for model in models:
            modelCount += 1
            print(modelCount)
            currentModel = general.find(
                {"company": company['name'], "enName": enName, "models": {"$elemMatch": model[0]}})
            if len(list(currentModel)) == 0:
                general.update_one({"_id": insertProduct['_id']}, {"$push": {"models": model[0]}})

