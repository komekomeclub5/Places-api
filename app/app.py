#API関連
import googlemaps
import pprint 
import json
import urllib.request

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/")
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/index",methods=["POST"])
def index():

    key = 'APIキー' # APIキー
    client = googlemaps.Client(key) #インスタンス生成
    place = request.form["place"]
    geocode_result = client.geocode(place) # 位置情報を検索
    loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
    place_results = client.places_nearby(location=loc, radius=3000, type='supermarket') #半径3km以内のスーパーマーケットの情報を取得
    
    # result_out=pprint.pformat(place_result,depth=3, width=50, indent=4)

    results = []

    for place_result in place_results['results']:
        results.append(place_result)

    return render_template("index.html",results=results,place=place)




if __name__ == "__main__":
    app.run(debug=True)
   
