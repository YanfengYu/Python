'''
中国大学排名定向爬虫
'''
import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #         print(r.text)
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            #             for i in tds:
            #                 print(i)
            ulist.append([tds[0].string, tds[2].string, tds[5].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}\t".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}\t".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/BCSR/jisuanjikexueyujishu2017.html"
    html = getHTMLText(url)

    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
