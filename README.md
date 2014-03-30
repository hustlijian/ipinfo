使用淘宝的[IP地址库](http://ip.taobao.com/index.php)，对IP进行查询,返回json格式的IP信息

##原理
1. 请求接口（GET）：  
http://ip.taobao.com/service/getIpInfo.php?ip=[ip地址字串]

2. 响应信息：  
（json格式的）国家 、省（自治区或直辖市）、市（县）、运营商

3. 返回数据格式：  

    {
        "code": 0, 
        "data": {
            "city": "\u5317\u4eac\u5e02", 
            "area_id": "100000", 
            "county_id": "-1", 
            "region_id": "110000", 
            "area": "\u534e\u5317", 
            "city_id": "110000", 
            "ip": "210.75.225.254", 
            "region": "\u5317\u4eac\u5e02", 
            "isp": "\u7535\u4fe1", 
            "country_id": "86", 
            "county": "", 
            "isp_id": "100017", 
            "country": "\u4e2d\u56fd"
        }
    }

其中code的值的含义为，0：成功，1：失败。


##接口
1. info(ip\_list)  
查询ip列表信息，返回json格式的列表信息

2. show\_info(data\_list)
格式化输出json格式的列表信息

##例子
`show_info(info(['8.8.8.8']))`

##参考
1. 淘宝IP地址库[rel](http://ip.taobao.com/index.php)
2. unirest 网络库[rel](http://unirest.io/python.html)
3. ipinfo.io [rel](http://ipinfo.io/)
