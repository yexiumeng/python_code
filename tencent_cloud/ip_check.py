# _*_ coding: utf-8 _*_
import time, datetime, os, json
import urllib, urllib2
import hashlib, base64, hmac, random
import requests
import re

###此程序用于查询云解析中哪些IP，不属于CLB中的虚IP

###用于创建请求url
def url_create(api,action,extra_paras={}):
    method = 'GET'
    timestamp = int(time.time())
    nonce = random.randint(1000, 1000000)
    secretid = urllib.quote('xxxxxxx')   #填入正确的secretid
    signature_method = urllib.quote('HmacSHA256')
    secretkey = 'xxxxxxxxxxxxx'    #填入正确的secretkey
    action = urllib.quote(action)

    req_params = 'Action=%s&Nonce=%s&SecretId=%s&Timestamp=%s&SignatureMethod=%s' % (action, 
    nonce, secretid, timestamp, signature_method)

    for i in extra_paras:
        key = extra_paras[i]
        if key:
            if isinstance(key,str):
                key = urllib.quote(key)
            new_para = "&"+i+"="+str(key)
            req_params = req_params+new_para

    req_params_array = req_params.split('&')
    req_params_array = sorted(req_params_array)
    req_params = '&'.join(req_params_array)

    req_str = "%s%s?%s" % (method, api, req_params)

    signature = urllib.quote(base64.b64encode(hmac.new(secretkey, req_str, digestmod=hashlib.sha256).digest()))
    req_url = "https://%s?%s&Signature=%s" % (api, req_params, signature)
    return req_url

###获取所有domain列表.储存在domain_list列表中
domain_list = []
domain_check_url = url_create(api="cns.api.qcloud.com/v2/index.php",action='DomainList')
domain_check_dict = requests.get(domain_check_url).json()["data"]["domains"]
for i in domain_check_dict:
    domain_list.append(str(i["punycode"]))

###获取所有domain云解析的A记录ip，储存在domain_ip_list列表，ip与domain的对应关系存储在domain_ip_dict字典中
domain_ip_dict = {}
domain_ip_list = []
for domain in domain_list:
    domain_ip_url = url_create(api="cns.api.qcloud.com/v2/index.php",action='RecordList',
    extra_paras={'domain': domain})
    domain_records = requests.get(domain_ip_url).json()["data"]["records"]
    for i in domain_records:
        if i['type'] == "A":
            val = str(domain)+"_"+str(i["name"])
            key = str(i["value"])
            domain_ip_list.append(key) 
            if key in domain_ip_dict:    #判断domain_ip_list字典是否有相同IP，有则对该IP做处理，防止被覆盖
                key = key+"_"+i["name"] + "."+str(domain)
            domain_ip_dict[key]=val
    

###获取所有CLB的ip，存储在clb_ip_list列表中
clb_list = []
clb_ip_list = []
region_list=['ap-guangzhou','ap-shanghai','ap-hongkong','ap-tokyo','na-ashburn']  #
for region in region_list:
    clb_list_url = url_create(api="clb.tencentcloudapi.com/",action='DescribeLoadBalancers',
    extra_paras={'Version':'2018-03-17','Region': region,'Limit': 200})
    clb_list = clb_list + requests.get(clb_list_url).json()["Response"]["LoadBalancerSet"]

for clb in clb_list:
    clb_ip_list.append(str(clb["LoadBalancerVips"][0]))

###利用ip做比较
domain_ip_set = set(domain_ip_list)
clb_ip_set = set(clb_ip_list)

unuse_ip_set = domain_ip_set - clb_ip_set

unuse_domain_ip_list = []
for key in domain_ip_dict:
    key_re = re.search('\d+\.\d+\.\d+\.\d+', key)
    ip = str(key_re.group())
    if ip in unuse_ip_set:
        domain = domain_ip_dict[key]
        unuse_domain_ip_list.append(domain+" "+ip)

###将域名与非腾讯云CLB的ip关系写入文件中
unuse_domain_ip_list.sort()
f = open('domain_ip_check.txt', 'w+')
for i in unuse_domain_ip_list:
    f.write(i+'\n')
f.close()   

###将非腾讯云CLB的ip列表写入文件中
f = open('ip_check.txt', 'w+')
for i in unuse_ip_set:
    f.write(i+'\n')
f.close()







