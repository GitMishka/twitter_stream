#use it Google colab

from faker import Faker
import json
import time

fake = Faker()

def get_user_click():
    return {
        "user_id": fake.random_int(min=1, max=1000, step=1),
        "timestamp": time.time(),
        "url": fake.uri(),
        "ip": fake.ipv4(),
        "user_agent": fake.user_agent()
    }

while True:
    print(json.dumps(get_user_click()))
    time.sleep(1) 

