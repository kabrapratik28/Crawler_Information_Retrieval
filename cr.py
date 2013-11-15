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

'''Seed reader .. only used for first time'''
def seed_reader():   ##return list of urls 
#read all seed normalized it and then put it into back queue 
    list_of_url = [] 
    DocumentWhole = open( "url", "r" )
    for line in DocumentWhole:
        line = line.strip('\n')
        list_of_url.append(line)
    return list_of_url


'''Data store to already created object when site marked as visited'''
def datastorer(site , at_given_url):      # return beautifulsoup object                   *** # at exception return 0 
# on that url that page text saved , title , meta character also saved  
# beautiful soap used for url
# try and catch used (broken url)
# url stored in dictionary and returns for further use of link on that page
# modify time visit of that site 
    listofobject = data_url[site] 
    list_of_one_object =  filter(lambda x: x.url ==at_given_url , listofobject)
    object_url = list_of_one_object[0]
    ##open page and give to beautiful soup
    try : 
        objecturllib = urllib2.urlopen( at_given_url) 
        htmlcode  =  objecturllib.read()
        soupobject = BeautifulSoup(htmlcode)
        #soupnormalized = soupobject.prettify()
        #print soupnormalized
        if soupobject.title : 
            ##print soupobject.title.string 
            object_url.add_title(soupobject.title.string) 
        ##print soupobject.body.get_text().encode('utf-8') ##printing purpose utf8 conversion 
        object_url.dataadd(soupobject.body.get_text())
        return  soupobject
    except Exception :
        object_url.dataadd("Error : Url is broken !!!")
        return 0 
    #print object_url.url.encode('utf-8')           
    #print object_url.title.encode('utf-8')               
    #print object_url.urldata.encode('utf-8')
    



'''Returns all page on given page '''
def all_url_on_given_page(beautful_soap_string):   # return [[url,anchor,anchorwindow],[url,anchor,anchorwindow],.... ]  
#give all urls on given page 
#normalized them using below defination
#return all url,achor text , anchor text window 
    temp_list = [] 
    for link in soup.find_all('a'):             ## for all a
         if link.get('href') :                  ## only contain href
             ref_anchorwindow = ''
             ref_link = link.get('href')
             ref_anchor = link.string
             if link.previousSibling : 
                 ref_anchorwindow = link.previousSibling.string     ##******** CORRECT THIS AFTERWARDS  *******************
             make_list = [ref_link, ref_anchor,ref_anchorwindow]
             temp_list.append(make_list)
    return temp_list



'''Site normalized before further processong '''
def sitenamenormalization(baseurl , one_url_at_a_time): ## baseurl is one used for datastored , and one url from all url returns from that page
# return final url provided         

#lower case 
#normalizes site name www.asd.com => http://asd.com
# relative to absolute /ddd => http://asd.com/ddd
#same page remove 
## REFER TO URL STUDY  ##
    if baseurl.startswith('http://'):
        baseurl = baseurl[7:]
    if baseurl.startswith('https://'):
        baseurl = baseurl[8:]
    if baseurl.startswith('www.'):
        baseurl = baseurl[4:]

    flag_of_one_url_http = 0     
    if one_url_at_a_time.startswith('http://'):
        one_url_at_a_time = one_url_at_a_time[7:]
        flag_of_one_url_http = 1
    if one_url_at_a_time.startswith('https://'):
        one_url_at_a_time = one_url_at_a_time[8:]
        flag_of_one_url_http = 1
    if one_url_at_a_time.startswith('www.'):
        one_url_at_a_time = one_url_at_a_time[4:]
        flag_of_one_url_http = 1 

    if (flag_of_one_url_http==1):    
        one_url_at_a_time = "http://" + one_url_at_a_time

    modified_base_url = 'http://'+baseurl
    joinedurl = urljoin( modified_base_url,one_url_at_a_time )   ##join url
    joined_url_parsed  = urlparse( joinedurl)                    ## parsed ... remove query from urls 
    finalurl = joined_url_parsed.scheme+"://" + joined_url_parsed.netloc + joined_url_parsed.path
    return finalurl.lower().strip('/')             ##last element / no use and making duplicatswith / and without /               ## case insensative



'''Check for duplicate '''
def url_checker_dupli(site , normalized_absolute_url ):
#checks is url used first time or used before
#checks in visited_site_url dictionary at key site and in list for normalized_absolute_url
#check site is dere ot not in dictionary .... !!!!
#return 0 or 1 accordingly
# mark visited by adding url and site accordingly dere or not 
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
        #print "all new"
        return 1          ## site also ... no url offcourse



''' If duplicate url then ... and add to object created already '''
def add_anchor_only(site, url , anchor , anchor_window):
#add anchor of given url bz it done before jst add anchor  AND anchor window
#add in data_url dictionary at key site and in list for normalized_absolute_url
    all_url_rel = data_url[site]
    list_of_one_url_of_site =  filter(lambda mm: mm.url == url ,all_url_rel )
    one_url_gotted_obj = list_of_one_url_of_site[0] 
    one_url_gotted_obj.add_anchor(anchor , anchor_window)



  
'''*** MERGED IN URL DUPLICATE CLASS ... IT WILL CHECK IF NOT CREATE AND RETURN 1 IF DERE JST RETURN 0  .. both url and site check  
# Mark as visited and create object
def url_visited(site, url_provided):                       #return nothing 
#mark that url as visited and create object for it 
#add to both dictionary data_url and visited_site_url
# check site in dictionary there or not ... if not add sitte to dictionary  
'''


'''Robot call checker'''
def robots_checker(url_provided):   #return 0: denied 1 : granted
#check robots for that url call 
  try : 
    if robots.allowed(url_provided, '*'):   ## put user agent name instead of *
        return 1
    else : 
        return 0 
  except Exception : 
        return -1                # ************* site doesn't exists  


'''If robots denied'''
def denied_robots_call(site, url , anchor , anchor_window):
#add data="Robots denied" , anchor and anchor window to already created object 
#DONT ADD TO QUEUE OF SITE 
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

'''Give url  to fetch '''
def url_giver():
# returns one url that want to fetch 
# check time before giving 
#if time is less then pop another one and push this one back to queue   (if 1 or 2 element is remaining then)
# return url 



def url_splitter(fullurl):  ## in main this require bz every url function require site name and url 
##url splitted returns two parts 1.main domain 2. full url 




