import requests
import pymongo

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
collection = db['product']


company = requests.get('http://import.imed.fda.gov.ir/SrchInAutoComplete/Srch_UMDNSGroup_Visible_GroupOrChild.ashx?q=&limit=150&timestamp=1575670482380')
# print(company.text)
# print(len(company.text.split('\r\n')))
for com in set(company.text.split('\r\n')):
    collection.insert_one({"name": com, "start": 0, "update": False})

# com = collection.find()
# for item in com:
#     print(item.name)