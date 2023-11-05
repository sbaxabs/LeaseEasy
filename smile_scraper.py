# For biggie bert!
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# Initialize a Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)  # Make sure you have the Chrome WebDriver installed

# Load the webpage
driver.get("https://www.smilestudentliving.com/availability")
time.sleep(3)
# Wait for elements to load (you may need to adjust the wait time)
#wait = WebDriverWait(driver, 200)

#element = wait.until(EC.presence_of_element_located((By.ID, "your_element_id")))

# Get the page source using Selenium
page_source = driver.page_source

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')





# Find all the apartment buildings
building_cards = soup.find_all("div" , class_="listing-item")

    
# print(building_cards)



smile_locations = []


# Iterate through apartment building h2
for card in building_cards:
    
    
    
    # Getting HTML response of each of these buildings
    location_element = card.find("a")
    location = location_element.text.strip()    
    href = location_element["href"]
    location_url = f"https://www.smilestudentliving.com{href}"

    # Get HTML response and content
    
    
    location_name = location_element["aria-label"]
    print(location_url)
    # Load the webpage
    
    driver1 = webdriver.Chrome(options=chrome_options)
    
    time.sleep(2)
    driver1.get(location_url)
    time.sleep(1)

# Continue with other actions

# Optionally, you can also use WebDriverWait after the sleep for additional element-specific waits
    try:
        element = WebDriverWait(driver, 1)
        # Proceed with actions involving the found element
    finally:
        print("all good")
        page_source1 = driver1.page_source
    time.sleep(2)
    # Wait for elements to load (you may need to adjust the wait time)
    
    # Get the page source using Selenium
    #page_source1 = driver1.page_source
    location_soup = BeautifulSoup(page_source1 , "html.parser")

    # Initialize list of bedroom number
    bed_numbers = location_soup.find("div", class_= "feature beds")
    bed_number = bed_numbers.text.strip() 
    

    # Initialize the list of prices
    prices = location_soup.find("div", class_= "rent-info")
    price = prices.text.strip()

    # Initialize the list of bathrooms
    bathroom_number = location_soup.find("div", class_= "feature baths").text.strip()
    
    room_info = [location_name , bed_number, price, bathroom_number]
    print(room_info)
    smile_locations.append(room_info)
driver.quit()

# You can also access specific elements by their attributes, classes, or IDs, like this:
# element = soup.find('div', {'class': 'your-class-name'})
# element_text = element.text

# Close the browser
#driver.quit()
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
                    <p>{data[1]}</p>
                </div>
                <div class="content">
                    <img src="./images/size.svg" alt="">
                    <p>10x10m</p>
                </div>
                <div class="content">
                    <img src="./images/area.svg" alt="">
                    <p>{data[3]}</p>
                </div>
            </div>
            <div class="price">
                <p>{data[2]}</p>
                <a href="" class="booking-btn">Book Now</a>
            </div>
        </div>
    </div>'''
generated_elements = ""
for i in smile_locations:
    product_card = generate_html_element(i)
    generated_elements += "\n"+product_card
print(generated_elements)


# Write the HTML content to a file
with open("smile_output.html", "w", encoding="utf-8") as html_file:
    html_file.write(generated_elements)

