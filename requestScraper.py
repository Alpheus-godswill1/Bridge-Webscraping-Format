from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.jumia.com.ng/men-sneakers/adidas/'

html_file = requests.get(url)
soup = BeautifulSoup(html_file.text, 'lxml')

tags = soup.select('article.prd._fb.col.c-prd')

# Create an empty list to store the scraped data
data = []

# Iterate over the product elements and extract relevant information
for product in tags:
    # name = product.select_one('a.core')['title'].strip()  # Selector for product name
    price = product.select_one('div.price-box')  # Selector for product price

    # Create a dictionary to store the data for each product
    product_data = {
        # 'name': name,
        'price': price,
    }

    # Append the product data to the list
    data.append(product_data)

# Save the data in JSON format
with open('scraped_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Scraping complete. Data saved in scraped_data.json.')
