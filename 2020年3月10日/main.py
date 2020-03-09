from urllib import request

url = 'https://maoyan.com/board/4'
headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read().decode())