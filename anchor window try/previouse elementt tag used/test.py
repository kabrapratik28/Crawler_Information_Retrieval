from bs4 import BeautifulSoup
soup = BeautifulSoup(open("z.html"))
import re

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
                 #ref_anchorwindow = link.previousSibling.string     ##******** CORRECT THIS AFTERWARDS  *******************
                 for sibling in link.previous_siblings :
                     ref_anchorwindow = sibling.string
                     if ref_anchorwindow : 
                         reflen =len( re.sub('[^0-9a-zA-Z]+', '', ref_anchorwindow))
                         if reflen :
                             break
             #parent = link.parent 
             #if parent is None:
             #            print(parent)
             #else:
             #            print(parent.name)
             #            print parent.string
             if  link.previous_element.string: 
                 print   link.previous_element.string.encode("ascii","ignore")
             make_list = [ref_link, ref_anchor,ref_anchorwindow]
             temp_list.append(make_list)
    return temp_list



dd = all_url_on_given_page(soup)
print dd



#print (re.sub( '\s+', ' ', soup.get_text().encode("ascii","ignore")))
'''
ref_anchor = link.string
                                #for sibling in link.previous_siblings :  
                                #          ref_anchorwindow = sibling.string
                                #          ref_anchorwindow = ref_anchorwindow.encode("ascii","ignore")
                                #          reflen =len( re.sub('[^0-9a-zA-Z]+', '',ref_anchorwindow)) 
                                #          if reflen :
                                #               break           
'''

'''
     #print kk[0].encode('utf8') 
     #print kk[1].encode('utf8')
     #print kk[2].encode('utf8')
     #print "--------------------"
'''
