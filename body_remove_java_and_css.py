from bs4 import BeautifulSoup


soupobject = BeautifulSoup(open('z.html'))
        #soupnormalized = soupobject.prettify()
        #print soupnormalized
nouse = [xjs.extract() for xjs in soupobject.findAll(['script', 'style'])]
print (soupobject.body.get_text()).encode('utf-8')
        
