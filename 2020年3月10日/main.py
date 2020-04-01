from urllib import request
import re


def Happy(list):
    url = 'https://maoyan.com/board/' + str(list[1])
    headers = {
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    html = resp.read().decode()
    with open("asp.html", "w", encoding='utf-8') as f:
        f.write(html)

    s = r'<a class="video-pic loading"(.*?)title="(.*?)"(.*?)</a>'
    pattern = re.compile(s, re.S)
    films = pattern.findall(html)

    test = open("F:/Download/E/test.txt", "a+", encoding='utf-8')

    test.write("\n" + "index:" + str(list[1]) + "\n")
    for film in films:
        test.write(film[1] + "\n")

    test.close()

    if (list[1] < 95):
        list[1] += 1
        list[0] = True


if __name__ == "__main__":
    list = [True, 1]
    while 1:
        if (list[0]):
            list[0] = False
            print("cur_index:" + str(list[1]))
            Happy(list)
