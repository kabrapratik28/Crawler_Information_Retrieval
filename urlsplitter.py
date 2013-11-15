import urllib2
from urlparse import urlparse
from urlparse import urljoin


'''
url data
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


def url_splitter(fullurl):  ## in main this require bz every url function require site name and url 
##url splitted returns two parts 1.main domain 2. full url 
    site_and_rel   = urlparse( fullurl ) 
    return site_and_rel.netloc    ## site name without http ... :)  ..... ##**** PROBLEM ON FTP PROTOCOL


a = url_splitter("http://google.com/asd/bcs/kkk") 
print a
