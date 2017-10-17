# Session 1(Beautiful soup)
import bs4 as bs #importing beautiful soup4
import urllib.request # To make a request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read() # Source code

soup=bs.BeautifulSoup(sauce,'lxml') # lxml-->parser - Can also use HTML5lib
# Soup-->a beautiful soup object used to interact with the soup
#print(sauce)
#print(soup)
#print(soup.title)  -- > gets the title
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.text)
#print(soup.p)
#print(soup.find_all('p'))
#print(soup.p.text)

#for paragraph in soup.find_all('p'):
#    print(paragraph.text)
# we don't use string as there might be having a child tag in it like <strong>
#So it returns None which is why we prefer using text

#print(soup.get_text()) # used as sometimes websites dont use paragraph tags and use pretags 


#for url in soup.find_all('a'):  # 'a' tag --> hyperlink in HTML
    #print(url)
    #print(url.text)
    #print(url.get('href'))
