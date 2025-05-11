import requests
import json

refresh_token = input("Enter Refresh Token: ")

response = requests.get(f"https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token={refresh_token}")

token = None

if response.status_code == 200:
    token = response.json()
    token_file = open("output/token.json","w")
    json.dump(response.json(),token_file)
    token_file.close()
else:
    print("Error getting token: ")
    print(response.text)