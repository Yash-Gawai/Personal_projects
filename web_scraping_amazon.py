from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd

# Connect to a website

URL = "https://www.amazon.in/Asian-shoes-Running-Firozi-Indian/dp/B01N54ZM9W/ref=sr_1_5?keywords=shoe&qid=1639122113&sr=8-5"
 # Get the header from https://httpbin.org/get
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}

page = requests.get(URL, headers=headers)
# Get all the data from the page that can be found using inspect element in a browser
soup1 = BeautifulSoup(page.content,"html.parser")
 # To format it better
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# To pull a specific data
# Right click > Inspect > span id : <---this is the id used here
title = soup2.find(id = "productTitle").get_text()

fit = soup2.find(id = "fitRecommendationsLinkRatingText").get_text()
# To add the date
today1 = datetime.date.today()
print(today1)

print(title.strip())  # Strip is used here to remove anything useless like extra spaces around the main data
print(fit.strip())

# To make it into a csv file
header = ["title","fit","date"]
data = [title,fit,today1]
#type(data) # Important to know what type of the vairable data is

#with open("Amazon_dataset.csv", "w", newline="",encoding="UTF8") as f:
    #writer = csv.writer(f)
    #writer.writerow(header)   # For initial import of data into the csv
    #writer.writerow(data)


# Creating a df or data frame in pandas
df = pd.read_csv(r"C:\Users\yashg\Desktop\Programming\Python\Amazon_dataset.csv")
print(df)


with open("Amazon_dataset.csv","a+",newline="" ,encoding="UTF8") as f: # a+ for appending the data to the next empty cell
    writer = csv.writer(f)   # For initial import of data into the csv
    #writer.writerow(header)
    writer.writerow(data)

