import pymongo
#link to the mongodb
db_client = pymongo.MongoClient("mongodb://localhost:27017")

db = db_client["student"]

f = open("student.txt").readlines()
for line in f:
    line = line.replace("/n", "")
    tokens = line.split(", ")
    student = dict()
    student["name"] = tokens[0]
    student["age"] = tokens[1]
    student["department"] = tokens[2]
    student["university"] = tokens[3]

db.student_info.delete_one({"name": "bob"})
for student in db.student_info.find({"name":"bob"}):
    print(student)