import re
import urllib.request
import bs4
# url = "https://movie.douban.com/top250?start="
#url = "http://212.129.245.115/geek"
url = 'https://gitee.com/gritandsea/picture/tree/master/img'
# from bs4 import BeautifulSoup

def main():
    data = getData(url)
    askURL(url)

# findlink = re.compile(r'<a title=(.*>?)>')
findlink = re.compile(r'<a href="(.*?)">')
# findlink = re.compile(r'<a href="(.*)"</a>')


def getData(url): #爬取网址
    data = []
    html = askURL(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    for item in soup.find_all('a'):
        #print(item)
        item = str(item)
        link = re.findall(findlink,item)
        print(link)
        data.append(link)
        c = str(data)

    print(data)
    with open('img\\pic-link.text', 'w')as f:
        f.write(c)

    print('写完了')
    return data

def askURL(url): #模拟浏览器头部信息，进行伪装
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html

def saveData(savepath):  #保存数据
    print('save....')

if __name__ == "__main__":
    main()