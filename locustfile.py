from locust import HttpUser, TaskSet, task, between
from req_check import user_info

user_login = user_info['users'][0]['user_login']
user_pass = user_info['users'][0]['user_password']
token = user_info['users'][0]['token_shik']
goods_id = 1787079
project_id = 41740

class UserBehavior(HttpUser):
    wait_time = between(1, 5)
    def on_start(self):
        self.client.post("/login/signin", json = {"login": user_login, "password": user_pass})

    @task(1)
    def get_goods(self):
        self.client.get(f"/api/v1/goods/{goods_id}", headers = {"FaceKitToken": token}) 

    @task(2)
    def get_project(self):
        self.client.get(f"/api/v1/projects/{project_id}", headers = {"FaceKitToken": token})

# class WebsiteUser(HttpUser):
#     task_set = UserBehavior
#     min_wait = 5000
#     max_wait = 9000
