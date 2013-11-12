'''Seed reader .. only used for first time'''
url_fecher_queue = []   #['http://asd.com/ddd','http://asd.com/fff']
visited_site_url = {}	 # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }
data_url = {}             #{site : [urlobject1 , .... ]}  ##urrl object => url,anchor,anchor window,metachar,main text
site_last_time_visit ={}       # {'http://asd.com':time(), .... }
site_current_url_remain = {}   # {'http://asd.com':['http://asd.com/ddd','http://asd.com/fff'] , ... }

def seed_reader():
    list_of_url = [] 
#read all seed normalized it and then put it into back queue 
    DocumentWhole = open( "url", "r" )
    for line in DocumentWhole:
        line = line.strip('\n')
        list_of_url.append(line)
    return list_of_url


a = seed_reader()  
print a   


