#import the library
from requests_html import HTMLSession

# create a new session
session = HTMLSession()

# open a website
r = session.get("https://www.lwhs.org/page")

print(r) # returns if it was able to open the page or not

titles = r.html.find(".event-title")

for title in titles:
    print(title) # prints out the entire tag
    print(title.text) # prints out the text inside the tag



r = session.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=drugs")

# find the box by using the class we found
items = r.html.find(".item-content")

for item in items:
  # now we have the whole item
  print(item) #returns \<Element 'div' class=('item-content',)\> showing we're getting an element

  # we find the price class in the item .text
  price = item.find(".price", first=True)
  print(type(price))
  for prices in price:
      print(prices)
  # print(str(price["b"]))
  # we find the title
  title = item.find(".title", first=True).text()

  print(title + " costs " + price) # returns Pain Pills Raw... costs $1.00
