#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2014-03-30
# author: lijian
# description:
#   show ip information with country region city
#   and oiganization

import unirest
import time
import sys

URL = 'http://ip.taobao.com/service/getIpInfo.php'


def info(ip_list):
    '''
    return list of ip information:
    -> [{info1}, {info2}, ...]

    the info* format:
    {
        "ip":           "x.x.x.x",
        "city":         "xxxxx",
        "area_id":      "xxxxxx",
        "region_id":    "xxxxxx",
        "area":         "xxxxxxxxxxxx",
        "city_id":      "xxxxxx",
        "country":      "xxxxxxxxxxxx",
        "region":       "xxxxxxxxxxxxxxxxxx",
        "isp":          "xxxxxxxxxxxxxxxxxx",
        "country_id":   "xx",
        "county":       "",
        "isp_id":       "xxxxxx",
        "county_id":    "xx"
    }
    '''
    data = []
    for ip in ip_list:
        response = unirest.get(URL, params={'ip': ip})
        json_data = response.body
        info = {}
        if json_data['code'] == 0:  # success
            info = json_data['data']
        data.append(info)
        time.sleep(0.1)  # 为了保障服务正常运行，每个用户的访问频率需小于10qps。
    return data


def show_info(data_list):
    '''
    show list of data in nice show format
    '''
    for data in data_list:
        print '-'*60
        for (k, v) in data.iteritems():
            print '%10s: %s' % (k, v)

if __name__ == '__main__':
    args = sys.argv
    ips = ['202.114.6.79', '115.156.187.88']
    if len(args) > 1:
        ips = sys.argv[1:]
    show_info(info(ips))
