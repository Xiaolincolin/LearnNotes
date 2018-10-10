# -*- coding: utf-8 -*-
"""
    主要用于新闻类或者文章的爬取，适用于与第一层是所有新闻的标题，要获取url，
第二层是通过url获取文章的详情类容

"""


import scrapy
from scrapy.http import Request
from urllib import parse
from Spider.Article.items import dlfjItem
page = 2


class DlfjSpider(scrapy.Spider):
    name = 'dlfj'
    allowed_domains = ['http://www.jbshihua.com/index.php?m=content&c=index&a=lists&catid=40']
    start_urls = ['http://www.jbshihua.com/index.php?m=content&c=index&a=lists&catid=40']

    def parse(self, response):
        """
        获取起始url新闻的response
        """
        global page
        # tops = response.css('.xw_ul li a::attr(href)').extract()    #获取所有详情页url
        tops =  list(set(response.css('.bd li a::attr(href)').extract()))
        for url in tops:
            # url = 'http://www.klsh.com/'+urls
            # url = top.css('').extract_first("")
            # create_time = top.css('.winstyle23644 tr td:nth-child(3) span::text').extract()
            # meta = {"create_time": create_time},
            # parse.urljoin(response.url, url)         #用于url整合
            yield Request(url=url, callback=self.parse_detail)

        # 下一页
        if page <26:
            url_tag = "http://www.jbshihua.com/index.php?m=content&c=index&a=lists&catid=40&page="
            next_url = url_tag+str(page)
            page += 1

            #递归掉用本身进行下一页获取所有新闻
            #parse.urljoin(response.url, next_url)
            yield Request(url = parse.urljoin(response.url, next_url), callback=self.parse)

    #处理详情页
    def parse_detail(self, response):
        """
        每条新闻的详情页获取内容
        """
        yssh_item = dlfjItem()

        #把满足标题格式的添加进list，多篇文章不管标题用格式的标签都可以
        title_list = []
        # title1 =  response.css('.details h2::text').extract()
        # title1 = response.css('.wb_window tr td::text').extract()
        # title_list.append(''.join(title1))
        # title2 =  response.css('#Title::text').extract()
        # title_list.append(''.join(title2))
        title = (''.join(title_list)).strip()

        #把创建时间满足的添加进list
        time_list =[]
        # create_time1 =  response.css('.details h3 span::text').extract()
        # # create_time1 =  response.css('.admin_dat::text').extract_first("")
        # time_list.append(''.join(create_time1))
        # create_time = (''.join(time_list)).strip()

        #正文,创建一个list，每次把满足的标签添加进去，不满足则为空
        list_all= []
        # content1 =  response.css('.con p soan span::text').extract()
        # list_all.append(''.join(content1))
        # content11 =  response.css('.o p span::text').extract()
        # list_all.append(''.join(content11))
        # content12 = response.css('.o p::text').extract()
        # list_all.append(''.join(content12))
        # content13 = response.css('.c div span p font::text').extract()
        # list_all.append(''.join(content13))
        # content4 = response.css('.c div span::text').extract()
        # list_all.append(''.join(content4))
        # content2 =  response.css('.c div div font::text').extract()
        # list_all.append(''.join(content2))
        # content3 = response.css('.c div font::text').extract()
        # list_all.append(''.join(content3))
        # content6 = response.css('.c p font::text').extract()
        # list_all.append(''.join(content6))
        # content16 = response.css('.c font::text').extract()
        # list_all.append(''.join(content16))
        # content5 = response.xpath('//*[@id="profiles_left"]/div/div[2]/span/font/p/text()').extract()
        # list_all.append(''.join(content5))
        # content11 = response.xpath('//*[@id="profiles_left"]/div/div[2]/span/span/p/font/span/text()').extract()
        # list_all.append(''.join(content11))
        # content10 = response.xpath('//*[@id="profiles_left"]/div/div[2]/span/p/text()').extract()
        # list_all.append(''.join(content10))
        # content6 = response.xpath('//*[@id="profiles_left"]/div/div[2]/span/span/p/span/text()').extract()
        # list_all.append(''.join(content6))
        # content7 = response.xpath('//*[@id="profiles_left"]/div/div[2]/span/p/font/text()').extract()
        # list_all.append(''.join(content7))
        # content8 = response.css(".MsoNormal::text").extract()
        # list_all.append(''.join(content8))
        # content9 = response.css('.cntcnt div p span::text').extract()
        # list_all.append(''.join(content9))
        content = (''.join(list_all)).strip()

        #通过meta传过来的创建时间
        create_time = response.meta.get("create_time", "")

        #把结果给item传给pipeline存入数据库
        yssh_item["title"] = title
        yssh_item["create_time"] = create_time
        yssh_item["content"] = content
        yield yssh_item







