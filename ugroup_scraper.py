import requests
import json
from bs4 import BeautifulSoup

######UGROUP TIMEEEEEEEEEEE
ugroup_url = "https://ugroupcu.com/building-list/"
ugroup_response = requests.get(ugroup_url, headers={"User-Agent": "XY"})

ugroup_html_content = ugroup_response.content
ugroup_soup = BeautifulSoup(ugroup_html_content, "html.parser")

# Find all the apartment buildings
ugroup_cards = ugroup_soup.find_all("div", {"class":"property-list-box flex"}) #Possibly property-list-box flex
ugroup_locations = []

# Iterate through apartment building divs
for card in ugroup_cards:

    # Getting HTML response of each of these buildings
    location_element = card.find("div", class_="col-lg-6 propert_sm_detail").find("h3")
    location = location_element.text.strip() 
    print(location)   
    detail_element = card.find("div", class_="col-lg-6 propert_sm_detail").find("a")
    href = detail_element["href"]
    location_url = {href}
    print(location_url)
    ugroup_locations.append(location_url)

    # Get HTML response and content
    location_response = requests.get(location_url, headers={"User-Agent": "XY"})
    location_html_content = location_response.content
    location_soup = BeautifulSoup(location_html_content, "html.parser")

    # Initialize dictionary that stores a list of Room bedroom types
    room_data = {}

    # Initialize the array to be in the dict
    floorplan = []

    # Loop through bedroom tabs
    room_elements = location_soup.find_all("div", class_="views-element-container form-group")
    for parent_div in room_elements:
        room_divs = parent_div.find_all('div', class_=lambda x: x and "unit__bedrooms-button js" in x and 'js-' in x)

        # room_divs is a list of bed types
        # Loop through and append text to floorplan array
        # Make room_data hold location as the key and the floorplan array as the value
        # Append room_data dictionary to jsm_locations list
        for room_div in room_divs:
            floorplan.append(room_div.text)
    room_data = {location:floorplan}
    jsm_locations.append(room_data)


# Items to consider
# Price
# Bedroom Number
# Bathroom Number
location
link
Square footage?

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
######UGROUP TIMEEEEEEEEEEE
ugroup_url = "https://www.smilestudentliving.com/availability"
ugroup_response = requests.get(ugroup_url, headers=headers)