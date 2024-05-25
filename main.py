import requests

url = "https://api.github.com"
response = requests.get(url)
print(f"ステータスコード: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print("レスポンスの内容:")
    print(data)
else:
    print("リクエストが失敗しました")
