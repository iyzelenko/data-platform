from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = [
    "student_login",
    "assignment_submitted",
    "entered_classroom"
]

while True:

    event = {
        "student_id": random.randint(1,5),
        "event": random.choice(events),
        "timestamp": time.time()
    }

    producer.send("student_events", event)

    print(event)

    time.sleep(2)