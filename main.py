# Scrapper Version: 1.0 - Basic
# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.example.com'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all links on the page
# links = []
# for link in soup.find_all('a'):
#     links.append(link.get('href'))

# # Find all images on the page
# images = []
# for img in soup.find_all('img'):
#     images.append(img.get('src'))

# # Print the results
# print("Links:")
# for link in links:
#     print(link)

# print("\nImages:")
# for image in images:
#     print(image)





# Scrapper Version: 1.0.1 - Basic with Save to CSV
# import csv
# import requests
# from bs4 import BeautifulSoup

# # define the URL to scrape
# url = 'https://www.example.com'

# # make a GET request to the URL
# response = requests.get(url)

# # create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')

# # find the elements you want to scrape
# data = []
# for item in soup.find_all("div", {"class": "bluray-class"}):
#     # extract the data you want
#     name = item.find("h2").text.strip()
#     description = item.find("p").text.strip()
#     data.append([name, description,])

# # save the data to a CSV file
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Description"])
#     for row in data:
#         writer.writerow(row)



# Scrapper Version: 1.0.2 - Advanced
# import csv
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Set the URL of the first page to scrape
# # url = 'https://www.example.com'

# # Create an empty DataFrame to store the data
# data = pd.DataFrame(columns=['Title', 'Description'])

# # Loop through all pages of the website
# while url is not None:

#     # Send a GET request to the page
#     response = requests.get(url)

#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all the items on the page
#     items = soup.find_all('div', class_='item')

#     # Extract the data from each item and add it to the DataFrame
#     for item in items:
#         title = item.find('h2').text.strip()
#         description = item.find('p').text.strip()
#         data = data.append({'Title': title, 'Description': description}, ignore_index=True)

#     # Find the URL of the next page, if it exists
#     next_link = soup.find('a', class_='next')
#     if next_link is not None:
#         url = next_link.get('href')
#     else:
#         url = None

# # Save the data to a CSV file
# data.to_csv('output.csv', index=False)




# Scrapper Version: 1.0.3 - Amended Basic with Save to CSV
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# Find all images on the page
images = []
for img in soup.find_all('img'):
    images.append(img.get('src'))

# Write the results to a CSV file
with open('links_and_images.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Links'])
    for link in links:
        writer.writerow([link])
    writer.writerow([])
    writer.writerow(['Images'])
    for image in images:
        writer.writerow([image])

print("Results written to links_and_images.csv")
