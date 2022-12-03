import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myClient["mydatabase"]
# database created!
mycol = mydb["customers"]

mydict = {"name": "Sifat2", "adress": "Highway37"}
x = mycol.insert_one(mydict)
