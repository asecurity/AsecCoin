from urllib2 import Request, urlopen, URLError
import json
#headers = {'User-Agent': 'AsecCoin 0.1'}

# Break out api URL from $market to loop through list
request = Request('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-pivx')

# Create a dictionary/list of markets to loop through

try:
    response = urlopen(request)
    html = response.read()
    loadjson = json.loads(html)
    validate_resp = loadjson['success']

    if validate_resp == True:
        print "AsecCoin:\n"
        result = loadjson['result']

        print("Market: %s" %result[0]["MarketName"])
        print("Last:   %f" %result[0]["Last"])
        print("Bid:    %f" %result[0]["Bid"])
        print("Ask:    %f" %result[0]["Ask"])
        print("High:   %f" %result[0]["High"])
        print("Low:    %f" %result[0]["Low"])

    else: 
        print "Parsing failed..."

except URLError, e:
    print 'Error processing:', e
