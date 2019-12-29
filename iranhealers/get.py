import re

import requests
import xlsxwriter
from bs4 import BeautifulSoup

wb = xlsxwriter.Workbook("export.xlsx")
general = wb.add_worksheet()

headers = {
    "Host": "www.iranhealers.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.2",
    # "If-Modified-Since": "Mon, 03 Oct 2005 03:10:34 GMT",
    "Cache-Control": "max-age=0",
}
rowCount = 0
one = int(input("page: "))
two = int(input("item: "))
for number in range(one, 23):
    for item in range(two, 1000):
        print(number, item)
        if item == 0:
            level0ne = requests.get('http://www.iranhealers.com/drug/f{}.htm'.format(number), headers=headers)
        else:
            level0ne = requests.get('http://www.iranhealers.com/drug/f{}_{}.htm'.format(number, item), headers=headers)
        level0ne.encoding = level0ne.apparent_encoding
        level0ne = level0ne.text.replace(u'\u200c', ' ')
        level0ne = level0ne.replace('\n', ' ')
        level0ne = level0ne.replace('  ', ' ')
        level0ne = level0ne.replace('  ', ' ')
        level0ne = level0ne.replace(' ،', '،')
        level0ne = level0ne.replace(' :', ':')
        level0ne = level0ne.replace('#top]', '#top')
        level0ne = level0ne.replace('<o:p></o:p></a>', '')
        level0ne = level0ne.replace('بزرگسالان:', 'بزرگسالان')
        level0ne = level0ne.replace('كودكان:', 'كودكان')
        level0ne = level0ne.replace('سال:', 'سال')
        level0ne = level0ne.replace('اطفال:', 'اطفال')
        level0ne = level0ne.replace('بزرگسالان واكسينه نشده:', 'بزرگسالان واكسينه نشده')
        level0ne = level0ne.replace('بزرگسالان با واكسيناسيون ناقص:', 'بزرگسالان با واكسيناسيون ناقص')
        level0ne = level0ne.replace('واكسيناسيون اوليه:', 'واكسيناسيون اوليه')
        level0ne = level0ne.replace('در كودكان واكسينه نشده:', 'در كودكان واكسينه نشده')
        level0ne = level0ne.replace('بايد با احتياطمصرف شود:', 'بايد با احتياط مصرف شود؛')
        level0ne = level0ne.replace('عبارتنداز:', 'عبارتنداز')
        level0ne = level0ne.replace('خوراكي:', 'خوراكي؛')
        level0ne = level0ne.replace('تزريقي:', 'تزريقي؛')
        level0ne = level0ne.replace('است:', 'است؛')
        level0ne = level0ne.replace('مسهل:', 'مسهل؛')
        level0ne = level0ne.replace('موضعي:', 'موضعي؛')
        level0ne = level0ne.replace('واژينال:', 'واژينال؛')
        level0ne = level0ne.replace('مكانيسم  اثر:', 'مكانيسم اثر:')
        level0ne = level0ne.replace('عوارض  جانبي:', 'عوارض جانبي:')
        level0ne = level0ne.replace('اشكال  دارويي:', 'اشكال دارويي:')
        level0ne = level0ne.replace('نكات  قابل توصيه:', 'نكات قابل توصيه:')
        level0ne = level0ne.replace('تداخل هاي  دارويي:', 'تداخل هاي دارويي:')
        level0ne = level0ne.replace('به عنوان دهان شويه:', 'به عنوان دهان شويه')

        end = re.findall('''<p>Access to this resource on the server is denied!</p>''', level0ne)
        if end and item != 0:
            break

        soup = BeautifulSoup(level0ne, 'html.parser')
        Content = soup.find('div', attrs={'class': 'Section1'})
        if Content:
            rows = Content.findAll('p', attrs={'class': 'MsoPlainText'})
            count = 0
            drugs = []
            drug = []
            rowCheck = 0
            for row in rows:
                rowCheck += 1
                top = re.findall('href="#top"', str(row.contents))
                if top:
                    if len(drug) > 0:
                        drugs.append(drug)
                    span = row.findAll('span')
                    for s in span:
                        drug = [s.contents]
                    count += 1
                if count > 0:
                    span = row.findAll('span')
                    for s in span:
                        if len(s.contents):
                            if '<span lang="AR-SA' in str(s.contents):
                                spanC = s.findAll('span')
                            else:
                                drug.append(s.contents)
                if rowCheck == len(rows):
                    drugs.append(drug)

            for items in drugs:
                for obj in items:
                    if 'if !supportEmptyParas' in obj:
                        items.remove(obj)
                for obj in items:
                    if ':' in obj:
                        items.remove(obj)
                # for obj in items:
                #     if obj == [':']:
                #         items.remove(obj)
                # for obj in items:
                #     if obj == [':']:
                #         items.remove(obj)
                for obj in items:
                    if len(obj) > 0 and '<a href="javascript' in str(obj[0]):
                        items.remove(obj)
                for obj in items:
                    if '\x8a' in obj:
                        items.remove(obj)
                for obj in items:
                    if '\x8a400' in obj:
                        items.remove(obj)
                for obj in items:
                    if '\x8a40' in obj:
                        items.remove(obj)
                for obj in items:
                    if '\xa0' in obj:
                        items.remove(obj)
                for obj in items:
                    for sub in obj:
                        if str(sub) == "<o:p></o:p>":
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == " ":
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span dir="RTL"></span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span dir="LTR"></span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes"> </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">  </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">  </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">   </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">       </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">     </span>''':
                            obj.remove(sub)
                for obj in items:
                    for sub in obj:
                        if str(sub) == '''<span style="mso-spacerun: yes">      </span>''':
                            obj.remove(sub)

                drugText = []
                nameDrug = re.findall('''">([\s\S]*)</a>''', ''.join(str(items[1])))
                print(nameDrug)
                # print(items[0:2])
                for text in items[2:]:
                    drugText.append(''.join(text))
                drugText = re.sub('[a-z\d]:', '', ' '.join(drugText))
                if drugText.find('مقدار مصرف:') == -1:
                    drugText = drugText.replace('مقدار مصرف ', 'مقدار مصرف:', 1)

                print(drugText)
                cleanObj = {
                    "موارد مصرف": 11, "مكانيسم اثر": 12, "موارد منع مصرف": 15, "فارماكوكينتيك": 14, "فارماكوكنتيك": 14, "هشدارها": 8,
                    "عوارض جانبي": 12, "تداخل هاي دارويي": 17, "نكات قابل توصيه": 16, "مقدار مصرف": 11,
                    "اشكال دارويي": 13, "اجزاء فرآورده ها": 17, "اجزاء فراورده ها": 17,
                    "اجزاء فرآورده": 15, "تداخل دارويي": 13
                }


                # print(' '.join(drugText))

                def check(object):
                    response = ''
                    for item in cleanObj:
                        if len(object) > 0 and item in object[0][-20:]:
                            # print(object[0][0:-cleanObj[item]])
                            response = object[0][0:-cleanObj[item]]
                            break
                    return response


                uses = re.findall('''(موارد مصرف:.*?):''', drugText)
                mechanism = re.findall('''(مكانيسم اثر:.*?):''', drugText)
                contraindication = re.findall('''(موارد منع مصرف:.*?):''', drugText)
                if len(contraindication) == 0:
                    contraindication = re.findall('''(منع مصرف:.*?):''', drugText)
                    check(contraindication)
                Pharmacology = re.findall('''(فارماكوكينتيك:.*?):''', drugText)
                if len(Pharmacology) == 0:
                    Pharmacology = re.findall('''(فارماكوكنتيك:.*?):''', drugText)
                if len(Pharmacology) == 0:
                    Pharmacology = re.findall('''(فارماكوكينتيك:.*?):''', drugText)
                Warnings = re.findall('''(هشدارها:.*?):''', drugText)
                Adverse = re.findall('''(عوارض جانبي:.*?):''', drugText)
                interaction = re.findall('''(تداخل هاي دارويي:.*?):''', drugText)
                if len(interaction) == 0:
                    interaction = re.findall('''(تداخل دارويي:.*?):''', drugText)
                if len(interaction) == 0:
                    interaction = re.findall('''(تداخلهاي دارويي:.*?):''', drugText)

                Administration = re.findall('''(نكات قابل توصيه:.*?):''', drugText)
                Dosing = re.findall('''(مقدار مصرف:.*?):''', drugText)
                Dosage = re.findall('''(اشكال دارويي.*)''', drugText)
                # check(uses)
                # check(mechanism)
                # check(contraindication)
                # check(Pharmacology)
                # check(Warnings)
                # check(Adverse)
                # check(interaction)
                # check(Administration)
                # check(Dosing)
                # if len(Dosage) > 0:
                #     print(Dosage[0])

                if len(nameDrug) > 0:
                    general.write(rowCount, 0, nameDrug[0])
                general.write(rowCount, 1, check(uses))
                general.write(rowCount, 2, check(mechanism))
                general.write(rowCount, 3, check(contraindication))
                general.write(rowCount, 4, check(Pharmacology))
                general.write(rowCount, 5, check(Warnings))
                general.write(rowCount, 6, check(Adverse))
                general.write(rowCount, 7, check(interaction))
                general.write(rowCount, 8, check(Administration))
                general.write(rowCount, 9, check(Dosing))
                rowCount += 1

wb.close()
