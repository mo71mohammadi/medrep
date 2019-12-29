import re
from concurrent.futures.thread import ThreadPoolExecutor
import pandas as pd
import requests

headers = {
    "Cookie": "_ga=GA1.1.299033548.1574769633; _ga_KG30PKD657=GS1.1.1577159958.27.0.1577159968.0; PHPSESSID=8a1ef51746b1f8dd31e8561bfda32774",
}
get = requests.get('https://medrep.ir/admin/item/add', headers=headers)
options = re.findall('''<option value="(\d*)">(.*?)</option>''', get.text)

df = pd.read_excel("eRx.xlsx")
selects = list(df.index)[32000:]


def _import(i):
    print(i)
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

    body = '''-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[status]"

1
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[withPrescription]"

0
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[onlyDoctorUser]"

0
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameEn]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandEn]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameFa]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandFa]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[erxCode]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[genericCode]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[motherCode]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[categories][]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[insurances][]"

54
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[licenceOwner]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandOwner]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[brandOwnerCountry]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[producer]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[producerCountry]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[nameInteractive]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[packing]"

1
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[form]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[pregnancyCategory]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[videoId]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[ircCodes][0][irc]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[description]"

{}
-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[warnings]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[adverseEffects]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[interactions]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[tips]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[pharmacology]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[mechanism]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[uses]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[submit]"


-----------------------------5978937891865297244995603244
Content-Disposition: form-data; name="pouyasoft_bundle_item[_token]"

07LVwY0eTsxSoChqEwIuu_T-rOkHqzw7XsS--BP6MBE
-----------------------------5978937891865297244995603244--'''.format(G, H, Z, L, A, S, N, catNum, V, E, Q, R, W, ZZ, B,
                                                                      VV)

    headers = {
        "Host": "medrep.ir",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        # "Accept-Encoding": "gzip, deflate, br",
        "Content-Length": "15929",
        "Origin": "https://medrep.ir",
        "Connection": "keep-alive",
        "Referer": "https://medrep.ir/admin/item/import",
        'Content-Type': 'multipart/form-data; boundary=---------------------------5978937891865297244995603244',
        "Cookie": "_ga=GA1.1.299033548.1574769633; _ga_KG30PKD657=GS1.1.1577159958.27.0.1577159968.0; PHPSESSID=8a1ef51746b1f8dd31e8561bfda32774",
        "Upgrade-Insecure-Requests": "1",
        "AlexaToolbar-ALX_NS_PH": "AlexaToolbar/alx-4.0.2",
        "TE": "Trailers",
    }

    imp = requests.post('https://medrep.ir/admin/item/add', body.encode('utf-8'), headers=headers)
    findImp = re.findall('رمز عبور خود را فراموش کرده ام', imp.text)
    busy = re.findall('503 Service Unavailable', imp.text)
    error404 = re.findall('ممکن است صفحه مورد نظر شما حذف یا انتقال داده شده است', imp.text)

    if len(findImp) > 0:
        print("login:   ", A)
        return _import(i)
    elif len(busy) > 0:
        return _import(i)
    elif len(error404) > 0:
        file404 = open('text.txt', 'a')
        file404.write(A+"\n")
        file404.close()
    else:
        # findImp = re.findall('کالا با موفقیت ثبت شد', imp.text)
        # if len(findImp) == 0:
        findImp = re.findall('این مقدار قبلا مورد استفاده قرار گرفته است', imp.text)
        if len(findImp) == 0:
            findImp = re.findall('این مقدار معتبر نیست', imp.text)
            if len(findImp) > 0:
                print("catNum.......", catNum, A)
            else:
                print(imp.text)
                return _import(i)
    return repeat()


def repeat():
    nowSelects = selects[0:1]
    for select in nowSelects:
        selects.remove(select)
    _import(nowSelects[0])


nowSelects = selects[0:50]
for select in nowSelects:
    selects.remove(select)
with ThreadPoolExecutor(max_workers=100) as pool:
    pool.map(_import, nowSelects)
