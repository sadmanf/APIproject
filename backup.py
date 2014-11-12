import urllib2
import json

def acafilter(a):
        if a.find('.org')>-1:
		if a.find('wikipedia.org')>-1:
                	return True
        if a.find('.edu')>-1:
                return True
        if a.find('.gov')>-1:
                return True
        if a.find('.com')>-1:
                if a.find('nytimes.com')>-1:
                        return True
                if a.find('wsj.com')>-1:
                        return True

        return False

def

url="""
http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="""+PUTQUERYHERE+"""&safe=active
"""
request= urllib2.urlopen(url)
result = request.read()
d = json.loads(result)
rlist = d['responseData']['results']
for item in rlist:
        if acafilter(item['url']):
                print item['content']


