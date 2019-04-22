import re

import requests
from lxml import etree
import uuid


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/72.0.3626.96 Safari/537.36'
}

list = [1]


def get_result():
    result_list = []
    urls = ["https://music.douban.com/top250?start={}".format(str(i)) for i in range(0, 100, 25)]
    for url in urls:
        data = requests.get(url, headers=headers)
        html = etree.HTML(data.text)
        # 循环标签
        count = html.xpath("//tr[@class='item']")
        for info in count:
            title = info.xpath("normalize-space(td[2]/div/a/text())")  # 标题
            list[0] = title  # 因为title用normalize-space去掉空格了，再生产result时标题显示不全，所以我用了list替换它
            star = info.xpath("td[2]/div/div/span[2]/text()")  # 星评
            brief_introduction = info.xpath("td[2]/div/p//text()")  # 简介
            # 生成result串
            for star, title, brief_introduction in zip(star, list, brief_introduction):
                result = {
                            "title": title,
                            "star": star,
                            "brief_introduction": brief_introduction,
                }
                result_list.append(result)
    return result_list


if __name__ == '__main__':
    songs = get_result()
    for item in songs:
        song_id = uuid.uuid1()
        title = item['title']
        star = item['star']
        brief_introduction = item['brief_introduction']
        pattern = r'(?<=/)*|*(?>=/)'
        print(re.split(r'\d+-\d+-\d+', brief_introduction))

