import json

from aliyunsdkcore.client import AcsClient


def getClient():
    config = getConfigJson()
    keyId = config.get('AccessKeyId')
    keySecret = config.get('AccessKeySecret');
    print({'keyId': keyId, 'keySecret': keySecret})
    return AcsClient(keyId, keySecret, 'cn-hangzhou')


def getConfigJson():
    with open('config.json', 'r') as file:
        jsonStr = json.load(file)
    return jsonStr
