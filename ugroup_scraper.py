import requests
import json
from bs4 import BeautifulSoup
from flask import Flask

# app = Flask(__searcher__)

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
    detail_element = card.find("div", class_="col-lg-6 propert_sm_detail").find("a")
    href = detail_element["href"]
    location_url = href


    # Get HTML response and content
    location_response = requests.get(location_url, headers={"User-Agent": "XY"})
    location_html_content = location_response.content
    location_soup = BeautifulSoup(location_html_content, "html.parser")
    
    # Loop through bedroom tabs
    room_elements = location_soup.find_all("div", class_="tab-content_in_wrapp tab-cntnt_wrap_btm")
    for layout in room_elements:
        info = layout.find_all("div", class_="col-lg-5")
        room = layout.find("div", class_="col-lg-6 tab-content_in_lft popup-gallery").find("h4")
        room_numba = room.text.strip()
        li_list = []
        for poop in info:
            poopy = poop.text.strip()
            li_list.append(poopy)
        if len(li_list) >= 8:
            room_data = [room_numba, li_list[1], li_list[7], location_url]
            ugroup_locations.append([location, room_data])
        else:
            pass
print(ugroup_locations)


def generate_html_element(data):
    # Customize this function to generate the HTML element based on your data
    return f'''<div class="product-card">
        <img src="./images/house1.png" alt="" class="product-img">
        <div class="card-info">
            <div class="card-info-content">
                <img src="./images/location.svg" alt="">
                <p class="loaction-name">{data[0]}</p>
            </div>
            <div class="card-info-content">
                <div class="content">
                    <img src="./images/bed.svg" alt="">
                    <p>{data[1][0]}</p>
                </div>
                <div class="content">
                    <img src="./images/size.svg" alt="">
                    <p>10x10m</p>
                </div>
                <div class="content">
                    <img src="./images/area.svg" alt="">
                    <p>{data[1][2]} Bathroom</p>
                </div>
            </div>
            <div class="price">
                <p>{data[1][1]}</p>
                <a href="{data[1][3]}" class="booking-btn">Book Now</a>
            </div>
        </div>
    </div>'''
generated_elements = ""
for i in ugroup_locations:
    product_card = generate_html_element(i)
    generated_elements += "\n"+product_card
print(generated_elements)


# Write the HTML content to a file
with open("output.html", "w", encoding="utf-8") as html_file:
    html_file.write(generated_elements)






# Items to consider
# Price
# Bedroom Number
# Bathroom Number
# location
# link
# Square footage?

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
# }
# ######UGROUP TIMEEEEEEEEEEE
# ugroup_url = "https://www.smilestudentliving.com/availability"
# ugroup_response = requests.get(ugroup_url, headers=headers)

# location_url = "https://ugroupcu.com/property-details/303-e-chalmers-january-2024/"

# location_response = requests.get(location_url, headers={"User-Agent": "XY"})
# location_html_content = location_response.content
# location_soup = BeautifulSoup(location_html_content, "html.parser")

# # Initialize dictionary that stores a list of Room bedroom types
# room_data = {}

# # Initialize the array to be in the dict
# floorplan = []

# # Loop through bedroom tabs
# room_elements = location_soup.find_all("div", class_="tab-content_in_wrapp tab-cntnt_wrap_btm")
# for layout in room_elements:
#     info = layout.find_all("div", class_="col-lg-5")
#     li_list = []
#     for poop in info:
#         poopy = poop.text.strip()
#         li_list.append(poopy)

#     # room_divs is a list of bed types
#     # Loop through and append text to floorplan array
#     # Make room_data hold location as the key and the floorplan array as the value
#     # Append room_data dictionary to jsm_locations list
# #     for room_div in room_divs:
# #         floorplan.append(room_div.text)
# # room_data = {location:floorplan}
# # ugroup_locations.append(room_data)
