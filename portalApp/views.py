from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def index(request):
    authUrl= "https://altrasoftwaresystems-dev-ed.develop.my.salesforce.com/services/oauth2/token?"
    payload = {
    "client_id":"3MVG9fe4g9fhX0E58YVLQfgEs2O.e90Ac5YBzPEOsKrL85AOCzGHTatRui5O1DL9ZSjDPZrjjIZx1f43C6o09",
    "client_secret":"3677D3EFA9096644265A2CCB531A51F002DBC5DECFECD5B8D4FA2EE03575935F",
    "username":"geetha.salesforce@crm.com",
    "password":"Sales@4321yVo8hqf0dcz8kCKGO6Yh1kO2A",
    "grant_type":"password"
    }    

    try:
        response = requests.post(authUrl, data=payload)
        response.raise_for_status()
        token = response.json()["access_token"]
        print
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json  
    try:
        profilePayload = json.loads(request.body)       
        url = "https://altrasoftwaresystems-dev-ed.develop.my.salesforce.com/services/data/v58.0/sobjects/Referral_Staging__c"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        response2 = requests.post(url, data=json.dumps(profilePayload), headers=headers)
        print(json.dumps(profilePayload))
        response2.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return HttpResponse(response2)