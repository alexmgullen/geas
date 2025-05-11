import requests
import json
from datetime import datetime, date, timedelta
import time


token_file = open("output/token.json","r")
token = json.load(token_file)
token_file.close()

account_file = open("output/account.json","r")
account = json.load(account_file)
account_file.close()

all_activites = []

for a in account["accounts"]:

    account_creation_date = datetime(2020,1,1)
    today = datetime(2020,4,20)#datetime.today()

    delta = today - account_creation_date 

    print(delta)


    #print(today.strftime("%Y-%m-%dT17:00:00-05:00"))

    #2011-02-01T00:00:00-05:00

    # Maximum of 31 days can be requested at a time
    url = f"{token["api_server"]}v1/accounts/{a["number"]}/activities?startTime=2011-02-01T00:00:00-05:00&endTime=2011-02-28T00:00:00-05:00&"

    print(url)
    response = requests.get(url,headers={"Authorization": f"Bearer {token["access_token"]}"})
    if response.status_code == 200:

        all_activites.append(response.json())
    else:
        print("Failed to fetch accounts: ")
        print(response.text)

    #politness timer
    time.sleep(0.8)
    
activites_file = open("output/activites.json","w")
json.dump(all_activites,activites_file)
activites_file.close()