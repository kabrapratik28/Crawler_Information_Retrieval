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



'''Back queue lenght is less than 3'''
def back_queue_feeder():
#fill back queue 
#check queue lenght if greater than 3 dont do anything
#if smaller then go through all dictionary site_current_url_remain keys pop 1 element (remove from queue)
#if list remaining 1 element then pop and delete that list and key from dictionary

# if dictionary is empty then ????    ...end of crawl 
    if len(url_fecher_queue)== 0  : 
        if len(site_current_url_remain):
                  dellist = []
                  for eachsite in site_current_url_remain : 
                        if len(site_current_url_remain[eachsite]) > 1 :
                            tempvar = site_current_url_remain[eachsite].pop(0)
                            url_fecher_queue.append(tempvar)
                        else : 
                            tempvar = site_current_url_remain[eachsite].pop(0)
                            url_fecher_queue.append(tempvar)
                            dellist.append(eachsite)
                  for del_each in dellist : 
                      del (site_current_url_remain[del_each])
        else : 
                  print "Site Queue Finished ... Stopping Crawling"
                  exit()
    #else : 
    #    print "No need to feed"




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


def url_splitter(fullurl):  ## in main this require bz every url function require site name and url 
##url splitted returns two parts 1.main domain 2. full url 
    site_and_rel   = urlparse( fullurl ) 
    return site_and_rel.netloc    ## site name without http ... :)  ..... ##**** PROBLEM ON FTP PROTOCOL


'''Give url  to fetch '''
def url_giver():
# returns one url that want to fetch 
# check time before giving 
#if time is less then pop another one and push this one back to queue   (if 1 or 2 element is remaining then)
# return url 


## time checking and feeder covered here  .... 

    if len(url_fecher_queue) == 0 : 
        back_queue_feeder()
    while True :
        jstforhold = ""
        current_pop_url = url_fecher_queue.pop(0)
        site_of_given_url = url_splitter(current_pop_url)
        value_return = time_checker(site_of_given_url)
        if value_return==1 : 
            jstforhold = current_pop_url 
            break 
        else : 
            url_fecher_queue.insert(10 ,current_pop_url )                 ## **** TIME NOT MATCH THEN 10 th position insert .... 
    return jstforhold

url_fecher_queue = ['http://pappa.com','http://maa.com']

site_current_url_remain = {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'],'http://kkk.com':['http://kkk.com/kkl','http://kkk.com/lll'] }

site_last_time_visit = {'maa.com' : dt.datetime.now(), 'kkk.com' :  dt.datetime.now()  }

while True : 
    a = url_giver()
    print a
