import requests

acc_token = 'GSgAMecqxbhwuYmSvM0lez4UcnJrCHMYET4bhWNjn0R'

image_file = './sky.jpg'

def send_line(msg, image_file):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}

    with open(image_file,'rb') as fp:
        files = {'imageFile': fp}
        requests.post(url,headers=headers, params=payload, files=files)

if __name__=='__main__':
    send_line('こんにちは', image_file)
    print('ok')