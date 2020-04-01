import requests
import time
import re

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

url = [
    'https://www.runoob.com/python/python-exercise-example{0}.html'.format(i)
    for i in range(1, 101)
]


def get_one_page(url, headers):
    response = requests.get(url)

    if response.status_code == 200:
        # return response.content.decode('utf-8')
        return response.content.decode()
    return None


if __name__ == '__main__':
    menu_pattern = '<p><strong>题目：</strong>(.*?)</p>'
    all_content_pattern = '<p>程序源代码：</p>(.*?)<p>以上实例输出结果为：</p>'
    content_pattern = '(<span class="(.*?)">(.*?))*</span>'

    for i in range(1, 101):
        website = 'https://www.runoob.com/python/python-exercise-example{0}.html'.format(
            i)
        tmp = get_one_page(website, headers=headers)
        if not tmp == None:
            menu = re.findall(menu_pattern, tmp)
            all_content = re.findall(all_content_pattern, tmp, re.S)
            content = []
            if len(all_content) > 0:
                content = re.findall(content_pattern, all_content[0])

            if len(menu) > 0:
                # file = open('E:/study/studypython/practice/practice_' +
                #             str(i) + '.py',
                #             'w',
                #             encoding="utf-8")
                # file.write('#' + menu[0] + '\n')
                # file.write('\'\'\'\n')
                # for c in content:
                #     if c[0] == '':
                #         file.write('\n')
                #     else:
                #         file.write(c[2] + ' ')
                # file.write('\n\'\'\'')
                # file.close()

        time.sleep(0.5)
