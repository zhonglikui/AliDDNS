import json
import ssl
import urllib.request


# 利用API获取含有用户ip的JSON数据
def getIpPage():
    url = "https://api.ipify.org/?format=json"
    response = urllib.request.urlopen(url, context=ssl._create_unverified_context())
    html = response.read().decode('utf-8')
    return html


# 解析数据，获得IP
def getRealIp(data):
    jsonData = json.loads(data)
    return jsonData['ip']


# 利用API获取含有用户ip的JSON数据
def getIpPageV6():
    url = "https://v6.ident.me/.json"
    response = urllib.request.urlopen(url, context=ssl._create_unverified_context())
    html = response.read().decode('utf-8')
    return html


# 解析数据，获得IP
def getRealIpV6(data):
    jsonData = json.loads(data)
    return jsonData['address']
