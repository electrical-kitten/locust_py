from locust import HttpUser, TaskSet, task, between
from req_check import user_info
import random

users = [
    {
    "login": user_info['users'][0]['user_login'], 
     "password": user_info['users'][0]['user_password'], 
     "token": user_info['users'][0]['token_shik']
    },
    {
    "login": user_info['users'][1]['user_login'], 
     "password": user_info['users'][1]['user_password'], 
     "token": user_info['users'][1]['token_shik']
    },
    {
    "login": user_info['users'][2]['user_login'], 
    "password": user_info['users'][2]['user_password'], 
    "token": user_info['users'][2]['token_shik']
    }
]

goods_ids = [27, 25, 15, 6]

class UserBehavior(HttpUser):
    wait_time = between(1, 10)

    def on_start(self):
        self.user_data = random.choice(users)
        self.login()

    def login(self):
        response = self.client.post("/login/signin", json = {"login": self.user_data["login"], "password": self.user_data["password"]})
        if response.status_code != 200:
            self.environment.events.request.fire(
                request_type="POST",
                name = "login",
                response_time = response.elapsed.total_seconds(),
                response_length=len(response.content),
                exception=Exception(f"Login failed: {response.text}"),
            )


    @task()
    def get_goods(self):
        goods_id = random.choice(goods_ids)
        response = self.client.get(f"/api/v1/goods/{goods_id}", headers = {"FaceKitToken": self.user_data["token"]})
        if response.status_code != 200:
            self.environment.events.request.fire(
                request_type="GET",
                name = "get_goods",
                response_time = response.elapsed.total_seconds(),
                response_length=len(response.content),
                exception=Exception(f"Get goods failed: {response.text}"),
            )




    # @task()
    # def get_project(self):
    #     self.client.get(f"/api/v1/projects/{project_id_ms}", headers = {"FaceKitToken": token})