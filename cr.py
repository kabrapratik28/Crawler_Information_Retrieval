'''
0. url and data stored for coressponfing url (title , meta chara also) ... anchor saved before only
1. url get from page
2. normalized them (lower case , http ,relative to absolute )
3. check for done before or not
	if done => add anchor only , anchor window 
        else => add to visited 
       		checks robots.txt
        	if => exclusion .. add url and set data as "Robot denied !!!" and add anchor  also add  to visited
                else => url ( create a empty object with anchor no data  ... bz before it processed via queue if another came can add anchor text to it )
                	Add to site queue dictionary 
4.check urlfetcher queue lenght 
	if => it is less than 3 refill it with site queue dictionary 
        else => 
        	see time last or put it aside time diff =2 sec 
        	try : fetch url exception : broken urls  

STOPING CONDITION => after N(e.g. 10) url dont tc urls into url dictionary and empty all dictionary and put into queue and finish that queue
'''

'''
data
'''
url_fecher_queue = []   #['http://asd.com/ddd','http://asd.com/fff']
visited_site_url = {}	 # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }
data_url = {}             #{site : [urlobject1 , .... ]}  ##urrl object => url,anchor,anchor window,metachar,main text
site_last_time_visit ={}       # {'http://asd.com':time(), .... }
site_current_url_remain = {}   # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }

'''Seed reader .. only used for first time'''
def seed_reader():
#read all seed normalized it and then put it into back queue 


'''Data store to already created object when site marked as visited'''
def datastorer(at_given_url):      # return beautifulsoup string                   *** # at exception return 0 
# on that url that page text saved 
# beautiful soap used for url
# try and catch used (broken url)
# url stored in dictionary and returns for further use of link on that page
# modify time visit 





'''Returns all page on given page '''
def all_url_on_given_page(beautful_soap_string):   # return [[url,anchor,anchorwindow],[url,anchor,anchorwindow],.... ]  
#give all urls on given page 
#normalized them using below defination
#return all url,achor text , anchor text window 



'''Site normalized before further processong '''
def sitenamenormalization(one_url_at_a_time):      # url provided    # return ['site','normalized absoluteurl']  ***#return 0 for same page (# used for identifing refernce of same page )        

#lower case 
#normalizes site name www.asd.com => http://asd.com
# relative to absolute /ddd => http://asd.com/ddd
#same page remove 


'''Check for duplicate '''
def url_checker_dupli(site , normalized_absolute_url ):
#checks is url used first time or used before
# checks in visited_site_url dictionary at key site and in list for normalized_absolute_url
#return 0 or 1 accordingly




''' If duplicate url then ... and add to object created already '''
def add_anchor_only(site, url , anchor , anchor_window):
#add anchor of given url bz it done before jst add anchor  AND anchor window
#add in data_url dictionary at key site and in list for normalized_absolute_url

  

''' Mark as visited and create object'''
def url_visited(site, url_provided):                       #return nothing 
#mark that url as visited and create object for it 
#add to both dictionary data_url and visited_site_url
 

'''Robot call checker'''
def robots_checker(url_provided):   #return 0: denied 1 : granted
#check robots for that url call 


'''If robots denied'''
def denied_robots_call(site, url , anchor , anchor_window):
#add data="Robots denied" , anchor and anchor window to already created object 


''' If not denied by robots call ''' 
def add_to_site_queue_dict(site, url):
#add to dictionary of queue sitewise


'''Back queue lenght is less than 3'''
def back_queue_feeder():
#fill back queue 


'''Before url fetched check this time '''
def time_checker():
#checks time and return 0 or 1 accordingly what to do 


'''Give url  to fetch '''
def url_giver():
# returns one url that want to fetch 







