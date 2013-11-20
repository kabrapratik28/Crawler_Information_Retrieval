## depth calculation for crawling


USER_GIVEN_NO  = 4      ## Number of depth max user want to crawl 
LIST_DEPTH_REC = []     ## list where records are stored 

def create_depth_list (user_given_no):   ## create depth empty list 
## e.g. depth 4 === [ [],[],[],[]  ] ## for each depth one list
## add 1 to user given because first is zero and taken by seeds
    LIST_DEPTH_REC = [[] for x in range(user_given_no + 1)]


def add_to_depth (one_full_url , depth_number): ## adding given urls to depth
## depth number provides info about in which depth we want to add
    LIST_DEPTH_REC[ depth_number].append(one_full_url) 


def check_depth (full_absolute_url): ## returning 1 if depth is not boundary depth AND 0 when depth is boundary depth 
    for current_list in  LIST_DEPTH_REC:
        if full_absolute_url in current_list : 
            break 
    depth_of_url = LIST_DEPTH_REC.index(current_list)
    if depth_of_url == USER_GIVEN_NO : 
        return [0,depth_of_url]
    else :
        return [1,depth_of_url]




create_depth_list (USER_GIVEN_NO)
LIST_DEPTH_REC = [['google.com','bour.com'],[],[],['asd.com','basd.com'],['bass.com']] 
a = check_depth ('google.com')
print a


add_to_depth ('asdeee.com' , 0)
print LIST_DEPTH_REC
