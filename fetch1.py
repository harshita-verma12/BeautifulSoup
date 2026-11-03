import requests

def fetchandsave(url,path): 
    r = requests.get(url)
    with open(path,"w",encoding ="utf-8") as f:
        f.write(r.text)

url = "https://www.geeksforgeeks.org/python/libraries-in-python/"

r = requests.get(url)


fetchandsave(url,"data/details.html")


