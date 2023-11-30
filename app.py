from flask import Flask
from flask_cors import CORS
from flask import Response
from flask import request
import json
import os
import geoip2.database
import sys

app = Flask(__name__)
CORS(
    app,
    resources=r"/*",
    origins=[
        "https://reuzel.com",
        "https://reuzelinc.myshopify.com",
        "https://reuzel.uk",
        "https://uk-reuzel.myshopify.com",
    ]
)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
reader = geoip2.database.Reader(f'{path}/GeoLite2-ASN.mmdb') 

@app.route("/")
def helloWorld():
  return "jfod;w fpn9y9 nr0qny"

@app.route("/locate")
def locateASN():
    print(request.headers,file=sys.stderr)
   # resp = reader.asn(request.remote_addr)
   # print(resp,file=sys.stderr)
   return Response(
        json.dumps({"msg":f"pewp"}),
        status=200,
        mimetype='application/json'
    )





    

         
