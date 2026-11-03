from bs4 import BeautifulSoup


with open("data/details.html" , "r" , encoding ="utf-8") as html_file :
     content = html_file.read()
Soup = BeautifulSoup(content,'html.parser') 
tags = Soup.find_all('h2')

for tag in tags:
  print(tag.text)

headings = Soup.find('h1')
print(headings.text)
libs = Soup.find_all('span' , class_="n")
for lib in libs :
    print(lib.text)


list = Soup.find_all('li')
for li in list:
    print(li.text)