import requests
import json
from bs4 import BeautifulSoup

# # Get JSM HTML
# jsm_url = "https://jsmliving.com/buildings"
# jsm_response = requests.get(jsm_url)
# jsm_html_content = jsm_response.content
# apt_soup = BeautifulSoup(jsm_html_content, "html.parser")

# # Find all the apartment buildings
# building_cards = apt_soup.find_all("div", class_="building__card-content")
# jsm_locations = []

# # Iterate through apartment building divs
# for card in building_cards:

#     # Getting HTML response of each of these buildings
#     location_element = card.find("h2").find("a")
#     location = location_element.text.strip()    
#     href = location_element["href"]
#     location_url = f"https://jsmliving.com{href}"

#     # Get HTML response and content
#     location_response = requests.get(location_url)
#     location_html_content = location_response.content
#     location_soup = BeautifulSoup(location_html_content, "html.parser")

#     # Initialize dictionary that stores a list of Room bedroom types
#     room_data = {}

#     # Initialize the array to be in the dict
#     floorplan = []

#     # Loop through bedroom tabs
#     room_elements = location_soup.find_all("div", class_="views-element-container form-group")
#     for parent_div in room_elements:
#         room_divs = parent_div.find_all('div', class_=lambda x: x and "unit__bedrooms-button js" in x and 'js-' in x)

#         # room_divs is a list of bed types
#         # Loop through and append text to floorplan array
#         # Make room_data hold location as the key and the floorplan array as the value
#         # Append room_data dictionary to jsm_locations list
#         for room_div in room_divs:
#             floorplan.append(room_div.text)
#     room_data = {location:floorplan}
#     jsm_locations.append(room_data)

######UGROUP TIMEEEEEEEEEEE
ugroup_url = "https://ugroupcu.com/apartment-search/"
ugroup_response = requests.get(ugroup_url, headers={"User-Agent": "XY"})

ugroup_html_content = ugroup_response.content
ugroup_soup = BeautifulSoup(ugroup_html_content, "html.parser")

# Find all the apartment buildings
ugroup_cards = ugroup_soup.find_all("div", class_="property-list-box flex") #Possibly property-list-box flex
print(ugroup_cards)
ugroup_locations = []

# for card in ugroup_cards:
    # print(card)

# # Iterate through apartment building divs
# for card in ugroup_cards:

#     # Getting HTML response of each of these buildings
#     location_element = card.find("h3")
#     location = location_element.text.strip()    
#     detail_element = card.find("div", class_="romm-list").find("a")
#     href = detail_element["href"]
#     location_url = {href}
#     print(location_url)
#     ugroup_locations.append(location_url)

# print(ugroup_locations)

# #     # Get HTML response and content
# #     location_response = requests.get(location_url)
# #     location_html_content = location_response.content
# #     location_soup = BeautifulSoup(location_html_content, "html.parser")

# #     # Initialize dictionary that stores a list of Room bedroom types
# #     room_data = {}

# #     # Initialize the array to be in the dict
# #     floorplan = []

# #     # Loop through bedroom tabs
# #     room_elements = location_soup.find_all("div", class_="views-element-container form-group")
# #     for parent_div in room_elements:
# #         room_divs = parent_div.find_all('div', class_=lambda x: x and "unit__bedrooms-button js" in x and 'js-' in x)

# #         # room_divs is a list of bed types
# #         # Loop through and append text to floorplan array
# #         # Make room_data hold location as the key and the floorplan array as the value
# #         # Append room_data dictionary to jsm_locations list
# #         for room_div in room_divs:
# #             floorplan.append(room_div.text)
# #     room_data = {location:floorplan}
# #     jsm_locations.append(room_data)


# # Items to consider
# # Price
# # Bedroom Number
# # Bathroom Number
# location
# link
# Square footage?

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
######UGROUP TIMEEEEEEEEEEE
ugroup_url = "https://www.smilestudentliving.com/availability"
ugroup_response = requests.get(ugroup_url, headers=headers)