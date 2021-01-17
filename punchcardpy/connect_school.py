# -*- coding: UTF-8 -*-

import logging
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import urllib.request
import json
from fake_useragent import UserAgent
import re


def get_login_cookie(login_url_number):
    # 页面cookie来源连接
    login_url_head = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount='
    login_url_tail = '&agentId=1000060'
    return get_url_cookies(login_url_head + login_url_number + login_url_tail)


def get_url_cookies(url):
    while True:
        c_service = Service('geckodriver')
        driver = any
        try:
            c_service.command_line_args()
            c_service.start()
            firefox_options = Options()
            # 不启动界面显示- linux下命令行模式必须启用
            firefox_options.add_argument('-headless')
            driver = Firefox(firefox_options=firefox_options)
            driver.get(url)
            time.sleep(2)
            driver.refresh()
            time.sleep(2)
            cookies = driver.get_cookies()
            cookies_str = cookies[0]['name'] + "=" + cookies[0]['value']
            return cookies_str
        except Exception as identifier:
            logging.warning("{0}  获取cookie出错".format(re.compile(
                r'(?<=userAccount=)\d+\.?\d*').findall(url)[0]))
            logging.warning(identifier)
            time.sleep(5 * 60)
        finally:
            driver.quit()
            c_service.stop()


# 刷新cookie所属权
def refresh_cookie(login_url_number, cookie):
    try:
        # 伪装成浏览器
        ua = UserAgent()
        login_url = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount' + \
                    login_url_number + '&agentId=1000060'
        headers = {'Cookie': cookie, 'Accept-Encoding': 'gzip',
                   'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': ua.random}

        login_request = urllib.request.Request(
            url=login_url, headers=headers)
        urllib.request.urlopen(login_request)  # 发送请求

        headers['Referer'] = login_url
        weiXinJsSdkApiAuthorize_json = {
            "url": login_url}
        weiXinJsSdkApiAuthorize_request = urllib.request.Request(
            url='http://sjgl.zzut.edu.cn/mobile/weiXinJsSdkApiAuthorize.json', headers=headers,
            data=json.dumps(weiXinJsSdkApiAuthorize_json).encode(encoding='UTF8'))
        urllib.request.urlopen(weiXinJsSdkApiAuthorize_request)  # 发送请求

        setUserInfo_json = {"userAccount": login_url_number}
        setUserInfo_request = urllib.request.Request(
            url='http://sjgl.zzut.edu.cn/mobile/setUserInfo.json', headers=headers,
            data=json.dumps(setUserInfo_json).encode(encoding='UTF8'))
        urllib.request.urlopen(setUserInfo_request)  # 发送请求

        findListByAgentIdCache_json = {"agentId": "1000060"}
        findListByAgentIdCache_request = urllib.request.Request(
            url='http://sjgl.zzut.edu.cn/mobile/sysMobileBusiness/findListByAgentIdCache.json', headers=headers,
            data=json.dumps(findListByAgentIdCache_json).encode(encoding='UTF8'))
        urllib.request.urlopen(findListByAgentIdCache_request)  # 发送请求
    except Exception as identifier:
        logging.warning("{0}  刷新cookie所有权出错".format(login_url_number))
        logging.warning(identifier)
        time.sleep(5 * 60)


# 用于添加当前时间点的打卡记录的
def add_record(url, headers, **data):
    try:
        # 伪装成浏览器
        ua = UserAgent()
        values = data['data']
        if not ('User-Agent' in headers):
            headers['User-Agent'] = ua.random

        request = urllib.request.Request(url=url, headers=headers, data=json.dumps(
            values).encode(encoding='UTF8'))  # 需要通过encode设置编码 要不会报错

        response = urllib.request.urlopen(request)  # 发送请求

        logInfo = response.read().decode()  # 读取对象 将返回的二进制数据转成string类型

        return_code = json.loads(logInfo)
        return return_code
    except Exception as identifier:
        logging.warning("{0}  打卡出错".format(re.compile(
            r'(?<=userAccount=)\d+\.?\d*').findall(url)[0]))
        logging.warning(identifier)
        time.sleep(5 * 60)
