import json

credentials = {
    "amazon" : {
        "email" : "user@domain.com",
        "pass" : "password",
        "method" : 1
    },
    "credit_card" : {
        "number" : "1234567890",
        "owner" : "Mario Rossi",
        "month" : "1",
        "year" : "22",
        "cvv" : "333"
    }
}

with open("config.json", 'w') as outfile:
    json.dump(credentials, outfile, indent=4, sort_keys=False)
