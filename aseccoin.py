from urllib2 import Request, urlopen, URLError
import json
#headers = {'User-Agent': 'AsecCoin 0.1'}

request = Request('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc')

try:
    response = urlopen(request)
    html = response.read()
    loadjson = json.loads(html)
    validate_resp = loadjson['success']

    if validate_resp == True:
        print "Attempting to print JSON formatted...\n"
        result = loadjson['result']

        print("string value: %s" %result[0]["MarketName"])
        #print result

        #print(json.dumps(result, ensure_ascii=True, indent=4, sort_keys=True, separators=(',', ':')))
        #var = json.dumps(result, ensure_ascii=True, indent=4, sort_keys=True, separators=(',', ':'))
        #test = var['Ask']
    else: 
        print "Parsing failed..."

except URLError, e:
    print 'Error processing:', e
