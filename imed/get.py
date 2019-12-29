import re
import shutil
from concurrent.futures.thread import ThreadPoolExecutor

import pymongo
import requests
from bs4 import BeautifulSoup

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
general = db['general']
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
Company = companyDB.find({"start": {"$ne": -1}})
Company = list(Company)
Company = Company[start:]

row = 1
row_irc = 1


# for company in Company[start:]:
def get_company(company):
    # sleep(CompanyList.index(company) / 100 + 10)
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
    try:
        response = session.post(url=url, data=item_request_body)
    except:
        return get_company(company)

    timeout = re.findall('''( Timeout)''', response.text)
    if len(timeout) != 0:
        print(timeout)
        return get_company(company)

    noRecord = re.findall('''(No records to display)''', response.text)
    if len(noRecord) != 0:
        print('no data')
        companyDB.delete_one({"_id": company['_id']})
        return repeat()

    list_0 = re.findall(r'''RadGrid1_ctl00__(.*\n\s.*)type="button"\sname="(.*?)" value=((.*\n*\s*\d*)*?)</tr''',
                        response.text)

    # print('start l_1')
    # uCompany = companyDB.find_one({"_id": company['_id']})
    # print(uCompany)
    sortProduct = []
    indexRepeat = []
    for obj in list_0:
        fields = re.findall(
            r'''</td><td>(.*?)</td><td><a title="(.*)\s?">(.*?)\s?</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>''',
            obj[2])[0]

        product = {
            "company": company['name'], "faName": fields[0], "enName": fields[2], "category": fields[3],
            "UMDNS": fields[4], "manuName": fields[5], "countryLegal": fields[6], "eqType": fields[7],
        }

        if str(product) in sortProduct:
            indexRepeat.append(obj)
        else:
            sortProduct.append(str(product))

    print("products: ", len(list_0))
    for i in indexRepeat:
        list_0.remove(i)
    print("unique products: ", len(list_0))
    endPoint = 0

    for item in list_0:
        number = re.findall(r'''/></td><td>\s*(\d*)''', item[2])[0]

        # if company['start'] != -1 & list_0.index(item) + 1 >= int(uCompany['start']):
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

        try:
            level_1 = session.post(url=url, headers=headers, data=params, cookies=response.request._cookies)
        except:
            return get_company(company)

        timeout = re.findall('''( Timeout)''', level_1.text)
        if len(timeout) != 0:
            return get_company(company)

        models = re.findall(r'''RadGrid1_ctl00_ctl\d*_Detail\d*__\d*:((.*?\n*?\s*?)*)</tr''', level_1.text)

        viewstate_2 = re.findall(r'''__VIEWSTATE(.*)hiddenField''', level_1.text)
        # ..................... END LEVEL ONE ........................... #`
        print('start l_2')
        # ..................... START LEVEL TWO ........................... #
        model_list = []
        enName = fields[2]
        insertProduct = general.find_one({"company": company['name'], "enName": fields[2]})
        if not insertProduct:
            general.insert_one(product)
            insertProduct = general.find_one({"company": company['name'], "enName": fields[2]})

        modelCount = len(insertProduct["models"])
        for model in models:
            endPoint += 1
            links = re.findall(r'''&#39;(.*?)&#39''', model[0])
            regField = model[0].replace('\n', '')
            fields = re.findall(
                r'''px;">(.*?\n*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(\d*)</td>''',
                regField)[0]
            model_obj = {
                "Model": fields[0], "RegBrand": fields[1], "manuNameOEM": fields[2], "countryOEM": fields[3],
                "cmp_name": fields[4], "cmp_Code": fields[5]
            }
            currentModel = general.find_one(
                {"company": company['name'], "enName": enName, "models": {"$elemMatch": model_obj}})
            # print(currentModel)
            if not currentModel:
                cookies = dict(
                    cookies_are='Cookie: cookiesession1=0A000F8F2GV8JEA8ACKV80HUYFMM018E; ASP.NET_SessionId=maycwqxponc12zbexfskfg3q')
                params = {
                    "ctl00$MainContent$ScriptManager1": "ctl00$MainContent$ctl00$MainContent$RadGrid1Panel|ctl00$MainContent$RadGrid1$ctl00$ctl06$Detail10$ctl04$LinkButton1",
                    "ctl00_MainContent_ScriptManager1_TSM": ";;AjaxControlToolkit, Version=4.1.60919.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:ee051b62-9cd6-49a5-87bb-93c07bc43d63:ea597d4b:b25378d2;Telerik.Web.UI, Version=2016.2.504.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92:en-US:5e8fbefe-888b-4407-b221-396581adc527:16e4e7cd:ed16cbdc:33715776:58366029;",
                    "ctl00$MainContent$txt_asker": "",
                    "ctl00$MainContent$txt_kala": "",
                    "ctl00$MainContent$Drp_CompanyType": "",
                    "ctl00$MainContent$txt_UMDNS": "",
                    "ctl00$MainContent$txtIRC": "",
                    "ctl00$MainContent$txtVerifyCode": "",
                    "ctl00_MainContent_RadGrid1_ClientState": "",
                    "ctl00$MainContent$Drp_UMDNSGroup1": "",
                    "ctl00$MainContent$Drp_UMDNSGroup2": "",
                    "__EVENTTARGET": links[0],
                    "__EVENTARGUMENT": "",
                    "__LASTFOCUS": "",
                    "__VIEWSTATE": viewstate_2[0][1:-3],
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
                try:
                    level_2 = session.post(url=url, headers=headers, data=params, cookies=cookies)
                except:
                    return get_company(company)
                timeout = re.findall('''( Timeout)''', level_2.text)
                if len(timeout) != 0:
                    return get_company(company)

                ID = re.findall(r'''id%3d(.*)%2''', level_2.text)
                # ..................... ENd LEVEL TWO ........................... #
                modelCount += 1
                print('Start L_3', modelCount)
                # ..................... START LEVEL THREE ........................... #
                url_2 = ["http://report.imed.ir/Additionals/Additionals_UMDNSGroupCodeDetails.aspx?id=", ID[0], '=']
                url_2_irc = ["http://report.imed.ir/Additionals/Additionals_IRCList.aspx?id=", ID[0], '=']
                header = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3   ",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
                    "Connection": "keep-alive",
                    "Cookie": "cookiesession1=5B6DD9C3ATAASTC3NCUJHCRKG4OD8217; ASP.NET_SessionId=siujuktfflnenee5ny4peaqn",
                    "Referer": "http://report.imed.ir/Additionals/Reg_qualityconfirmedreport.aspx",
                    "Host": "report.imed.ir",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                }
                try:
                    level_3 = session.get(''.join(url_2), headers=header, )
                except:
                    return get_company(company)

                timeout = re.findall('''( Timeout)''', level_3.text)
                if len(timeout) != 0:
                    return get_company(company)

                try:
                    level_3_irc = session.get(''.join(url_2_irc), headers=header, )
                except:
                    return get_company(company)
                timeout = re.findall('''( Timeout)''', level_3_irc.text)
                if len(timeout) != 0:
                    return get_company(company)

                FANI = {}
                FaName = re.findall(r'''lbl_Kala">(.*)</span>''', level_3.text)
                EnName = re.findall(r'''lblDeviceNameEn">(.*)</span>''', level_3.text)
                Describe = re.findall(r'''lblDeviceDesc">(.*)</span>''', level_3.text)
                UMDNS = re.findall(r'''lblUMDNS">(.*)</span>''', level_3.text)
                Legal = re.findall(r'''Control_lbl_Legal">(.*)</span>''', level_3.text)
                Country_Legal = re.findall(r'''lbl_Country_Legal">(.*)</span>''', level_3.text)
                OEM = re.findall(r'''Control_trOEM">(.*)</span>''', level_3.text)
                Model = re.findall(r'''lbl_Model">(.*)</span>''', level_3.text)
                companyType = re.findall(r'''lbl_companyType">(.*)</span>''', level_3.text)
                Foriati = re.findall(r'''lbl_Foriati">(.*)</span>''', level_3.text)
                Unit = re.findall(r'''lbl_Unit">(.*)</span>''', level_3.text)
                Usability = re.findall(r'''lbl_Usability">(.*)</span>''', level_3.text)
                CommonName = re.findall(r'''lbl_CommonName">(.*)</span>''', level_3.text)
                LableName = re.findall(r'''lbl_LableName">(.*)</span>''', level_3.text)
                Brand = re.findall(r'''lbl_Brand">(.*)</span>''', level_3.text)
                RegCode = re.findall(r'''lbl_RegCode">(.*)</span>''', level_3.text)
                Catalog = re.findall(r'''lbl_Catalog">(.*)</span>''', level_3.text)
                FANI['عمومی'] = {}
                if FaName:
                    FANI['عمومی']['FaName'] = FaName[0]
                if EnName:
                    FANI['عمومی']['EnName'] = EnName[0]
                if Describe:
                    FANI['عمومی']['Describe'] = Describe[0]
                if UMDNS:
                    FANI['عمومی']['UMDNS'] = UMDNS[0]
                if Legal:
                    FANI['عمومی']['Legal'] = Legal[0]
                if Country_Legal:
                    FANI['عمومی']['Country_Legal'] = Country_Legal[0]
                if OEM:
                    FANI['عمومی']['OEM'] = OEM[0]
                if Model:
                    FANI['عمومی']['Model'] = Model[0]
                if companyType:
                    FANI['عمومی']['companyType'] = companyType[0]
                if Foriati:
                    FANI['عمومی']['Foriati'] = Foriati[0]
                if Unit:
                    FANI['عمومی']['Unit'] = Unit[0]
                if Usability:
                    FANI['عمومی']['Usability'] = Usability[0]
                if CommonName:
                    FANI['عمومی']['CommonName'] = CommonName[0]
                if LableName:
                    FANI['عمومی']['LableName'] = LableName[0]
                if Brand:
                    FANI['عمومی']['Brand'] = Brand[0]
                if RegCode:
                    FANI['عمومی']['RegCode'] = RegCode[0]
                if Catalog:
                    FANI['عمومی']['Catalog'] = Catalog[0]

                Text = re.findall(r'''Red;">(.*?)</span>(.*)([</\w>\s="%:,)(~.\+-]*)style''', level_3.text)
                if Text:
                    for obj in Text:
                        Char = re.findall(r'''AllControl[\w\d]*">(.*?):?</span>''', obj[1])
                        object = {}
                        for i in range(1, int((len(Char) + 2) / 2)):
                            key = Char[(i * 2) - 2].replace('.', '')
                            object[key] = Char[(i * 2) - 1]
                        FANI[obj[0]] = object
                level_3_irc = level_3_irc.text.replace('\r\n', '')
                IRC_GTIN = re.findall(
                    r'''</td><td>(.*)</td><td><a title="([\s\S]*?)">([\s\S]*?)</a></td><td>([\s\S]*?)</td><td>([\s\S]*?)</td>''',
                    level_3_irc)
                # temp = re.findall(
                #     r'''</td><td>(.*)</td><td><a title="(.*)">(.*)</a></td><td>(.*)\n</td><td>(.*)</td>''',
                #     level_3_irc.text)
                # print(temp)
                # for irc_gtin in temp:
                #     IRC_GTIN.append(irc_gtin)

                IRC_list = []
                if IRC_GTIN:
                    for irc in IRC_GTIN:
                        obj = {"IRC": irc[0], "DescriptionFa": irc[1], "Description": irc[3], "GTIN": irc[4]}
                        IRC_list.append(obj)

                model_obj['FANI'] = FANI
                model_obj['IRCs'] = IRC_list
                model_list.append(model_obj)
                general.update_one({"_id": insertProduct['_id']}, {"$push": {"models": model_obj}})
        # product['models'] = model_list
        # general.insert_one(product)
        companyDB.update_one({"_id": company['_id']}, {"$set": {"start": int(number)}})
    if endPoint > 0:
        companyDB.update_one({"_id": company['_id']}, {"$set": {"start": -1}})
    return repeat()


def repeat():
    # select = Company[0:2][0]
    select = Company[0:1]
    for com in select:
        Company.remove(com)
    # get_company(select)
    with ThreadPoolExecutor(max_workers=500) as pool:
        pool.map(get_company, select)


repeat()
