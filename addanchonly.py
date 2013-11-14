
from bs4 import BeautifulSoup
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

visited_site_url['apra.com'] = ['http://apra.net/telegraphic'  , ]
aa = Url_class('http://apra.net/telegraphic')
data_url['apra.com'] = [aa  , ]
aa.add_anchor('anchortext','ancwintext')



''' If duplicate url then ... and add to object created already '''
def add_anchor_only(site, url , anchor , anchor_window):
#add anchor of given url bz it done before jst add anchor  AND anchor window
#add in data_url dictionary at key site and in list for normalized_absolute_url
    all_url_rel = data_url[site]
    list_of_one_url_of_site =  filter(lambda mm: mm.url == url ,all_url_rel )
    one_url_gotted_obj = list_of_one_url_of_site[0] 
    one_url_gotted_obj.add_anchor(anchor , anchor_window)




add_anchor_only('apra.com', 'http://apra.net/telegraphic' , "hi hello " , 'anc _ winnn ')
print aa.anchor
print aa.anchor_win
