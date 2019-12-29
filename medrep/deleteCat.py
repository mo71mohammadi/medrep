from concurrent.futures.thread import ThreadPoolExecutor

import requests

headers = {
    "Cookie": "_ga=GA1.1.299033548.1574769633; _ga_KG30PKD657=GS1.1.1577123037.24.0.1577123045.0; PHPSESSID=efe6e31573ab8f06bf692f53a61916d6",
}
selects = list(reversed(range(4000, 4643)))
print(selects)

def _import(i):
    print(i)
    url = 'https://medrep.ir/admin/category/{}/delete'.format(i)
    requests.get(url, headers=headers)
    return repeat()


def repeat():
    nowSelects = selects[0:1]
    for select in nowSelects:
        selects.remove(select)
    _import(nowSelects[0])


nowSelects = selects[0:5]
for select in nowSelects:
    selects.remove(select)
with ThreadPoolExecutor(max_workers=50) as pool:
    pool.map(_import, nowSelects)
