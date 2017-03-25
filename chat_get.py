import urllib
import urllib2

url = 'http://alice.pandorabots.com/'
values = {'input' : 'Hello!'}


data = urllib.urlencode(values)
req = urllib2.Request(url, data)
print " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
values = {'input' : 'How are you?'}
data = urllib.urlencode(values)
new_req = urllib2.Request(req, data)


response = urllib2.urlopen(new_req)
the_page = response.read()
print the_page