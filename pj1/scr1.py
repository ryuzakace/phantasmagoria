import requests
from bs4 import BeautifulSoup
import sys
import urllib.request 

url1 = "https://xkcd.com/"
frm = int(sys.argv[1])
tu = int(sys.argv[2])

for i in range(frm, tu+1):
    url = url1 + str(i)
    #print(i),
    print ("downloading comic no "+str(i),end = " ")
    re = requests.get(url)
    print(re,end = " ")
    cod = re.text
    soup = BeautifulSoup(cod, "lxml")
    for im in soup.findAll('div',{'id' : 'comic'}):
        img = im.find('img')
        imgurl ="https:" + img.get('src')
        #print(imgurl)
       
        urllib.request.urlretrieve(imgurl,str(i)+".jpg")
        print("Downloaded")
        
    
