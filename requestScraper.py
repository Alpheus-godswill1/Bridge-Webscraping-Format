from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.jumia.com.ng/mens-casual-button-down-shirts/'

html_file = requests.get(url)
soup = BeautifulSoup(html_file.text, 'lxml')

cloths = soup.find_all('article', class_='prd _fb col c-prd')

data_positions = []  # List to store the data-position values

for cloth in cloths:
    href = cloth.find('a', class_='core')
    data_position = href.get('data-position')
    data_positions.append(data_position)  # Append the data-position value to the list

print(data_positions)


# Create an empty list to store the scraped data
# data = []

# # Iterate over the product elements and extract relevant information
# for product in Tags:
#     VerifiedPurchases = soup.find('h2', '-fs14 -m -upp -ptm').text 
#     NumbOfGoodsPurchased = soup.find('div', 'stars _m _al -mvs').text.strip() 
#     ReviewTitle = soup.find('h3', '-m -fs16 -pvs').text
#     Reviews = soup.find('p','-pvs').text
#     DateOfReview = soup.find('span', '-prs').text
#     DateAndReviewersName = soup.find('div', '-df -j-bet -i-ctr -gy5').text
#     PurchaseStatus = soup.find('div', '-df -i-ctr -gn5 -fsh0').text
    
    
#     # Create a dictionary to store the data for each product
#     product_data = {
#         'Product Name': "",
#         'Product Brand': "",
#         'Product Price': "",
#         'Product Verified Ratings' : "",
#         'Verified Purchase': "",
#         'Number Of Item Purchased(Sales)': "",
#         'Review Title': "",
#         'Customer Review (Comment)': "",
#         'Date Of Review ': "",
#         'Purchase Status': ""
#     }

#     # Append the product data to the list
#     data.append(product_data)

# # Save the data in JSON format
# with open('scraped.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# print('Scraping complete. Data saved in scraped_data.json.')
