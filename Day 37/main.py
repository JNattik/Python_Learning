import requests, datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "nittakj"
TOKEN = "uiopqaubfnwon"

parameters = {
    "token": TOKEN,    # can be random
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.date.today()

value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

#response = requests.post(url=value_endpoint, json=value_config, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

response = requests.delete(url=update_endpoint, headers=headers)

print(response.text)