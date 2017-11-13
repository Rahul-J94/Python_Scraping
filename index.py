import requests
import bs4
import re

response = requests.get('https://www.kingdomsg.com/kingdomsg2018')
soup = bs4.BeautifulSoup(response.text, "html.parser")
#soup1 = bs4.BeautifulSoup(response.text, "html.parser")
#links = soup.select('img[src]')
#links = [img.attrs.get('src') for img in soup.select('img')]
#for rdx , val in enumerate(links):
#    print (rdx,val)
#    print (">>")
#print (links)
#print (response.text)

#list = []
#title = soup.find_all("div", class_=re.compile("^guaranteed"))
#for tm , val in enumerate(title):
#    print (tm, val)
#    print (".....")

print ("__________________________________________")
#for h3 in title:
#    for h3ind in h3.find_all('h3'):
#        print (h3ind)
#        print (">>>>>>>")

#print (title)
print ("++++++++++++++++++++++++++++++++++++++++++")
#print (list)

r = requests.get('https://www.kingdomsg.com/kingdomsg2018')
data = r.text
soup = bs4.BeautifulSoup(data, "html.parser")
list_to_ignore = ["https://www.kingdomsg.com","https://www", "http://", "https://"]
ignore = ["callto:+61299049225", "mailto:info@kingdomsg.com", "javascript:void(0)"]
link_list = []
#for i in soup.find_all('a').length():
for link in soup.find_all('a'):
    print ("{{{{{{{{{")
    print (link.get('href'))
    link_list.append(link.get('href'))
    if str(link.get('href')).startswith(tuple(list_to_ignore)):
        p = requests.get(link.get('href'))
        data1 = p.text
        soup1 = bs4.BeautifulSoup(data1, "html.parser")
        for p in soup1.find_all('a'):
            #print(p.get('href'))
            link_list.append(p.get('href'))
    elif str(link.get('href')) in ignore :
        print ("Encountred")
    else:
        p = requests.get("https://www.kingdomsg.com" + link.get('href'))
        data2 = p.text
        soup2 = bs4.BeautifulSoup(data2, "html.parser")
        for p in soup2.find_all('a'):
            #print(p.get('href'))
            link_list.append(p.get('href'))

#print(link_list)

print ("|||||||||||||||||||||||||||||||||||||||||")
print (list(set(link_list)))
y = list(set(link_list))
file = open('text.txt', 'w')

for i in y:
    file.write("%s\n" % i)


#for link in soup.find_all('a'):
#    print(link.get('href'))


