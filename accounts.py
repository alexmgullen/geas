import requests
import json


token_file = open("output/token.json","r")
token = json.load(token_file)
token_file.close()


url = f"{token["api_server"]}v1/accounts"
print(url)
response = requests.get(url,headers={"Authorization": f"Bearer {token["access_token"]}"})

if response.status_code == 200:
    account_file = open("output/account.json","w")
    json.dump(response.json(),account_file)
    account_file.close()
else:
    print("Failed to fetch accounts: ")
    print(response.text)