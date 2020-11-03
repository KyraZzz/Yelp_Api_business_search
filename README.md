# Yelp_api_business
Find the information of business using the Yelp API according to a location.

### Idea:
It is great if we can hang out with friends for a Sunday brunch or dinner. However, I do not want to spend a lot of time searching for the restaurants on Tripadvisor. So I would like to create a search program to filter the list of restaurants in Cambridge, Cambridgeshire, the UK which has a high review rate.

# What is an API?
**API** stands for application programming interface, it enables different applications to communicate and interact with each other. Think about the google map you get from the Airbnb app whenever you are booking a stay, google map has provided an API to be used in the Airbnb app.

# Yelp Fusion
[Link for Yelp Fusion Website](https://www.yelp.com/developers)
**Yelp** provides various API to connect customers and businesses. It holds a database which stores business around the world and customers can utilise the APIs to interact with **Yelp's database** and extract information about businesses such as `name`, `review_count`, `categories`, `rating`, `price`, `location` etc.

# Aim:
* Utilise Yelp API to do a business search

# Steps:
1. Create an App on Yelp's Developers site to obtain a private API key. **Note that the private API key has to be hidden if you want to publish on an opensource platform like Github**(I will mention the steps to hide the key in the later sections)
2. Authenticate API calls with the API Key. There are several rules in **Authentication** which we need to take care of(read the Authentication documentation for more details).
3. Start interacting with the API to do a business search.

## Step 1: Create an App on Yelp's Developers site to obtain a private API key
After creating an APP, you will get a **client ID** and an **API key**.

``` python
import requests
import config  # hide the API key to ensure the safety
```
Create a python file called `config.py` to store your **API Key**, then import the file into the main python file (in my case, `app.py`)

Go to the `business endpoints` section on **Yelp fusion**, copy down the URL(https://api.yelp.com/v3/businesses/search) for a business search request. For later usage, I created a new variable to store the URL.
``` python
url = "https://api.yelp.com/v3/businesses/search"
```

## Step 2: Authenticate API calls with the API Key
When we are requesting a visit to the API, it will authenticate our identity and privilege. According to the [Authentication documentation](https://www.yelp.com/developers/documentation/v3/business_search), The `requests.get()` function requires at least 3 parameters: a URL, a header and a list of filtering arguments. For the filtering argument list, a location or the equivalent latitude and longitude are required. This can help **Yelp API** to locate the list of business in the target area.

``` python
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "food",
    "location": "Cambridge"
}
response = requests.get(url, headers=headers, params=params)
```

## 3. Start interacting with the API to do a business search.
Let us have a look at the response:
```python
text = response.text # gives us a string object
bus_dict = response.json() # gives us a dictionary object
```
Since we want to do a business search, the `response.json()` is much more helpful than the previous one. So what does the `bus_dict` store?
``` python
print(bus_dict.keys())
dict_keys(['businesses', 'total', 'region'])

# print(bus_dict["businesses"]) this piece of codes gives us a list of dictionaries which stores the detailed information for each business.

print(bus_dict["total"])
494

print(bus_dict["region"])
{'center': {'longitude': 0.1146697998046875, 'latitude': 52.20419549090858}}
```
Hence, we only care about the `bus_dict["businesses"]` section of the dictionary.

``` python
businesses = response.json()["businesses"]
high_rate_bus = [item["name"]
                 for item in businesses if item["rating"] > 4]
print(high_rate_bus)
```
We use a `list comprehension` technique to compress the length of the code: `[expression for an item in list if ...]`. Here we want to search for the name of the restaurants which has a `rating > 4` (indicates a fair restaurant).

Here is our result:
```
['Pint Shop', 'Noodles Plus', 'The Ivy Cambridge Brasserie', 'MillWorks', 'The Trailer of Life', 'Bread and Meat', 'Honest Burgers Cambridge', 'Bibimbap House', 'The Senate', 'Butch Annies', 'Golden House']
```

# Extension ideas:
There are more things we can do for interaction with APIs, what about creating a react app to set up our self-owned review system! More to come...

