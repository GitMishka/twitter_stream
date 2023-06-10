import time
from data_generator import generate_data
from kafka_producer import send_data

while True:
    data = generate_data()
    send_data(data)
    time.sleep(1) 
