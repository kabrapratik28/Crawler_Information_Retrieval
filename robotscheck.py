from reppy.cache import RobotsCache
robots = RobotsCache()
'''Robot call checker'''
def robots_checker(url_provided):   #return 0: denied 1 : granted
#check robots for that url call 
  try : 
    if robots.allowed(url_provided, '*'):
        return 1
    else : 
        return 0 
  except Exception : 
        return -1                # ************* site doesn't exists  


a = robots_checker("http://google.com/search")
b = robots_checker("http://rediff.com/images/dd")
c = robots_checker("http://cnn.com/kkk/asd")
d = robots_checker("http://fufajf.com/kkk/asd")
e = robots_checker("http://www.openlooioop.com/softwareEngineering/1")
print a
print b
print c
print d
print e
