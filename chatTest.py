from pymongo import MongoClient
from datetime import datetime
client = MongoClient('localhost', 27018)
db = client.chatDB
collection=db['users']
groupCollection=db['groups']
usersCollection=db['allusers']
# result = db.createCollection("users")

name="asmaa"
email="a@yahoo.com"
age=22
id=3
password=2
#-------------add user (sign up)----------------
# addUser = db.users.insert_one(
# {
#         "_id":id,
#         "name": name,
#         "password":password,
#         "age": age,
#         "email":email,
#         "friends": [],
#         "Groups":[],
#         "img":"img",
#         "notification":[]
# }
# )
# allUsers = db.allusers.insert_one(
# {
#    "_id":id,
# }
# )


#-----------------sign in-----------------
# db.users.update({"_id":3},
#                           {"$set" : {"password":3}})
# name="aya"
# flag="false"
# userID=db.users.find_one({"name":name},{"_id":1})# 1 for true to get id only
#
# print(userID)
# if not(userID is None):
#     #print("hi")
#     flag="true"
#     for key, val in userID.items():
#
#        userPassword=db.users.find_one({"_id":val},{"password":1,"_id":0})# 1 for true to get pwd only
#        print(userPassword)
# givenPass=1
# if (flag is "true"):
#    for key, val in userPassword.items():
#       #print("ho")
#       #print(val)
#       if(givenPass is val):
#          print("Right user")


#-------------- accept user (add friend)---------------
# name="zaienab"
# userID=db.users.find_one({"name":name},{"_id":1})
# print(userID)
# for key, val in userID.items():
#         #print(val)
#         id=1 # a8yr el id
#         db.users.update(
#                    {"_id":id},
#                    {"$push":{"friends":val}}
#                 )
#         db.users.update(
#                    {"_id":val},
#                    {"$push":{"friends":id}}
#                 )
#-----------------------find my friends----------------------
# userName="aya"
# myFriendsIDs=db.users.find_one({"name":userName},{"_id":0,"friends":1})
# myFriendsVal=[]
# myFriendsNames=[]
# for key, myFriendsVal in myFriendsIDs.items():
#          print(myFriendsVal)
# for val in myFriendsVal:
#     myFriendsObjects=db.users.find_one({"_id":val},{"name":1,"_id":0})
#     print(myFriendsObjects)
#     for  key, val in myFriendsObjects.items():
#          myFriendsNames.append(val)
# for val in myFriendsNames:
#           print(val)
#-----------------------all users----------------------
# userName="zaienab"
# myFriendsIDs=db.users.find_one({"name":userName},{"_id":0,"friends":1})
# myFriendsVal=[]
# myFriends=[]
# allUsers=[]
# notFriendsID=[]
# notFriendsNames=[]
#
# myIDObj=db.users.find_one({"name":userName},{"_id":1})
# myID=myIDObj['_id']
# print(myID)
# for key, myFriendsVal in myFriendsIDs.items():
#          print(myFriendsVal)
# for key, val in myFriendsIDs.items():
#         #  print (val)
#          myFriends.append(val)
# allUsersIDs=db.users.find({},{"_id":1})
# for   val in allUsersIDs:
#         #  print(val['_id'])
#          allUsers.append(val['_id'])
# for elem in allUsers:
#    if elem == myID:
#        continue
#    if elem not in myFriendsVal:
#          print (elem)# prints users thats is not my friends ids
#          notFriendsID.append(elem)
# for val in notFriendsID:
#     myFriendsObjects=db.users.find_one({"_id":val},{"name":1,"_id":0})
#     print(myFriendsObjects)
#     for  key, val in myFriendsObjects.items():
#         print(val)
#         notFriendsNames.append(val)


#---------------------remove friend-----------------------
# name="zaienab"
# userID=db.users.find_one({"name":name},{"_id":1})
# print(userID)
# for key, val in userID.items():
#         #print(val)
#         id=1 # to be changed
#         db.users.update(
#                    {"_id":id},
#                    {"$pull":{"friends":val}}
#                 )
#         db.users.update(
#                            {"name":"zaienab"},
#                            {"$pull":{"friends":id}}
#                         )
#

#--------------------add group------------------
# id=1
# name="openSource"
# owner="aya"
# img="img"
# desc="just description"
# addGroup = db.groups.insert_one(
# {
#         "_id":id,
#         "name": name,
#         "owner":owner,
#         "members":[],
#         "img":"img",
#         "description":desc
# }
# )
#-------------- join group----------------
# groupName="openSource"
# groupID=db.groups.find_one({"name":groupName},{"_id":1})
# print(groupID)
# for key, val in groupID.items():
#         #print(val)
#         userID=2 #givenID
#         db.groups.update(
#                    {"_id":val},
#                    {"$push":{"members":userID}}
#                 )
#         db.users.update(
#                    {"_id":userID},
#                    {"$push":{"Groups":val}}
#                 )
#-------------------leave group----------------------
# groupName="openSource"
# groupID=db.groups.find_one({"name":groupName},{"_id":1})
# print(groupID)
# for key, val in groupID.items():
#         #print(val)
#         userID=2
#         db.groups.update(
#                    {"_id":val},
#                    {"$push":{"members":userID}}
#                 )
#         db.users.update(
#                    {"_id":userID},
#                    {"$push":{"Groups":val}}
#                 )
#-------------------find my groups----------------------
# userName="zaienab"
# myGroupsIDs=db.users.find_one({"name":userName},{"_id":0,"Groups":1})
# myGroupsVal=[]
# myGroupsNames=[]
# for key, myGroupsVal in myGroupsIDs.items():
#          print(myGroupsVal)
# for val in myGroupsVal:
#     myGroupsObjects=db.groups.find_one({"_id":val},{"name":1,"_id":0})
#     print(myGroupsObjects)
#     for  key, val in myGroupsObjects.items():
#          myGroupsNames.append(val)
# for val in myGroupsNames:
#           print(val)
#-----------------------all groups----------------------
# userName="zaienab"
# myGroupsIDs=db.users.find_one({"name":userName},{"_id":0,"Groups":1})
# myGroupsVal=[]
# myGroups=[]
# allGroups=[]
# notGroupsID=[]
# notGroupsNames=[]
#
# for key, myGroups in myGroupsIDs.items():
#         print ("val")
#         #  myGroups.append(val)
#
# allGroupsIDs=db.groups.find({})
# for   val in allGroupsIDs:
#         #  print("sss",val['_id'])
#          allGroups.append(val['_id'])
# for elem in allGroups:
#    # if elem == myID:
#    #     continue
#    if elem not in myGroups:
#          print (elem)# prints users thats is not my friends ids
#          notGroupsID.append(elem)
# for val in notGroupsID:
#     myGroupsObjects=db.groups.find_one({"_id":val},{"name":1,"_id":0})
#     print(myGroupsObjects)
#     for  key, val in myGroupsObjects.items():
#         print(val)
#         notGroupsNames.append(val)

