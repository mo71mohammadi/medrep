import pymongo

Client = pymongo.MongoClient('localhost', 27017)
db = Client['imed']
company = db['product']
general = db['general']
#
Company = company.find({"start": {"$ne": -1}})
General = general.find()

# for g in General:
#     for item in g['models']:
#         if len(item['IRCs']) > 1:
#             print(g['_id'], g['company'])
count = 0
for item in Company:
    count += 1
    # col.update_one({"_id": item["_id"]}, {"$set": {"start": 0}})

print(count)
