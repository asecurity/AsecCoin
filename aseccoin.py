from urllib2 import Request, urlopen, URLError
import json

#print "This is a test"

request = Request('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc')

try:
    response = urlopen(request)
    html = response.read()
    print html
except URLError, e:
    print 'Error processing:', e
