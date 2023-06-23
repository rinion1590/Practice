import requests
import time
def main():
    url = "https://notify-api.line.me/api/notify"
    token = "qyk3XkjKFUGpIJuTzljUsyxgSiEXCBOeSSZuBxov8f0"
    token2 = "J7F13B9Vz2SP7qXD6GFtWv4Zi3VBMVzaIByO0Q6kXqH"
    headers = {"Authorization" : "Bearer "+ token2}
    sec=input("待機時間:")
    Input = input("メッセージ:")
    message = Input
    time.sleep(int(sec))
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
