import os, time, requests, urllib
from bs4 import BeautifulSoup

login_url = 'https://uta.pw/sakusibbs/users.php?' + \
    'action=login&m=try'
user_id, password = ('JS-TESTER', 'ipCU12ySxl')
save_file = './list2.csv'

def login_download():
    session = requests.Session()
    res = session.post(login_url, params={
        'username_mmlbbs6': user_id,
        'password_mmlbbs6': password})
    time.sleep(1)
    mypage_url = get_link(res.text,'マイページ')
    mypage_html = session.get(mypage_url).text
    time.sleep(1)
    csv_url = get_link(mypage_html,'CSVでダウンロード')
    download_save(session, csv_url)

def download_save(session, csv_url):
    res = session.get(csv_url)
    with open(save_file, "wt") as fp:
        fp.write(res.text)
        print(res.text)

if __name__=='__main__':
    login_download()