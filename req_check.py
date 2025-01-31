import requests as r
import json

def user_info_conf():
    with open('./user_info.json', encoding='utf-8') as file:
        user_info_parse = json.load(file)
    return user_info_parse

user_info = user_info_conf()

user_login = user_info['users'][0]['user_login']
user_pass = user_info['users'][0]['user_password']
base_url = "https://multishik.cynteka.ru"
token = user_info['users'][0]['token_shik']
# print(type(user_login))
# print(type(user_pass))

sign_in = r.post(f"{base_url}/login/signin", json={"login": user_login, "password": user_pass})

get_goods = r.get(f"{base_url}/api/v1/goods/1787079", headers = {"FaceKitToken": token})

get_project = r.get(f"{base_url}/api/v1/projects/41740", headers = {"FaceKitToken": token})

print(sign_in.status_code)
# print(sign_in.text)
print(get_goods.status_code)
print(get_project.status_code)
# print(get_project.text)
