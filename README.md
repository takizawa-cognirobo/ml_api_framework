# ml_api_framework
# 独自の機械学習APIを実装するためのフレームワーク

## 概要
モデル用クラス及びpickleファイル、
データインターフェースを作成するだけで機械学習の推論APIが実装できるフレームワーク

## インターフェース
WEBAPIとして実装
HTTPリクエストでデータをJSON形式でPOSTし、推論結果をJSONで返すAPI

## 利用サンプル
### Docker起動
docker run -it --rm -p 5000:5000 -p 8888:8888 -v $(pwd):/home ml_api:1.0 /bin/bash

### APIへのポスト
curl http://127.0.0.1:5000/predict -X POST -H 'Content-Type:text/json' -d '[{"feature1":1,"feature2":1,"feature3":1,"feature4":1},{"feature1":2,"feature2":3,"feature3":4,"feature4":2}]'

