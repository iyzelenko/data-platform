from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'student-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='student-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for messages...")

for message in consumer:
    print("Received:", message.value)