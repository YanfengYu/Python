'''
股票爬虫
'''
import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出错了"


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])

        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + str(stock) + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            else:
                infoDict = {}
                soup = BeautifulSoup(html, 'html.parser')

                    ulist.append([tds[0].string, tds[1].string, tds[3].string])
                stockInfo = soup.find('td',attrs={id:"tdquote"})
                print(stockInfo)
        #     name = stockInfo[0]
        #     price = stockInfo[4]
        #
        #     infoDict[name] = price
        #
        #     with open(fpath,'a',encoding='utf-8') as f:
        #         f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html#sh'
    stock_info_url = 'http://so.cfi.cn/so.aspx?txquery='
    output_file = 'D://股票信息汇总.txt'
    alist = []

    getStockList(alist, stock_list_url)
    getStockInfo(alist, stock_info_url, output_file)


main()