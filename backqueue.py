
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

site_current_url_remain = {}
url_fecher_queue  = ['asd','dgf']

back_queue_feeder()
print url_fecher_queue
print site_current_url_remain
