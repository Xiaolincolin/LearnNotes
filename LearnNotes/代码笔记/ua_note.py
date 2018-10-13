"""
在scrapy中加入UA代理，随机使用User_Agent来进行代理模拟
1.pip install fake-useragent
2.在middlewares.py中加入以下代码
3.在settings中加入RANDOM_UA_TYPE = "random"
4.相当于全局做UA代理
"""

from fake_useragent import UserAgent


class RandomUserAgentMiddlware(object):
    def __init__(self,crawler):
        super(RandomUserAgentMiddlware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):

        def get_ua():
            return getattr(self.ua, self.ua_type)
        random_type = get_ua()
        request.headers.setdefault('User-Agent', get_ua())