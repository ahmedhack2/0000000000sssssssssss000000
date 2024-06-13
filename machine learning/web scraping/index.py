import requests
from bs4 import BeautifulSoup
import csv


page = requests.get("https://www.amazon.com/s?k=iphone")

def main(page):
    src = page.content
    soup =BeautifulSoup(src , "lxml")
    # print(soup)

    products = soup.find_all("div",{'class': 'a-section a-spacing-small a-spacing-top-small'})
    print(products)

    # def get_product_detail(products):
    #     product_title = products.contents[1]
    #     print(product_title)
    # print(get_product_detail(products))
        

main(page)

# / هيطبعلنا كود وهنا يجي دور البارثنج بتاع البيوتفل سوب


# import requests
# from bs4 import BeautifulSoup
# import json

# # Define the URL of the Amazon page you want to scrape
# url = 'https://www.amazon.com'

# # Send a GET request to the URL
# response = requests.get(url)

# # Create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find the HTML elements that contain the product information
# product_elements = soup.find_all('div', {'class': 'puisg-col-inner'})

# # Create an empty list to store the product data
# products = []

# # Iterate over the product elements
# for product_element in product_elements:
#     # Extract the desired information from each product element
#     title_element = product_element.find('span', {'class': 'a-size-medium'})
#     price_element = product_element.find('span', {'class': 'a-offscreen'})
#     rating_element = product_element.find('span', {'class': 'a-icon-alt'})
    
#     # Create a dictionary to store the product data
#     product = {
#         'title': title_element.text.strip() if title_element else '',
#         'price': price_element.text.strip() if price_element else '',
#         'rating': rating_element.text.strip() if rating_element else ''
#     }
    
#     # Add the product dictionary to the list of products
#     products.append(product)

# # Save the products as a JSON file
# with open('products.json', 'w') as file:
#     json.dump(products, file, indent=4)

# # Print a success message
# print('Product data has been scraped and saved as products.json.')