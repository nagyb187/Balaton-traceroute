import urllib
import urllib.request
from bs4 import BeautifulSoup

def removedupl(x):
  return list(dict.fromkeys(x))


link = "https://www.met.hu/idojaras/tavaink/balaton/mert_adatok/main.php?c=tablazat&v=Balatonaliga"
f = urllib.request.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile,"html5lib")
text = soup.get_text(" ")
#print (text)

data = {}
time = []
winddir = []
windsp = []
for tag in soup.findAll(onmouseover=True):
    datatosearchin = tag['onmouseover']
    #print (datatosearchin)
    if datatosearchin.find("UTC") != -1:
        tmpdata = datatosearchin.split(" ")
        time.append(tmpdata[4])
    elif datatosearchin.find("wind") != -1:
        tmpdata = datatosearchin.split("<")
        del tmpdata[0:3]
        del tmpdata[2:4]
        tmpdata[0] = tmpdata[0].replace("br>", "")
        tmpdata[1] = tmpdata[1].replace("br>(", "")
        tmpdata[1] = tmpdata[1].replace(")", "")
        tmpdata[1] = tmpdata[1].replace("/div>","NaN")
        #print(tmpdata)
        winddir.append(tmpdata)
    elif datatosearchin.find("spacer") != -1:
        tmpdata = datatosearchin
        print(tmpdata)
        winddir.append(['-','NaN'])
    elif datatosearchin.find("km/h") != -1:
        tmpdata = datatosearchin
        tmpdata = tmpdata.replace("Tip('<div class=ikon-title>","")
        tmpdata = tmpdata.replace("</div>')","")
        windsp.append(tmpdata)


k = len(winddir) - 1
while k >= 0:
    del winddir[k]
    k -= 2
    #print(k)

time.pop()
print (time)
print(len(time))

print(winddir)
print(len(winddir))

print(windsp)
print(len(windsp))
      
balatonaliga = []
i = 0
for line in time:
    balatonaliga.append([line, winddir[i], windsp[i], winddir[i+1], windsp[i+1]])
    i += 2
    
balatonaliga.insert(0, ["Idő", "Széllökés irány", "Széllökés sebesség", "Átlagszél irány", "Átlagszél sebesség"])
for item in balatonaliga:
    print(item)
