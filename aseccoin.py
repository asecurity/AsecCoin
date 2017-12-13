from urllib2 import Request, urlopen, URLError
import json
#debug = {'verbose': sys.stderr}

#headers = {'User-Agent': 'AsecCoin 0.1'}


#print "This is a test"

request = Request('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc')


try:
    response = urlopen(request)
    html = response.read()
    loadjson = json.loads(html)
    validate_resp = loadjson['success']

    if validate_resp == True:
        print "Attempting to print JSON formatted...\n"
        result = loadjson['result']

        result1 = json.dumps(result)
        print(result1)
    else: 
        print "Parsing failed..."

except URLError, e:
    print 'Error processing:', e
