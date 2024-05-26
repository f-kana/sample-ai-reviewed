import requests

url = "https://api.github.com"
response = requests.get(url)
print(f"ステータスコード: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print("レスポンスの内容:")
    # 出力内容が長すぎるので100文字に制限してみたが、妥当な修正かはAIに聞いてみたいところ。
    print(data[1:100])
else:
    print("リクエストが失敗しました")
