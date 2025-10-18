from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['<EC2_PUBLIC_IP>:9092'])
for i in range(5):
    msg = f"Kafka 4.1 Message {i}"
    producer.send('test-topic', msg.encode('utf-8'))
    print("Sent:", msg)
producer.close()
