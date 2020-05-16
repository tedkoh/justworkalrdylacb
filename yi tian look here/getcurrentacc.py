def createcurrentacc():
    import requests
    
    url = "https://razerhackathon.sandbox.mambu.com/api/savings"
    auth = ('Team112','pass19694D02B3')
    payload = "{\n    \"savingsAccount\": {\n        \"name\": \"Digital Account\",\n        \"accountHolderType\": \"CLIENT\",\n        \"accountHolderKey\": {{clientId}},\n        \"accountState\": \"APPROVED\",\n        \"productTypeKey\": \"8a8e878471bf59cf0171bf6979700440\",\n        \"accountType\": \"CURRENT_ACCOUNT\",\n        \"currencyCode\": \"SGD\",\n        \"allowOverdraft\": \"true\",\n        \"overdraftLimit\": \"100\",\n        \"overdraftInterestSettings\": {\n            \"interestRate\": 5\n        },\n            \"interestSettings\": {\n        \"interestRate\": \"1.25\"\n    }\n    }\n\n}"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data = payload, auth=auth)

    print(response.text.encode('utf8'))
    return response.json()