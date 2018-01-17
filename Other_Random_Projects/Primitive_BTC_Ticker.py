import requests, json
import numpy as np
from colorama import Fore
import time

i=1

def getBitcoinPriceStr(currency):
        URL = 'https://api.coinbase.com/v2/prices/BTC-%s/spot' % currency
        try:
                r = requests.get(URL)
                priceStr = "{0:.2f}".format(float(json.loads(r.text)['data']['amount']))
                return priceStr
        except requests.ConnectionError:
                float ("Error fetching Bitcoin price from Coinbase API")
                

line1 = float(getBitcoinPriceStr('EUR'))
init = line1
l = []
a = []
c = []
inita = 0
initc = 0



i=1
while i<51:
    line2 = float(getBitcoinPriceStr('USD'))
    print("Fetching " + str(i) + " /50")
    l.append(init + line1)
    i=i+1
    a.append(inita + np.var(l))
 
    

i=1
c.append(1)
c.append(2)
c.append(3)



def Ticker():
    del l[0]
    line2 = float(getBitcoinPriceStr('USD'))    
    l.append(init + line2)
    var = np.var(l)
    del a[0]
    a.append(inita + var)
    del c[0]
    c.append(np.mean(a))


    if l[49] < l[48]:
            print(Fore.RED + "USD/BTC " + str(line2) + "   Var = " + str(np.var(a)))       
    elif l[49] > l[48]:
            print(Fore.GREEN + "USD/BTC " + str(line2) + "   Var = " + str(np.var(a)))
    elif l[49] == l[48]:
            print(Fore.BLACK + "USD/BTC " + str(line2) + "   Var = " + str(np.var(a)))
    
    
    time.sleep(0.01)



while True:
    Ticker()
    