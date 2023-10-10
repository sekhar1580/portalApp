from django.http import HttpResponse
import requests


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
        print(response.json()["access_token"])
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    return HttpResponse(response)