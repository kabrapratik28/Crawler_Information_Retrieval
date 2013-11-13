
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


'''Check for duplicate '''
def url_checker_dupli(site , normalized_absolute_url ):
#checks is url used first time or used before
#checks in visited_site_url dictionary at key site and in list for normalized_absolute_url
#check site is dere ot not in dictionary .... !!!!
#return 0 or 1 accordingly
    if visited_site_url.has_key(site):
        if normalized_absolute_url in visited_site_url[site]:
            return 0     ## duplicate 
        else :
            visited_site_url[site].append(normalized_absolute_url)  ## added as visited
            new_obj_url = Url_class( normalized_absolute_url)
            data_url[site].append(new_obj_url)                      ## blank dataobject created for that url and added 
            return 1      ## site is present but url is new 
    else : 
        visited_site_url[site] = []
        data_url[site] = []
        visited_site_url[site].append(normalized_absolute_url)
        new_obj_url = Url_class( normalized_absolute_url)
        data_url[site].append(new_obj_url)   
        print "all new"
        return 1          ## site also ... no url offcourse


a = url_checker_dupli('rediff.com' , 'http://apra.net/telegraphic/sd' )

print visited_site_url
print data_url
print a 
