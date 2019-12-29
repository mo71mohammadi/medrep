from concurrent.futures.thread import ThreadPoolExecutor

import requests

headers = {
    "Cookie": "_ga=GA1.1.299033548.1574769633; _ga_KG30PKD657=GS1.1.1577034071.17.0.1577034077.0; PHPSESSID=14cd744d0ae52b25bda78f15cc0bdee9",
}
selects = list(range(105892, 115801))


def _import(i):
    print(i)
    url = 'https://medrep.ir/admin/item/{}/delete'.format(i)
    requests.get(url, headers=headers)
    return repeat()


def repeat():
    nowSelects = selects[0:1]
    for select in nowSelects:
        selects.remove(select)
    _import(nowSelects[0])


nowSelects = selects[0:20]
for select in nowSelects:
    selects.remove(select)
with ThreadPoolExecutor(max_workers=50) as pool:
    pool.map(_import, nowSelects)
