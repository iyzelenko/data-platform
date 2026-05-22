from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

students = [
    {"student": "Alice", "faculty": "IT", "grade": 90},
    {"student": "Bob", "faculty": "IT", "grade": 86},
    {"student": "Charlie", "faculty": "Math", "grade": 95},
]

for student in students:
    producer.send("student-events", student)
    print(f"Sent: {student}")
    time.sleep(2)

producer.flush()