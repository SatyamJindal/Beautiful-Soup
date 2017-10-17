# Session 2(Beautiful Soup)
import bs4 as bs #importing beautiful soup4
import urllib.request # To make a request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read() # Source code

soup=bs.BeautifulSoup(sauce,'lxml') # lxml-->parser - Can also use HTML5
#Soup is basically a beautiful soup object which lets us interact with the soup

nav = soup.nav # navigation bar at the top
#print(nav)

#for url in nav.find_all('a'):
#    print(url.get('href'))
#the output shows two times as there is a side bar after minimizing the screen

body=soup.body
#print(body)
#for paragraph in body.find_all('p'):
#    print(paragraph.text)
# but there might be a div section

#for div in soup.find_all('div'): # But this gives everything which we do not need
#    print(div.text)

#So we define a class
#for div in soup.find_all('div',class_='body'):
#    print(div.text)
