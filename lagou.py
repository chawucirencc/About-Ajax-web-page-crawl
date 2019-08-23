import requests
import random
import time
from urllib import parse


"""
拉勾网站招聘信息的爬取;
"""
def get_page_json():
    agent = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        ]
    agents = random.sample(agent, 1)   
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "User-Agent": str(agents),
        "Host": "www.lagou.com",
        # "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=",
        # "X-Anit-Forge-Code": "0",
        # "X-Anit-Forge-Token": "None",
        # "X-Requested-With": "XMLHttpRequest",
        }

    # for page_num in range(1, 6):       
    url_1 = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='  # 网页地址的url
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'  # Ajax请求地址。

    r = requests.get(url=url_1, headers=headers, timeout=3)
    cookie = r.cookies # 获取网站的cooKies

    form_data = parse.urlencode([
            ('first', 'true'),
            ('pn', 1),
            ('kd', 'Python')
            ])
    res = requests.post(url, headers=headers, data=form_data, cookies=cookie, timeout=3)
    time.sleep(3)

    # print(type(res.text)) 
    # print(res.text)    # 匹配得到文本，不是很好处理。
    result_json = res.json()
    print(type(result_json))
    # print(result_json)
    result_list = result_json["content"]["positionResult"]["result"]
    # print(result_list)
    # yield result_list
    return result_list
    
    
def fun1(result_list):
    result_end = {}
    for i in result_list:
        result_end.setdefault("city", []).append(i["city"])
        result_end.setdefault("companyFullName", []).append(i["companyFullName"])
        result_end.setdefault("education", []).append(i["education"])
        result_end.setdefault("positionName", []).append(i["positionName"])
        result_end.setdefault("slalry", []).append(i["salary"])
        result_end.setdefault("workYear", []).append(i["workYear"])
    print(result_end)
    # 数据格式 {'city':[, , ,], 'companyFullName':[, , , ], ... , 'workYear':[, , , ]}


def fun2(result_list):
    result_end = []
    for i in result_list:
        result_end.append([i["city"], i["companyFullName"], i["education"], i["positionName"], i["salary"], i["workYear"]])
    print(result_end)
    # 数据格式[[], []]


def fun3(result_list):
    result = []
    for i in result_list:
        result_end = {}
        result_end["city"] = i["city"]
        result_end["companyFullName"] = i['companyFullName']
        result_end["education"] = i["education"]
        result_end["positionName"] = i["positionName"]
        result_end["salary"] = i["salary"]
        result_end["workYear"] = i["workYear"]
        result.append(result_end)
        # yield result_end
    print(result)
    # 数据格式[{}, {}]


# result_list = get_page_json()
# fun2(result_list)
