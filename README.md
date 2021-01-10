# Places-api

## 概要

台風の時に周辺のスーパーマーケットの営業状態をひと目でわかるようにしたい。

(将来的にユニオンの営業状態で台風の危険度を判断したい。)

## 事前準備

DockerDesktopを事前にダウンロードしてください。


[DockerをMacにインストールする（更新: 2019/7/13）](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)

　

Google PlacesAPI のAPIキーを取得してください。

[Get an API Key](https://developers.google.com/places/web-service/get-api-key)




## 使用方法

初めて起動するとき
```
docker-compose up --build
```

起動
```
docker-compose up
```

ブラウザでアクセス
```
localhost:8000
```

終了
```
docker-compose down
```
