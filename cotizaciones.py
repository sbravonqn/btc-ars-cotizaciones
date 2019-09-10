
import json
import requests
import math


base = ['BTC']

for int in base:
    
    r = requests.get('https://ripio.com/api/v1/rates/')
    ARS_BUY = ""
    ARS_SELL = ""

    if r.status_code == 200:

        data = r.json()
        ARS_BUY = data["rates"]["ARS_BUY"]
        ARS_SELL = data["rates"]["ARS_SELL"]
    else:
        raise Exception(str(r.status_code) + ". Error")

#############

pares = ["btc-ars"]

for pair in pares:
    url = "https://www.buda.com/api/v2/markets/{}/ticker".format(pair)
    r1 = requests.get(url)

    last_price = ""
   
    if r1.status_code == 200:
        data1 = r1.json()
        last_price = float(data1["ticker"]["last_price"][0])

    else:
        raise Exception(str(r1.status_code) + ". Error")

#############

par = ["btcusd"]

for int in par:

        r3 = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd')

        last = ""

        if r3.status_code == 200:
            data2 = r3.json()
            last = data2["last"]
        else:
            raise Exception(str(r3.status_code) + ".Error ")

#############


r4 = requests.get('http://ws.geeklab.com.ar/dolar/get-dolar-json.php')

response = r4.json()

print "Cotizacion BitStamp: " , last
print "Cotizacion Dolar Oficial: " , response["libre"]


#############

r5 = requests.get('https://api.satoshitango.com/v2/ticker')

response1 = r5.json()

satoshitango = response1["data"]["compra"]["arsbtc"]


#############

#r6 = requests.get('https://api.cryptomkt.com/v1/ticker?market=BTCARS')

#response2 = r6.json()

#print (int(response2[data][bid]))

#############


bsarg = float(last) * float(response["libre"])

dife = (float(last_price)/float(bsarg)) - 1

d = (dife*100)

dife2 = (float(ARS_BUY)/float(bsarg)) - 1

d2 = (dife2*100)

dife3 = (float(satoshitango)/float(bsarg)) -1

d3 = (dife3*100)

#############


print "" 
print "Cotizacion Compra BTC / ARS"
print ""
print "Ripio (https://www.ripio.com/es/): ", ARS_BUY , "ARS - BitStamp +",round(d2),"%"
print "Buda (https://www.buda.com/argentina): ", last_price, "ARS - BitStamp +",round(d),"%"
print "SatoshiTango (https://www.satoshitango.com/es-AR/): ", satoshitango, "ARS - BitStamp +",round(d3),"%"
print "" 

#############


f = open("precios.txt", "w")
f.write(

            'Ripio @RipioApp - https://www.ripio.com/es/: ' + str(round(ARS_BUY)) + ' ARS - BitStamp +' + str(round(d2)) + '%' + '\n'
            'Buda @BudaPuntoCom - https://www.buda.com/argentina: ' + str(round(last_price)) + ' ARS - BitStamp +' + str(round(d)) + '%' + '\n'
            'SatoshiTango @SatoshiTango - https://www.satoshitango.com/es-AR/: ' + str(round(satoshitango)) + ' ARS - BitStamp +' + str(round(d3)) + '%' + '\n'
            ''
        )
f.close()
