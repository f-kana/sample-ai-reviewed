import requests

print("Program starts.")

url = "https://api.github.com"
response = requests.get(url)
print(f"ステータスコード: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print("レスポンスの内容:")
    # 出力内容が100文字は流石に短かったので200文字に変更したが、そもそもコレで良いのかはAIの意見がほしい。
    print(data[1:200])
else:
    print("リクエストが失敗しました")

if False:
    print("Program ends.")
