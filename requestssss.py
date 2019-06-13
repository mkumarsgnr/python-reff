
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)



data= {
    'username':'sam',
    'password':'coolcool'
}
r =requests.post(url = 'http://httpbin.org/post',data=data)

rd = r.json()
print(rd)
print(rd['form'])
print(rd['form']['username'])
