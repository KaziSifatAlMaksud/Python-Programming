import pymongo

myCliand = pymongo.MongoClient("mongodb://localhost:27017")

db = myCliand["student"]

student = dict()

f = open("Mongodb 1/student.txt").readlines()

for line in f:
    line = line.replace("/n", "")
    #array
    tockens = line.split(", ")
    student["name"] = tockens[0]
    student["age"] = tockens[1]
    student["department"] = tockens[2]
    student["edu"] = tockens[3]
    db.student.insert_one(student)

for std in db.student.find():
    print(std)
