
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
             make_list = [ref_link, ref_anchor,ref_anchorwindow]
             temp_list.append(make_list)
    return temp_list

## Focused is focusing (narrowing the urls)
## chceking anchor's (NOT IMPLEMENTING ANCHOR WINDOW BZ MANY TIME GIVE WRONG)
## checking with keywords provided
## keywords are extracted from user provided text cutting
## if keyword there add otherwise not add and return this list 

##==========*************************==============
##AFTER WORDS BY APLLYING VECTOR SPACE MODEL ON ANCHORS ARANGE QUEUE ACCORDING TO THERE SCORES
##==========************************================

USER_PROVIDED_TEXT  = "News bUSiness career engliSH reSult"
LIST_OF_WORDS_USER =  filter(None,  USER_PROVIDED_TEXT.lower().split(" "))

def focused_links (list_of_links):
#****************** MAKE LOWER ANCHOR TEXT ************************ >>>>IN PREVIOSE ONLY
    list_ret = [ ]
    for evry_link_list in list_of_links :
        if evry_link_list[1] : 
            anchor_for_that_url = evry_link_list[1].lower()    ## remove lower from here and put that in datastorer function
            words_in_that_anchor = filter(None, anchor_for_that_url.split(" "))
            if len(list(set(LIST_OF_WORDS_USER) & set(words_in_that_anchor))):
                list_ret.append(evry_link_list)
    return list_ret





dd = all_url_on_given_page(soup)
pp  = focused_links (dd)

for kk in pp:
    print kk
    
'''
>>> a = [1,2,3,4,5]
>>> b = [1,3,5,6]
>>> list(set(a) & set(b))
[1, 3, 5]
'''


