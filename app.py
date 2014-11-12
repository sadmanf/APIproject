import urllib2
import json

url="""
https://api.foursquare.com/v2/venues/40a55d80f964a52020f31ee3
"""
request= urllib2.urlopen(url)
result = request.read()
d = result
rlist = d#['responseData']['results']
for item in rlist:
	print item

print rlist
