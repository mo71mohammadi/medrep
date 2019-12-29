import re

import pandas as pd
import requests

Cookie = "_ga=GA1.1.299033548.1574769633; _ga_KG30PKD657=GS1.1.1577123037.24.0.1577123045.0; PHPSESSID=efe6e31573ab8f06bf692f53a61916d6"
headers = {
    "Cookie": Cookie,
}
get = requests.get('https://medrep.ir/admin/item/', headers=headers)
options = re.findall('''value="(\d*)">(.*?)</option>''', get.text)

df = pd.read_excel("eRx.xlsx")
selects = list(df.index)
chekList = []
count = 0
for item in options:
    chekList.append(item[1])
for i in df.index:
    A = df['eRx code'][i]
    if A == 'nan':
        A = ' '
    S = df['کد ژنریک معادل'][i]
    if S == 'nan':
        S = ' '

    G = df[' نام عمومی انگلیسیnew generic name '][i]
    if G == 'nan':
        G = ' '

    H = df[' نام برند انگلیسی brand E name '][i]
    if H == 'nan':
        H = ' '

    # K = df['brand & g name نام برند و عمومی باهم انگلیسی'][i]
    L = df['نام برند فارسی'][i]
    if L == 'nan':
        L = ' '

    Z = df['نام عمومی فارسی'][i]
    if Z == 'nan':
        Z = ' '

    # X = df['نام برند و عمومی فارسی'][i]
    C = df['بارکد'][i]
    if C == 'nan':
        C = ' '

    V = df['صاحب پروانه'][i]
    if V == 'nan':
        V = ' '

    B = df['IRC2'][i]
    if B == 'nan':
        B = ' '

    N = df['کد مادري'][i]
    if N == 'nan':
        N = ' '

    M = df['تاريخ اعتبار'][i]
    if M == 'nan':
        M = ' '

    Q = df['کشور صاحب نام تجاری'][i]
    if Q == 'nan':
        Q = ' '

    E = df[' صاحب نام تجاری '][i]
    if E == 'nan':
        E = ' '

    W = df['کشور تولید کننده'][i]
    if W == 'nan':
        W = ' '

    R = df['توليدکننده'][i]
    if R == 'nan':
        R = ' '

    T = df['نام مهاوره ای'][i]
    if T == 'nan':
        T = ' '

    Y = df['سطح یک گروه بندی'][i].strip()
    U = df['سطح دو دسته بندی'][i].strip()
    I = df['سطح سه دسته بندی'][i].strip()
    O = df['سطح چهار دسته بندی'][i].strip()
    P = df['ATC دسته بندی'][i]
    if P == 'nan':
        P = ' '

    AA = df['بسته بندی'][i]
    if AA == 'nan':
        AA = ' '

    XX = df['INDEX NAME'][i]
    if XX == 'nan':
        XX = ' '

    ZZ = df['شکل محصول'][i]
    if ZZ == 'nan':
        ZZ = ' '

    CC = df['رده بارداری'][i]
    if CC == 'nan':
        CC = ' '

    VV = df['توضیحات'][i]
    if VV == 'nan':
        VV = ' '

    BB = df['هشدارها '][i]
    if BB == 'nan':
        BB = ' '

    NN = df['عوارض جانبی'][i]
    if NN == 'nan':
        NN = ' '

    MM = df['تداخل های دارویی '][i]
    if MM == 'nan':
        MM = ' '

    QQ = df['نکات قابل توصیه'][i]
    if QQ == 'nan':
        QQ = ' '

    WW = df['فارماکوکینتیک'][i]
    if WW == 'nan':
        WW = ' '

    EE = df['مکانیسم اثر'][i]
    if EE == 'nan':
        EE = ' '

    RR = df['موارد مصرف'][i]
    if RR == 'nan':
        RR = ' '
    categoryStr = Y + ' - ' + U + ' - ' + I + ' - ' + O
    catNum = 0
    for item in options:
        if item[1] == categoryStr:
            catNum = item[0]
    if catNum == 0:
        print(A, i)


        def add_item(items, category, objects, number):
            if items[1] == category and category + ' - ' + objects not in chekList:
                print(objects)
                url = 'https://medrep.ir/admin/category/index/{}'.format(items[0])
                header = {
                    "Cookie": Cookie,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Upgrade-Insecure-Requests": "1",
                    "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.2",
                    "Referer": "https://medrep.ir/admin/category/index/2059",
                }
                data = {
                    "pouyasoftbundle_category[name]": objects,
                    "pouyasoftbundle_category[code]": '',
                    "pouyasoftbundle_category[submit]": '',
                    "pouyasoftbundle_category[_token]": "4ZnZQIYQZMZ5OAjbsVxlmfkv5DaBep8emSHdQXzmeno"
                }
                requests.post(url, data, headers=header)
                chekList.append(category + ' - ' + objects)
                return number

        def addCat(items):
            category = Y + ' - ' + U + ' - ' + I
            number = add_item(items, category, O, 1)
            if number:
                return number

            category = Y + ' - ' + U
            number = add_item(items, category, I, 2)
            if number:
                return number

            category = Y
            number = add_item(items, category, U, 3)
            if number:
                return number

            return 4

        for obj in options:
            response = addCat(obj)
            if response == 1:
                count += 1
                break
            if response == 2:
                count += 1
                for objs in options:
                    response = addCat(objs)
                    if response == 1:
                        count += 1
                        break
                break
            if response == 3:
                count += 1
                for objss in options:
                    response = addCat(objss)
                    if response == 2:
                        count += 1
                        for objs in options:
                            response = addCat(objs)
                            if response == 1:
                                count += 1
                                break
                        break
                break
        print(count)

