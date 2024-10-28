import requests

key = 'cfbd0ceb0c45450588547e8f695eec0d'
api_addresses = "http://newsapi.org/v2/top-headlines?country=us&apikey=" + key


json_data = requests.get(api_addresses).json()

ar = []

def news():
    
    for i in range(3):
        ar.append("Number " + str(i + 1) + ": " + json_data["articles"][i]["title"] + " - ")
    
    return ar

