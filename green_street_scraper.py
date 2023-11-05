import requests
import json
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
# Get JSM HTML
gs_url = "https://www.greenstrealty.com/properties/search/area/on-campus/availability/Available%20Now/availability/Available%20August%202024"
gs_response = requests.get(gs_url, headers=headers)
gs_html_content = gs_response.content
apt_soup = BeautifulSoup(gs_html_content, "html.parser")

# Find all the apartment buildings
building_cards = apt_soup.find_all("div", class_="property-item-data-group")
print(building_cards)
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

#     room_elements = location_soup.find_all("article", class_="unit is-promoted teaser clearfix")
#     for layout in room_elements:
#         layout_name = layout.find("h2").find("span")
#         layout_name = layout_name.text.strip()
#         parts = [part.strip() for part in layout_name.split(',')]

#         beds = None
#         baths = None

#         # Iterate through the parts to find beds and baths information
#         for part in parts:
#             if "Beds" in part:
#                 beds = int(part.split()[0])  # Extract the number before "Beds" and convert it to an integer
#             elif "Baths" in part:
#                 baths = int(part.split()[0])  # Extract the number before "Baths" and convert it to an integer

#         info = layout.find_all("td")
#         li_list = []
#         for poop in info:
#             poopy = poop.text.strip()
#             li_list.append(poopy)
#         if len(li_list) >= 3:
#             room_data = [beds, li_list[1], baths]
#             jsm_locations.append([location, room_data])
#         else:
#             pass


    

# print(jsm_locations)
