# For biggie bert!
import requests
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
######SMILE TIMEEEEEEEEEEE
smile_url = "https://www.smilestudentliving.com/availability"
smile_response = requests.get(smile_url, headers=headers)
print(smile_response.status_code)
smile_html_content = smile_response.content
apt_soup = BeautifulSoup(smile_html_content, "html.parser")
print(smile_html_content)
# Find all the apartment buildings
building_cards = apt_soup.find_all("div", class_="listing-item")
smile_locations = []
print(building_cards)

# Iterate through apartment building h2
for card in building_cards:

    # Getting HTML response of each of these buildings
    location_element = card.find("a").find("slider-link")
    location = location_element.text.strip()    
    href = location_element["href"]
    location_url = f"https://www.smilestudentliving.com{href}"

    # Get HTML response and content
    location_response = requests.get(location_url)
    location_html_content = location_response.content
    location_soup = BeautifulSoup(location_html_content, "html.parser")
    location_name = location_element["aria-label"]

    # Initialize list of bedroom number
    bed_numbers = location_soup.find("div", class_= "feature beds")
    bed_number = bed_numbers.text.strip() 
    

    # Initialize the list of prices
    prices = location_soup.find("div", class_= "rent-info")
    price = prices.text.strip()

    # Initialize the list of bathrooms
    bathroom_number = location_soup.find("div", class_= "feature baths")
    
    room_info = [location_name , bed_number, price, bathroom_number]
    print(room_info)
    smile_locations.append(room_info)