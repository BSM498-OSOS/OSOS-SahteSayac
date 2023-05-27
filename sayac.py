from flask import Flask,request
from pymongo import MongoClient
import datetime
import random

CONNECTION_STRING = 'mongodb://localhost:27017'
client = MongoClient(CONNECTION_STRING)
db=client.Readings
app = Flask(__name__)

def returnLastOne(Obis000):
    col=db.Reading
    data=list(col.find({"Obis000":int(Obis000)}).sort("_id",-1))
    item={"Obis000":Obis000,"Obis092":datetime.datetime.now()}
    if len(data)>0:
        item["Obis180"]=data[0]['Obis180']+random.uniform(0,50.0)
    else:
        item["Obis180"]=random.uniform(0,50.0)
    return item

@app.route('/',methods= ['GET'])
def index():
    serialNo=request.args.get("Obis000")
    return returnLastOne(serialNo)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)