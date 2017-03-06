import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.ca/search?find_desc=Restaurants&find_loc=Sherwood+Park%2C+AB&ns=1"

yelp_r = requests.get(url)
print(yelp_r.status_code)

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

#print(yelp_soup.prettify())
#print(yelp_soup.findAll('a'))

# Pull Page Title
#print ("\nThe Page Title is: " + yelp_soup.title.text)

#for link in yelp_soup.findAll('a'):
#    print(link.get('href'))

print(yelp_soup.find("div", class_="secondary-attributes"))
print(yelp_soup.find_all("title"))
