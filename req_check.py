import requests as r
import json

def user_info_conf():
    with open('./user_info.json', encoding='utf-8') as file:
        user_info_parse = json.load(file)
    return user_info_parse

user_info = user_info_conf()

user_login = user_info['users'][1]['user_login']
user_pass = user_info['users'][1]['user_password']
base_url = "https://multishik.cynteka.ru"
# base_url = "https://multivladick.cynteka.ru"
token = user_info['users'][1]['token_shik']
goods_id = 27
# body = {
#   "filters": [
#     {
#       "name": "шакал пик",
#       "onlyWithNotBlockTransferState": "true",
#       "typeId": "6",
#       "grouped": "false",
#       "sortBy": "id",
#       "sortByOrder": "desc",
#       "batchSize": 42,
#       "excludedIds": []
#     }
#   ]
# }

sign_in = r.post(f"{base_url}/login/signin", json={"login": user_login, "password": user_pass})

get_goods = r.get(f"{base_url}/api/v1/goods/{goods_id}", headers = {"FaceKitToken": token})

# get_project = r.get(f"{base_url}/api/v1/projects/41740", headers = {"FaceKitToken": token})

# filter_goods = r.post(f"{base_url}/api/v1/goods/filter", headers = {"FaceKitToken": token}, json = body)



print(sign_in.status_code)
print(sign_in.json())
print(get_goods.status_code)
# print(get_goods.json())
# print(get_project.status_code)
# print(get_project.text)
# print(filter_goods.status_code)
# print(filter_goods.json())
