'''
0. url and data stored for coressponfing url (title , meta chara also) ... anchor saved before only
1. url get from page
2. normalized them (lower case , http ,relative to absolute )
3. check for done before or not
	if done => add anchor only , anchor window 
        else => checks robots.txt
        	if => exclusion .. add url and set data as "Robot denied !!!"
                else => Add to visited url ( create a empty object with achor no data  ... bz before it processed via queue if another came can add anchor text to it )
                	Add to site queue dictionary 
4.check urlfetcher queue lenght 
	if => it is less than 3 refill it with site queue dictionary 
        else => 
        	see time last or put it aside
        	try : fetch url exception : broken urls  
'''

'''
data
'''
url_fecher_queue = []   #['http://asd.com/ddd','http://asd.com/fff']
visited_site_url = {}	 # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }
site_last_time_visit ={}       # {'http://asd.com':time(), .... }
site_current_url_remain = {}   # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }
def seed_reader():
#read all seed normalized it and then put it into back queue 

def sitenamenormalization():
#lower case 
#normalizes sitr name www.asd.com => http://asd.com
# relative to absolute /ddd => http://asd.com/ddd

def url_checker_dupli():
#checks is url used first time or used before
#return 0 or 1 accordingly



def url_visited():
#mark that url as visited 






def url_giver():
# returns one url that want to fetch 



def back_queue_feeder():
#fill back queue 





