import requests

url = 'https://fcm.googleapis.com/fcm/send'
headers = {
    "Authorization": "key $fcm_api_key",
    "Content-Type": "application/json"
}

data = {"registration_ids": "ABC"}

res = requests.post(url, headers = headers, data=data)

print(res.text)
