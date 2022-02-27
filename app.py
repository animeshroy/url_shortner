from flask import Flask, redirect, request
import json, hashlib, re
app = Flask(__name__)
    
short_hash_map = {} # short_url is key
long_hash_map = {} # long_url is key

@app.route('/<short_url>',methods = ['GET'])
def long_url(short_url):
    url = "http://localhost:5000/"+short_url
    if  url in short_hash_map:
        return redirect(short_hash_map[url])
    else:
        return json.dumps({"message":"URL NOT FOUND or NOT CORRECT"})

@app.route('/shorten_url/',methods = ['GET'])
def shorten_long_url():
    result = {}
    long_url = request.get_json()["url"]
    short_url = shorten_url(long_url)
    result["long_url"]=short_url
    return json.dumps(result)

@app.route('/search_key/<key_word>',methods = ['GET'])
def search_keyword(key_word):
    long_url_values = list(long_hash_map.keys())
    result = []
    for i in long_url_values:
        if bool(re.search(key_word,i,flags = re.I)):
            result.append({"long_url":i,"short_url":long_hash_map[i]})
    if not result:
        result = {"Error":"No Data Found"}
    return json.dumps(result)

def shorten_url(long_url):
    global url_hash_map
    if long_url in long_hash_map:
        return long_hash_map[long_url]
    else:
        short_url = "http://localhost:5000/"+hashlib.sha256(long_url.encode()).hexdigest()[:5]
        long_hash_map[long_url] = short_url
        short_hash_map[short_url] = long_url
        return long_hash_map[long_url]

if __name__ == '__main__':
   app.run(debug = True)
