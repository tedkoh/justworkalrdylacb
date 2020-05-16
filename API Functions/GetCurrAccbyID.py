def GetCurrAccbyID(accountId):
    import requests

    url = "https://razerhackathon.sandbox.mambu.com/api/savings/{}/"
    auth = ('Team112', 'pass19694D02B3')
    payload  = {}
    headers = {'': ''}

    response = requests.request("GET", 
                                url.format(accountId), 
                                headers=headers, 
                                data = payload,
                                auth = auth)

    return response.json()