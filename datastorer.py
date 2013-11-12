
from bs4 import BeautifulSoup
import urllib2


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

newobj = Url_class('http://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html')
data_url['http://nlp.stanford.edu'] = [newobj,]

newobj2 = Url_class('http://stackoverflow.com/questions/10858575/find-object-by-its-member-inside-a-list-in-python')
data_url['http://stackoverflow.com'] = [newobj2,]



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
    objecturllib = urllib2.urlopen( at_given_url) 
    htmlcode  =  objecturllib.read()
    soupobject = BeautifulSoup(htmlcode)
    #soupnormalized = soupobject.prettify()
    #print soupnormalized
    if soupobject.title : 
        ##print soupobject.title.string 
        object_url.add_title(soupobject.title.string) 
    ##print soupobject.body.get_text().encode('utf-8') ##printing purpose utf8 conversion 
    object_url.dataadd(soupobject.body.get_text())
    
    #print object_url.url.encode('utf-8')
    #print object_url.title.encode('utf-8') 
    #print object_url.urldata.encode('utf-8')



a = datastorer('http://nlp.stanford.edu' ,'http://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html' )
b =  datastorer('http://stackoverflow.com' ,'http://stackoverflow.com/questions/10858575/find-object-by-its-member-inside-a-list-in-python' )
