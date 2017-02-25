from pymongo import MongoClient
from datetime import datetime
client = MongoClient('localhost', 27018)
db = client.chatDB
collection=db['users']
# result = db.createCollection("users")

name="asmaa"
email="a@yahoo.com"
age=22
id=2
password=2
#-------------add user (sign up)----------------
addUser = db.users.insert_one(
{
        "_id":id,
        "name": name,
        "password":password,
        "age": age,
        "email":email,
        "friends": [],
        "Groups":[],
        "img":"img",
        "notification":[]
}
)
#-----------------sign in-----------------
# db.users.update({"_id":3},
#                           {"$set" : {"password":3}})
name="aya"
flag="false"
userID=db.users.find_one({"name":name},{"_id":1})# 1 for true to get id only

#print(userID)
if not(userID is None):
    #print("hi")
    flag="true"
    for key, val in userID.items():

       userPassword=db.users.find_one({"_id":val},{"password":1,"_id":0})# 1 for true to get pwd only
       print(userPassword)
givenPass=1
if (flag is "true"):
   for key, val in userPassword.items():
      #print("ho")
      #print(val)
      if(givenPass is val):
         print("Right user")


#-------------- add friend----------------
name="zaienab"
userID=db.users.find({"name":name},{"_id":1})
print(userID)
for key, val in userID.items():
        #print(val)
        id=1
        db.users.update(
                   {"_id":id},
                   {"$push":{"friends":val}}
                )
