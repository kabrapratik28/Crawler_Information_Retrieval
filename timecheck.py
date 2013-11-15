import time  ## delay for testing
'''
data
'''
import datetime as dt
from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse
from urlparse import urljoin
from reppy.cache import RobotsCache
robots = RobotsCache()         ## creating object for cache robots.txt



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

site_last_time_visit['google.com'] =  dt.datetime.now() 
time.sleep(4)                    ##testing purpose putted sleep 
'''Before url fetched check this time '''
def time_checker(site_name):
#checks time and return 0 or 1 accordingly what to do 
#checks last visit
#check site present or not ** very first task . then if present . not present create . ****time last visit remained in above dataadder function
    
    if site_last_time_visit.has_key(site_name):   ## site visited previously
        time_when_vistied = site_last_time_visit[site_name]  
        time_now  =  dt.datetime.now()
        difference_delta_obj  = time_now - time_when_vistied  
        if difference_delta_obj.days > 0 or difference_delta_obj.seconds >=2 :             #========= PUTTED 2 SECOND GAP +++ ARY HERE IF U WANT DIFFERENT +++++ 
            return 1   ## time is greater than 2 seconds  .... no problem
        else :
            return 0   ## not rite time last time visited is less than 2 seconds
    else : 
        ## do nothing datastorer create when he load the site url  .. he store site last time 
        return 1    ## fine never visited so go ahead 

aa =   time_checker("google.com")
print aa
