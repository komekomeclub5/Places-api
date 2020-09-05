# Places-api

## 概要

台風の時に周辺のスーパーマーケットの営業状態をひと目でわかるようにしたい。

## 事前準備

DockerDesktopを事前にダウンロードしてください。


[DockerをMacにインストールする（更新: 2019/7/13）](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)

　

Google PlacesAPI のAPIキーを取得してください。

[Get an API Key](https://developers.google.com/places/web-service/get-api-key)

**APIキーを他の人が使うとGoogleに止められちゃうかも**


## 使用方法

起動
```
docker-compose up -d
```

ブラウザでアクセス
```
localhost:8000
```

終了
```
docker-compose down
```
