import pymongo

#连接数据库
from bson import ObjectId

dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbclient["fashiondb"]

users = db['users']
clothes = db['clothes']

def login(name):
    obj = {"name": name}
    id = users.insert_one(obj)
    return id

def add_clothes(uid, url, class_index):
    obj = {"uid": uid, "url": url,"class_name": class_index}
    id = clothes.insert_one(obj)
    return id

def find_all_clothes(uid):
    all_clothes = []
    for cloth in clothes.find({"uid": uid}):
        cloth['_id'] = str(cloth['_id'])
        all_clothes.append(cloth)
    return all_clothes

def find_all_clothes_by_classname(uid, class_index):
    all_clothes = []
    for cloth in clothes.find({"uid": uid, "class_name": class_index}, {"uid": 0}):
        cloth['_id']= str(cloth['_id'])
        all_clothes.append(cloth)
    return all_clothes

def update_cloth_class(id, class_index):
    value = {"_id": ObjectId(id)}
    new_value = {"$set": {"class_name": class_index}}
    return clothes.update_one(value, new_value)

def delete_cloth(id):
    obj = {"_id": ObjectId(id)}
    return clothes.delete_one(obj)

