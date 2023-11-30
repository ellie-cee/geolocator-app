from flask import Flask
from flask_cors import CORS
from flask import Response
from flask import request
import json
import os
import geoip2.database

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
    resp = reader.asn(request.remote_addr)
    print(resp,file=sys.stderr)



@app.route("/webhooks/<topic>",methods=["POST","GET"])
def webhook(topic):
    match topic:
        case "order_edit":
            return webhooks.OrderEdited(app,request).run()
        case "order_created":
            return webhooks.OrderCreated(app,request).run()
        case "list":
            return webhooks.Shopify(app,request).list()
        case "install":
            webhooks.Shopify(app,request).install("orders/edited","webhooks/order_edit")
            #webhooks.Shopify(app,request).install("orders/create","webhooks/order_created")
            return Response(
                json.dumps({"msg":"installed"}),
                status=200,
                mimetype='application/json'
            )
        case "uninstall":
            webhooks.Shopify(app,request).uninstall()
            return Response(
                json.dumps({"msg":"uninstalled"}),
                status=200,
                mimetype='application/json'
            )

    return Response(
        json.dumps({"msg":f"Unkown webhook {topic}"}),
        status=200,
        mimetype='application/json'
    )

         
@app.route("/api/collect",methods=["POST"])
def confirm_request():
    return controllers.Collector(request).run()

@app.route("/api/install",methods=["GET"])
def iwh():
    webhooks.Shopify(app,request).install("orders/edited","webhooks/order_edit")
    webhooks.Shopify(app,request).install("orders/create","webhooks/order_created")
    return Response(
        json.dumps({"msg":"installed"}),
        status=200,
        mimetype='application/json'
    )
@app.route("/api/uninstall",methods=["GET"])
def uwh():
    webhooks.Shopify(app,request).uninstall()
    return Response(
        json.dumps({"msg":"installed"}),
        status=200,
        mimetype='application/json'
    )
