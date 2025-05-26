from bs4 import BeautifulSoup
import pandas as pd
import requests
import html



count = 0
data = []
BASE_URL = "https://books.toscrape.com/"
def scrape_books(url):
    global count
    result = {"Name": [], "Star-Rating": [], "Price": []}
    html_text = requests.get(url)
    html_text.encoding = 'utf-8'
    soup = BeautifulSoup(html_text.text, 'html.parser')
    names = soup.select("a[title]")
    ratings = soup.select("p.star-rating")
    prices = soup.select("p.price_color")
    for name, rating, price in zip(names,ratings,prices):
        print(f"Name: {name.text}")
        star_rating = rating.get('class')
        print(f"Star Rating: {star_rating[1]}")
        print(f"Price: {price.text}")
        print("\n")
        count += 1
        result["Name"].append(name.text)
        result["Star-Rating"].append(star_rating[1])
        result["Price"].append(price.text)
    return result



for i in range (3):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    page_data = scrape_books(url)
    df_page = pd.DataFrame(page_data)
    data.append(df_page)

df = pd.concat(data, ignore_index=False)
df.to_csv("project_output3.csv",index=False, encoding='utf-8-sig')
print(count)
    
