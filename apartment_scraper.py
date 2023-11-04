import requests
import json
from bs4 import BeautifulSoup

# Get JSM HTML
jsm_url = "https://jsmliving.com/buildings"
jsm_response = requests.get(jsm_url)
jsm_html_content = jsm_response.content
apt_soup = BeautifulSoup(jsm_html_content, "html.parser")

# Find all the apartment buildings
building_cards = apt_soup.find_all("div", class_="building__card-content")
jsm_locations = []

# Iterate through apartment building divs
for card in building_cards:

    # Getting HTML response of each of these buildings
    location_element = card.find("h2").find("a")
    location = location_element.text.strip()    
    href = location_element["href"]
    location_url = f"https://jsmliving.com{href}"

    # Get HTML response and content
    location_response = requests.get(location_url)
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
