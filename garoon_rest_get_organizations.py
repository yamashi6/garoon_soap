import requests

url = 'https://(サブドメイン名).cybozu.com/g/api/v1/base/organizations/1/users'

headers = {
    'Host': '(サブドメイン名).cybozu.com:443', 
    # 'Content-Type': 'application/json',
     # 「ログイン名:パスワード」をBASE64エンコードしたものを値に指定。
     # xxxxxxxxxを書き換えること
    'X-Cybozu-Authorization': 'xxxxxxxxx',
    'Authorization': 'Basic xxxxxxxxx'
}

params = {
    'limit':1000
}

response = requests.get(url, headers=headers, params=params)

downloadData = response.json()

if len(downloadData) > 0:
    print(downloadData['users'])