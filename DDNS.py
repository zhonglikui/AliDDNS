import json
import time

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.request import CommonRequest

import AliClient
from Utils import Utils


def DDNS(use_v6):
    client = AliClient.getClient()
    recordId = getRecordId(client, AliClient.getConfigJson().get('Second-level-domain'))
    print({'recordId': recordId})
    if use_v6:
        ipAddress = Utils().getRealIPv6()
        ipType = 'AAAA'
    else:
        ipAddress = Utils().getRealIP()
        ipType = 'A'
    print({'type': ipType, 'ip': ipAddress})
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', recordId)
    request.add_query_param('RR', AliClient.getConfigJson().get('Second-level-domain'))
    request.add_query_param('Type', ipType)
    request.add_query_param('Value', ipAddress)
    return client.do_action_with_exception(request)


def getRecordId(client, domain):
    firstLevelDomain = AliClient.getConfigJson().get('First-level-domain')
    request = CommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('DescribeDomainRecords')
    request.add_query_param('DomainName', firstLevelDomain)
    response = client.do_action_with_exception(request)
    jsonObj = json.loads(response.decode('utf-8'))
    records = jsonObj['DomainRecords']['Record']
    print({'first': firstLevelDomain, "domain": domain})
    print({'response': response})
    print({"records": records})
    for each in records:
        if each['RR'] == domain:
            return each["RecordId"]


if __name__ == "__main__":
    try:
        while not Utils().isOnline():
            time.sleep(5)
            continue
        result = DDNS(False)
        print('成功了')
    except (ServerException, ClientException) as reason:
        print('失败了')
        print(reason.get_error_msg())
