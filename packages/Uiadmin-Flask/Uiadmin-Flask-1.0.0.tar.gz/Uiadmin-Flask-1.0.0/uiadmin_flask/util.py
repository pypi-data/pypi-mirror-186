from flask import jsonify

def jsonres(data):
    resp = jsonify(data)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type, CloudId, Eid")
    resp.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    print(resp.headers)
    return resp
