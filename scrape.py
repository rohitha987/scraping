import requests
from bs4 import BeautifulSoup
import csv
import time

url1="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
pages=40
product_data = []

for page in range(1,pages+1):
    url = url1 + f"&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    products = soup.find_all("div", {"data-component-type": "s-search-result"})
    
    for product in products:
        product_url = product.find("a", class_="a-link-normal")["href"]
        product_name = product.find("span", class_="a-text-normal").text
        product_price = product.find("span", class_="a-price-whole").text
        product_rating = product.find("span", class_="a-icon-alt").text.split()[0]
        product_num_reviews = product.find("span", {"class": "a-size-base"}).text.split()[0]
        
        product_data.append([product_url, product_name, product_price, product_rating, product_num_reviews])
    
    time.sleep(2)  
    print(product_data)

with open("product_data1.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews"])
    csvwriter.writerows(product_data)
#Due to the dynamic changes in the website I am unable to scrape other things





