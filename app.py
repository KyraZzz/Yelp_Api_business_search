import requests
import config  # hide the api key to ensure the safety

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "food",
    "location": "Cambridge"
}

response = requests.get(url, headers=headers, params=params)
'''
text = response.text
bus_dict = response.json()
print(bus_dict.keys())
print(bus_dict["businesses"])
print(bus_dict["total"])
print(bus_dict["region"])
'''
businesses = response.json()["businesses"]
high_rate_bus = [item["name"]
                 for item in businesses if item["rating"] > 4]
print(high_rate_bus)
