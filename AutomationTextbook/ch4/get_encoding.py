import chardet, requests

url = 'https://www.aozora/gr.jp/cards/000035/files/files/1567_14913.html'
bindata = requests.get(url).content
r = chardet.detect(bindata)
print(r)