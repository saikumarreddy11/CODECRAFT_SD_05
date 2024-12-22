import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target URL (replace with your chosen website)
url = "https://books.toscrape.com/"

# Send an HTTP request to the URL
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize empty lists to store data
product_names = []
prices = []
ratings = []

# Extract product information
for product in soup.select(".product_pod"):
    # Extract product name
    name = product.h3.a["title"]
    product_names.append(name)

    # Extract product price
    price = product.select_one(".price_color").text
    prices.append(price)

    # Extract product rating
    rating = product.select_one(".star-rating")["class"][1]  # Get the rating class
    ratings.append(rating)

# Save the data to a CSV file
data = {
    "Product Name": product_names,
    "Price": prices,
    "Rating": ratings
}
df = pd.DataFrame(data)
df.to_csv("products.csv", index=False)

print("Scraping completed. Data saved to products.csv")
