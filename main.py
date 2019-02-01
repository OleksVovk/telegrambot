import requests

url = "https://api.telegram.org/<your_token>/"


def get_updates(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    all_updates = len(results) - 1
    return results[all_updates]

