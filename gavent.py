# coding: utf-8
import requests
import time
#from urllib.error import URLError
import requests
import gevent
from gevent import monkey;monkey.patch_all()


def getdata():
    #要测试的接口
    url = "http://www.yy80.top:9000/api/alldata/"

    payload={}
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjYyNzA1OTUyLCJlbWFpbCI6bnVsbCwiaXNfc3VwZXJ1c2VyIjp0cnVlfQ.2r5kQVSXQOi9Ao1CsSe0a34hfWruMrgLQf_w9IAJ0LY',
    'Connection': 'keep-alive',
    'Referer': 'http://192.168.10.128:8000/websites',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        if response.status_code != 200:
            error.append("0")
    # except URLError as e:
    #     print('请求', e)
    #     error.append("ue0")
    except Exception as e:
        error.append("re0")
        print('网络连接错误：', e)

def call_gevent(count):
    """调用gevent 模拟高并发"""
    begin_time = time.time()
    run_gevent_list = []
    for i in range(count):
        print('\033[0;31m--------------%d--Test-------------\033[0m' % i)
        run_gevent_list.append(gevent.spawn(getdata()))
    gevent.joinall(run_gevent_list)
    end_time = time.time()
    print('\033[0;31m测试次数:\033[0m', count)
    print('\033[0;31m单次测试时间(平均)s:\033[0m', (end_time - begin_time) / count)
    print('\033[0;31m累计测试耗时(s):\033[0m', end_time - begin_time)
    print('\033[0;31m接口失败率:\033[0m',error.count("0")/ count)
    print('\033[0;31m网络请求报错次数:\033[0m',error.count("re0") )

if __name__ == '__main__':
    global error
    error=[]
    # 10万并发请求
    test_count = 10
    call_gevent(test_count)