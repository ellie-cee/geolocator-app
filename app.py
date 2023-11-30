from flask import Flask
from flask_cors import CORS
from flask import Response
from flask import request
import json
import os
import geoip2.database
import sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
config = json.load(open(f'{path}/config.json'))
app = Flask(__name__)
CORS(
    app,
    resources=r"/*",
    origins=config["origins"]
)



reader = geoip2.database.Reader(f'{path}/GeoLite2-ASN.mmdb') 
cr = geoip2.database.Reader(f'{path}/GeoLite2-Country.mmdb') 

@app.route("/")
def helloWorld():
  return "jfod;w fpn9y9 nr0qny"

@app.route("/locate")
def locateASN():
    print(request.headers.get("X-Forwarded-For"),file=sys.stderr)
    print(request.headers)
    resp = cr.country(request.headers.get("X-Forwarded-For"))
    print(resp,file=sys.stderr)
    return Response(
        json.dumps({"msg":f"pewp"}),
        status=200,
        mimetype='application/json'
    )





    

         
