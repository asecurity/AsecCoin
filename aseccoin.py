from urllib2 import Request, urlopen, URLError
import json
#debug = {'verbose': sys.stderr}

#headers = {'User-Agent': 'AsecCoin 0.1'}


#print "This is a test"

request = Request('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc')


try:
    response = urlopen(request)
    html = response.read()
    print html

    print "Attempting to print JSON formatted...\n"
except URLError, e:
    print 'Error processing:', e
