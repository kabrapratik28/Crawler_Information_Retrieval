

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

site_current_url_remain['asd.com']=  ['http://asd.com/aaa/bbb' ]

''' If not denied by robots call ''' 
def add_to_site_queue_dict(site, url):
#add to dictionary of queue sitewise
#first check site name present in dictionary or not if not create new key and empty list 
#if present append to site list 
    
##IF CHECK SITE PRESENT OR NOT 
##IF PRESENT JUST ADD TO QUEUE
##ELSE ADD SITE AND MAKE QUEUE BY MAKING LIST
    if site_current_url_remain.has_key(site):
        site_current_url_remain[site].append(url)
    else :
        site_current_url_remain[site] = [url , ]


aa  = add_to_site_queue_dict('asd.com','http://asd.com/ddd/bbb') 
bb = add_to_site_queue_dict('google.com', 'http://google.com/asd/hhh')

print site_current_url_remain
