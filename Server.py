from flask import Flask
from flask import request
import pymongo
myclient = pymongo.MongoClient("mongodb://3.129.248.120/")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Student Records Management'

@app.route('/adddata')
def AddData():
    a = request.args.get('name')
    b = request.args.get('id')
    c = request.args.get('course')
    d = request.args.get('marks')
    mydict = { "name": a,"id":b ,"course": c ,"marks" : d}
    x = mycol.insert_one(mydict)
    return "Data Successfully added"

@app.route('/deldata')
def DelData():
    a = request.args.get('id')
    mydict = { "id": a}
    x = mycol.delete_one(mydict)
    return "Data Successfully Deleted"

@app.route('/finddata')
def FindData():
    a = request.args.get('id')
    mydict = { "id": a}
    x = mycol.find(mydict)
    for i in x:
        pass
    print (i["name"],i["id"],i["course"],i["marks"]) 
    return "Record Found : "+"\nName : "+i["name"]+"\nId : "+i["id"]+"\nCourse : "+i["course"]+"\nMarks : "+i["marks"]

@app.route('/updatedata')
def UpdateData():
    a = request.args.get('name')
    b = request.args.get('id')
    c = request.args.get('course')
    d = request.args.get('marks')
    search = { "id":b }
    update = { "$set": { "name": a,"course": c ,"marks" : d} }
    x = mycol.update_one(search,update)
    return "Data Successfully Updated"

@app.route('/getid')
def getid():
    a = request.args.get('id')
    mydict = { "id": a}
    x = mycol.find(mydict)
    for i in x:
        pass
    print (i["id"]) 
    return i["id"]+","+i["name"]+","+i["course"]+","+i["marks"]


if __name__ == '__main__':
    app.run()