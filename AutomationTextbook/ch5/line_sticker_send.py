import requests

acc_token = 'GSgAMecqxbhwuYmSvM0lez4UcnJrCHMYET4bhWNjn0R'

image_file = './sky.jpg'

def send_sticker_line(msg, package_id, sticker_id):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {
        'message':msg,
        'stickerPackageId': package_id,
        'stickerId': sticker_id,
        }

    requests.post(url, headers=headers, params=payload)

if __name__=='__main__':
    send_sticker_line('スタンプ付きで、こんにちは', 4, 303)
    print('ok')
