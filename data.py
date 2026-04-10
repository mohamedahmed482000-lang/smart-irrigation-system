import random

def generate_data():
    return {
        "moisture": random.randint(10, 80),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(30, 90)
    }