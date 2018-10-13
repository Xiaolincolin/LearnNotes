# 学习Scrapy框架的要点

## 一、re的相关问题

### 1.匹配的字符意义
（1）`.`:可以是任意字符

（2）`*`：出现任意次数，包括零次

（3）`+`:至少要出现一次

（4）`{num}`:num代表只能出现的次数

（5）`{num_min：num_max}`:mix和max代表出现的最小和最大的次数

（6）`|`：或的关系，左右两边满足一个就行

（7）`[range]`：只要满足[]里面的任何一个值都可以（常用作电话号码匹配），用法`[12315]`或者`[0-9]`或者`[a-z]`都可以,`[^1]`代表不等于1都可以

（8）`\s`，`\S`：小s代表为一个空格，大S代表只要不是一个空格就行

(9)`\w`,`\W`:等同于`[a-zA-Z0-9_]`,大等同于大S（也是一个字符）

（10）`[\u4E00-\u9F45]`:只要是汉字都可以，代表一个汉字

(11)`\d`:代表的是数字`\d+`至少出现一次数字

(12)`^`,`$`:分别限定必须以什么开头和以什么结尾

(13)`?`:代表非贪婪模式

** 例子：**
```

line1 = "xxxx出生于2001年6月1日"
line2 = "xxxx出生于2001/6/1"
line3 = "xxxx出生于2001-6-1"
line4 = "xxxx出生于2001-06-01"
line5 = "xxxx出生于2001-06"
regex_str = ".*?出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}[\u4E00-\u9F45]|[月/-]$|$))"
```



### 2.贪婪模式（`.*`）与非贪婪模式（`.*？`）：
**非贪婪模式**是匹配串和母串进行匹配从左边开始匹配，匹配成功则返回结果，**贪婪模式**进行行反向匹配（从右），只要满足就给你，剩下的就算满足也不给你，如下：

```
line = "sadsxoooooooooooooooxxiaolin123"
regex_str = "^.*?(x.*x).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
```
第一个`.*?`是非贪婪模式，本得出了想要的`xooooooooox`，但是由于括号中间
的`.*`是贪婪模式，结果从右边匹配出了`xooooooooooxx`，只给了一个`xx`


## 二、scrapy框架

### 1.启程scrapy
（1）进入虚拟环境后下载scrapy框架：`pip install -i https://pypi.douban.com/simple/ scrapy`,使用豆瓣可以加速
（2）使用`scrapy startproject spidername`创建爬虫空间，`scrapy crawl spidername`启动


### 2.xpath选择器的语法结构
![xp][xpath]

![xp1][xpath1]


![xp2][xpath2]

#### xpath函数应用
在pycharm调试太慢，可以在虚拟空间进行调试：`scrapy shell url`

	(1)`.extract()`:获取html的文本信息,是以列表形式
	(2)`.strip()`:去掉空格
	(3)`.replace("old"，"new")`:字符串替换
	(4)`contains(@class, 'value')`:有些html标签的class有多个值，如想根据其中一个唯一的value找到这个标签就可以用这个函数
	(5)`h1/text()`:获取标签h1的内容

### 3.css选择器的语法结构

![cs][css]

![cs1][css1]

![cs2][css2]


#### css函数应用
	(1)`.extract()`:获取html的文本信息,是以列表形式
	(1.1)`extract_first("默认值")`:等同于`extract()[0]`只是为了避免跑出异常，默认值是没有的时候默认返回的值
	(2)`.strip()`:去掉空格
	(3)`.replace("old"，"new")`:字符串替换
	(4)`h1::text`:获取h1标签的内容
	(5)`a::attr(href)`:获取a的属性，加extract()可获得值



### 4、cookie与session的区别
  (1)cookie的有状态请求的本地存储机制:当用户第一次访问服务器时，服务器保存用户的信息，并分配给用户一个ID，当用户下次再访问服务器时，服务器根据ID就可以识别用户的信息  
  (2)session:其实是cooki在接收服务器返回的ID（包含个人信息）时，存在泄漏个人信息的微信，而seesion就是为了避免信息泄漏，将ID生成一段有生命周期的随机字符串，同时将ID对应的个人信息保存在服务器，下次浏览器只需发送服务器给的随机字符串即可，session是服务器机制。
![cookie][cook]




### 5、UA代理问题（user-agent）
	(1)scrapy在对服务器进行请求时，在没有设置代理的情况下，默认使用的是scrapy代理，这样很容易被服务器识别为爬虫，可以对UA进行重写，使用`fake-useragent`可以使用做好的UA代理池。
	(2)在'pip install fake-useragent'后'from fake_useragent'报错，原因是因为默认的版本过高，与py3.6不兼容，降低fake的版。
	(3)但是又出现`ake_useragent.errors.FakeUserAgentError:`错误，最后还得升级回来`pip install fake-useragent --upgrade`
	
	    
	 






<!---  链接  -->  
[xpath]:images/xpath.png
[xpath1]:images/xpath1.png
[xpath2]:images/xpath2.png
[css]:images/css.png
[css1]:images/css1.png
[css2]:images/css2.png
[cook]:images/cookie.png
