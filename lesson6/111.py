from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['books']
news_db = db['labirint']
news_db = db['book24']

news_db.delete_many({})
i = 0
for item in news_db.find():
    i += 1
    print(item)

print(i)