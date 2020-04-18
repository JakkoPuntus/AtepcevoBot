import http.client
import ast

token = '964615920:AAEwHybjIse8w7tBe76kuMNBZpo6ckO23vg'

conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "62acce0ea1mshf007f9b817ad5fcp190835jsndb975b7e65b0"
    }

conn.request("GET", "/country?format=json&name=russia", headers=headers)

res = conn.getresponse()
data = res.read()

corona = data.decode("utf-8")
corona = corona[1:-1]
coronaDict = ast.literal_eval(corona)
count = str(coronaDict['confirmed'])
Count = "В России " + count + " зараженных"
CountNF = "В Наро-Фоминске 32 зараженных"