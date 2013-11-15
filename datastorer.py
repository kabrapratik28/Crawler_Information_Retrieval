import datetime as dt
from bs4 import BeautifulSoup
import urllib2
import re

'''
data
'''

class Url_class  :
    def __init__(self , url ):
		self.url = url
		self.anchor = []
                self.anchor_win = []
                self.title = ""
                self.urldata = "" 
    def add_anchor(self,anchortext,ancwintext):
    	self.anchor.append(anchortext)
        self.anchor_win.append(ancwintext)
    def add_title(self,titletext):
        self.title =  titletext 
    def dataadd  (self,datatext):
        self.urldata = datatext


url_fecher_queue = []   #['http://asd.com/ddd','http://asd.com/fff']
visited_site_url = {}	 # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }
data_url = {}             #{site : [urlobject1 , .... ]}  ##urrl object => url,anchor,anchor window,metachar,main text
site_last_time_visit ={}       # {'http://asd.com':time(), .... }
site_current_url_remain = {}   # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }

newobj = Url_class('http://rediff.com')
data_url['http://rediff.com'] = [newobj,]

newobj2 = Url_class('http://w3schools.com/html/default.asp')
data_url['http://w3schools.com'] = [newobj2,]

newobj3 = Url_class('http://prat.com/questions/10858575/find-object-by-its-member-inside-a-list-in-python')
data_url['http://prat.com'] = [newobj3,]


'''Data store to already created object when site marked as visited'''
def datastorer(site , at_given_url):      # return beautifulsoup string                   *** # at exception return 0 
# on that url that page text saved , title , meta character also saved  
# beautiful soap used for url
# try and catch used (broken url)
# url stored in dictionary and returns for further use of link on that page
# modify time visit of that site 
    listofobject = data_url[site] 
    list_of_one_object =  filter(lambda x: x.url ==at_given_url , listofobject)
    object_url = list_of_one_object[0]
    ##open page and give to beautiful soup
    try : 
        objecturllib = urllib2.urlopen( at_given_url)
        site_last_time_visit[site] = dt.datetime.now()
        htmlcode  =  objecturllib.read()
        soupobject = BeautifulSoup(htmlcode)
        #soupnormalized = soupobject.prettify()
        #print soupnormalized
        if soupobject.title : 
            ##print soupobject.title.string 
            object_url.add_title(soupobject.title.string) 
        ##print soupobject.body.get_text().encode('utf-8') ##printing purpose utf8 conversion 
        new_modified_string  =  re.sub('\s+',' ', soupobject.body.get_text())                        ##  addded .... remove extra spaces and new lines
        object_url.dataadd(new_modified_string)
        #print new_modified_string.encode('utf-8')
        return  soupobject
    except Exception :
        object_url.dataadd("Error : Url is broken !!!")
        return 0 
    #print object_url.url.encode('utf-8')           
    #print object_url.title.encode('utf-8')               
    #print object_url.urldata.encode('utf-8')
    


a = datastorer('http://rediff.com' ,'http://rediff.com' )
b =  datastorer('http://w3schools.com' ,'http://w3schools.com/html/default.asp' )
c =  datastorer('http://prat.com' ,'http://prat.com/questions/10858575/find-object-by-its-member-inside-a-list-in-python' )


for link in a.body.find_all('a'):
	if link.get('href') :     
			print(link.get('href'))

for link in b.body.find_all('a'):
	if link.get('href') : 
			print(link.get('href'))

#print a.find_all('a')
#print b.find_all('a')
#print c   ##return  0   
print site_last_time_visit
