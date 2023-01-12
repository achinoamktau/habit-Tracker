import requests
from datetime import datetime

USERNAME = "your_own_user_name"
TOKEN = "your_own_token"
headers = {     # securing our authentication
    "X-USER-TOKEN": TOKEN
}

# ------------------creating a new user ---------------------------------------------
# these lines are creating a new user to the pixie thing only by python
# if we try to run this thing again than it will show user already exists
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,   # this is really our username and token
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# ----------------------------------------------------------------------

# ------------------------creating a graph----------------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

params_graph = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint,json=params_graph, headers=headers)
# ----------------------------------------------------------------

# ------------posting a pixel---------------------------------------------
today = datetime.now()
today = today.strftime("%Y%m%d")
insert_params = {
    "date": today,   # strftime formats the date in any way you like
    "quantity": input("How many Km did you cycle today? ")
}

insert_graph_endpoint = f"{graph_endpoint}/graph1"
response = requests.post(url=insert_graph_endpoint, json=insert_params, headers=headers)
# ---------------------------------------------------------------------


# --------------------updating a pixel (put)----------------------------------
update_endpoint = f"{insert_graph_endpoint}/{today}"
update_pixels_params = {
    "quantity": "10.9"
}
# response = requests.put(url=update_endpoint, json=update_pixels_params, headers=headers)
# print(response.text)
#------------------------------------------------------------------------

# -------------------------deleting a pixel------------------------------
delete_endpoint = f"{update_endpoint}"
# response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)