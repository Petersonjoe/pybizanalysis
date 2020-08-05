
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# count_url = "https://dbinabox.vip.ebay.com/api/get_dr_delay"
# test=str(requests.get(count_url, verify=False).content)

data = open('./data.txt').readlines()
data2 = data[0].replace('null', 'None')
db_list = eval(data2)

lag_map = {}

def ex_list(lst):
    r = []
    r.append(lst[1])
    r.append(lst[3])
    return r

def make_dict(lst):
    lag_map[lst[0]] = lst[1]
    return

res = map(ex_list,db_list)
d_list = [i for i in res]
_ = [make_dict(i) for i in d_list]
print(lag_map)

