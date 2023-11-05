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

    room_elements = location_soup.find_all("article", class_="unit is-promoted teaser clearfix")
    for layout in room_elements:
        layout_name = layout.find("h2").find("span")
        layout_name = layout_name.text.strip()
        parts = [part.strip() for part in layout_name.split(',')]

        beds = None
        baths = None

        # Iterate through the parts to find beds and baths information
        for part in parts:
            if "Beds" in part:
                beds = int(part.split()[0])  # Extract the number before "Beds" and convert it to an integer
            elif "Baths" in part:
                baths = int(part.split()[0])  # Extract the number before "Baths" and convert it to an integer

        info = layout.find_all("td")
        li_list = []
        for poop in info:
            poopy = poop.text.strip()
            li_list.append(poopy)
        if len(li_list) >= 3:
            room_data = [beds, li_list[1], baths]
            jsm_locations.append([location, room_data])
        else:
            pass

def generate_html_element(data):
    # Customize this function to generate the HTML element based on your data
    return f'''<div class="product-card">
        <img src="./images/jsm.png" alt="" class="product-img">
        <div class="card-info">
            <div class="card-info-content">
                <img src="./images/location.svg" alt="">
                <p class="loaction-name">{data[0]}</p>
            </div>
            <div class="card-info-content">
                <div class="content">
                    <img src="./images/bed.svg" alt="">
                    <p>{data[1][0]} Bedroom</p>
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
                <a href="" class="booking-btn">Book Now</a>
            </div>
        </div>
    </div>'''
generated_elements = ""
for i in jsm_locations:
    product_card = generate_html_element(i)
    generated_elements += "\n"+product_card
print(generated_elements)


# Write the HTML content to a file
with open("jsm_output.html", "w", encoding="utf-8") as html_file:
    html_file.write(generated_elements)







    # # Loop through bedroom tabs
    # room_elements = location_soup.find_all("div", class_="views-element-container form-group")
    # for parent_div in room_elements:
    #     room_divs = parent_div.find_all('div', class_=lambda x: x and "unit__bedrooms-button js" in x and 'js-' in x)

    #     # room_divs is a list of bed types
    #     # Loop through and append text to floorplan array
    #     # Make room_data hold location as the key and the floorplan array as the value
    #     # Append room_data dictionary to jsm_locations list
    #     for room_div in room_divs:
    #         floorplan.append(room_div.text)
    #     room_data = [location,floorplan]
    #     jsm_locations.append(room_data)