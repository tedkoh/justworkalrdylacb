def getCAccByID():
    import requests

    url = "https://razerhackathon.sandbox.mambu.com/api/savings/{{accountId}}/"
    auth = ('Team112','pass19694D02B3')
    payload  = {}
    headers = {'': ''}

    response = requests.request("GET", url, headers=headers, data = payload, auth=auth)

    print(response.text.encode('utf8'))
    return response.json()