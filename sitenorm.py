from urlparse import urlparse
from urlparse import urljoin

'''Site normalized before further processong '''
def sitenamenormalization(baseurl , one_url_at_a_time): ## baseurl is one used for datastored , and one url from all url returns from that page
# url provided    # return ['site','normalized absoluteurl']  ***#return 0 for same page (# used for identifing refernce of same page )        

#lower case 
#normalizes site name www.asd.com => http://asd.com
# relative to absolute /ddd => http://asd.com/ddd
#same page remove 
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

a =  sitenamenormalization('https://w3schools.com/html/default.asp' ,'/sitemap/sitemap_examples.asp' ) 
print a 
