import requests
from datetime import datetime

TOKEN = "dbdhcajnjj"
USERNAME = "msfluffy"
GRAPH_ID = "msfluffy695"
date = "20261003"
delete_date = "20261004"
# Create a user
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json = user_params)
# print(response.text)

# Create a graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_params = {
#     "id" : GRAPH_ID,
#     "name" : "Cycling Graph",
#     "unit" : "kms",
#     "type" : "float",
#     "color" : "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_params, headers = headers)
# print(response.text)



# Post a pixel value
today = datetime(year=2026, month=10, day=3)
# print(today) 

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_creation_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" :"12.0"
}

# response = requests.post(url = pixel_creation_endpoint, json = pixel_creation_params, headers = headers)
# print(response.text)

# Update the pixel 
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_pixel_params = {
    "quantity" : "16.5"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

# To delete the pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
