import requests
import json
import re
import time


def search(email):
    sess = requests.Session()
    headers = {
        'authority': 'account.samsung.com',
        'method': 'POST',
        'path': '/accounts/v1/DCGLRU/signUpCheckEmailIDProc?v=1569844406191',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 '
                      'Safari/537.36 ',
        'origin': 'https://account.samsung.com'
    }
    fndtk = 'https://account.samsung.com/accounts/v1/DCGLRU/signUpCheckEmailIDProc?'
    req = sess.get(fndtk, headers=headers)
    token = re.findall(r"'token' : '(.+?)'", req.text)
    if not token:
        return {
            'error': 'token not found'
        }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://account.samsung.com',
        'Referer': 'https://account.samsung.com/accounts/v1/DCGLRU/signUp',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 '
                      'Safari/537.36',
        'x-csrf-token': token[0],
    }
    params = {
        'v:': int(time.time() * 1000)
    }
    data = {
        "emailID": email,
    }
    url = 'https://account.samsung.com/accounts/v1/DCGLRU/signUpCheckEmailIDProc?'
    r = sess.post(url, headers=headers, params=params, data=json.dumps(data))
    if 'INVALID_EMAIL_ADDR' in r.text:
        result = {

            'exist': False
        }
    else:
        result = {
            'exist': True,
            'result': 'you can use this adress'
        }

    return result, r.text


if __name__ == '__main__':
    print(search('nikolaysdvatan@gmail.com'))
