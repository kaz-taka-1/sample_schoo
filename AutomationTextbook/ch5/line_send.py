import requests

acc_token = 'GSgAMecqxbhwuYmSvM0lez4UcnJrCHMYET4bhWNjn0R'

def send_line(msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    send_line('Pythonからこんにちは！')
    print('ok')