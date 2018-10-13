"""
    用自动化工具（模拟浏览器）进行爬取文章数据,将数据
保存到csv，从csv将数据读取出来。

"""


import requests
from pyquery import PyQuery as pq
import csv
import datetime,time
import re
from pyquery import PyQuery as pq
from requests import RequestException
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sphinx.util import requests


#用自动化爬取，通过url进行一下页
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)
HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__cfduid=d28e657f5b6073f00f172b8f19694a87f1538235651; GUID=ed68f462-baf1-4b77-a52e-7b14b74c74e7; SESSION_COOKIE=web1-59-82; BROWSEID=0fdd14be-095c-4544-834b-8287df11e991; existFlag=1; rd=; vct=8; pvc=2',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def get_html_page():
    for i in range(1, 164):
        urls = 'http://dxzspc.cnooc.com.cn/col/col26701/index.html?uid=578071&pageNum='+str(i)
        browser.get(urls)
        time.sleep(1)

        #将页面拖拉至底部
        for i in range(1, 5):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        #获取页面html
        html = browser.page_source
        doc = pq(html)
        items = doc('#578071').items()

        #items是个迭代器，必须循环才能取数
        for item in items:

            product = {
                'id': item.find("").text(),
                'content': item.find("").attr("href"),
            }
            save_to_csv(product)

            #用自动化进行下一页点击
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#\\32 5000 > table > tbody > tr > td > table > tbody > tr > td:nth-child(8) > a')))
            submit.click()

#处理文章详情页
def detail(url):
    urls = 'http://www.basf-ypc.com.cn/default.php?mod=article&do=detail&tid='+str(url)
    html = requests.get(urls, headers = HEADERS)
    doc = pq(html.text)
    items = doc('.mod_font08').items()
    for item in items:
        product = {
            'id':url,
            'content':item.text(),
        }
        print(product)
        save_to_csv(product)


# 保存为CSV文件,同用于字典保存形式
def save_to_csv(product):
    li = []
    for value in product.values():
        if value:
            values = value.replace('\n', '')
            li.append(values)
        else:
            li.append('NULL')
    with open('artcle8.csv', 'a', encoding='utf-8', newline='') as f:
         writer = csv.writer(f)
         #filedname = product.keys()
         #writer.writerow(filedname)
         writer.writerow(li)


#从csv里面读书文件，可以用逗号分隔
def get_baby_id():
    with open ('artcle5.csv','r',encoding='utf-8',newline='') as f:
        for line in f:
            info = line.split(',')
            print(info[0])


if __name__ == '__main__':
    get_html_page()











