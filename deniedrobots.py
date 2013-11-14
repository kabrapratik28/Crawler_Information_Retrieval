

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
data_url['apra.com'] = [Url_class('http://apra.net/telegraphic')  , ]

'''If robots denied'''
def denied_robots_call(site, url , anchor , anchor_window):
#add data="Robots denied" , anchor and anchor window to already created object 

## DONT ADD TO QUEUE
    list_of_object_derived = data_url[site] 
    list_of_one_object =  filter(lambda dd: dd.url == url ,  list_of_object_derived)
    object_url_gotted = list_of_one_object[0]
    object_url_gotted.add_title("ROBOTS DENIED")    ## ASK MADAM ... title of denied urls 
    object_url_gotted.add_anchor( anchor , anchor_window)
    object_url_gotted.dataadd("ROBOTS DENIED")     ## ASK MADAM CONFIRM  .... GOOGLE SHOWS LIKE THAT
    #print object_url_gotted.anchor
    #print object_url_gotted.anchor_win
    #print object_url_gotted.url
    #print object_url_gotted.title
    #print object_url_gotted.urldata

aa = denied_robots_call('apra.com', 'http://apra.net/telegraphic'  , 'anchor .. aaa' , 'anc winnnn ... ' )     
