from flask import Flask
from flask_cors import CORS
from flask import Response
from flask import request
import json
import os
import geoip2.database
import sys
from urllib.parse import urlparse

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
    url = urlparse(request.headers.get("Origin")).netloc.replace("www.","")
    if url in config.sites:
        if config.sites[url]["key"]==request.args.get(key)
            resp = cr.country(request.headers.get("X-Forwarded-For"))
            return Response(
                json.dumps({"continent":resp.continent.code,"country":resp.country.code}),
                status=200,
                mimetype='application/json'
            )
    return Response(
        json.dumps({"continent":"","country":}),
        status=403,
        mimetype='application/json'
    )





    

         
