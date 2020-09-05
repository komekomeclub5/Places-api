#API関連
import googlemaps
import pprint 

#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request

#Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():

    key = 'APIキー' # APIキー
    client = googlemaps.Client(key) #インスタンス生成

    geocode_result = client.geocode('宜野湾市役所') # 位置情報を検索
    loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
    place_result = client.places_nearby(location=loc, radius=3000, type='supermarket') #半径3km以内のスーパーマーケットの情報を取得

    result_out=pprint.pformat(place_result,depth=3, width=50, indent=4)


    return render_template("index.html",result_out=result_out)




if __name__ == "__main__":
    app.run(debug=True)
   