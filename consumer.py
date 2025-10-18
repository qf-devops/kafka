from kafka import KafkaConsumer
consumer = KafkaConsumer('test-topic', bootstrap_servers=['<EC2_PUBLIC_IP>:9092'])
for msg in consumer:
    print("Received:", msg.value.decode('utf-8'))
