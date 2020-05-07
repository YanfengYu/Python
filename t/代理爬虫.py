'''
使用代理服务器进行爬虫
'''
from urllib import request, error

if __name__ == '__main__':
    url = "https://www.baidu.com"

    proxy = {'http': '182.46.252.206:9999'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        req = request.urlopen(url)
        html = req.read().decode()

        with open("pabaidu.html", 'w', encoding='utf-8') as f:
            f.write(html)


    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)

    except Exception as e:
        print(e)
