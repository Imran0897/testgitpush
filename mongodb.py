import pymongo

client = pymongo.MongoClient("mongodb+srv://imran:imranmongo@cluster0.8ykda.mongodb.net/?retryWrites=true&w=majority")
db = client.test


d = {
    "name" : "sudhanshu",
    "email" : "sudhanshu@gmail.com",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)