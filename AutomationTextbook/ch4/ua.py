import requests
check_url = 'https://api.aoikujira.com/ip/ini'

ua = 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36(KHTML, like Gecko)Chrome/85.0.4183.83 Safari/537.36'

res = requests.get(check_url)
print(res.text)

headers = {'user-agent': ua}
res = requests.get(check_url, headers=headers)
print(res.text)