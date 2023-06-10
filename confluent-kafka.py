from confluent_kafka import Consumer, KafkaException

def get_latest_data():
    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'latest'
    })

    c.subscribe(['mytopic'])

    try:
        msg = c.poll(1.0)  # Wait up to 1 second for a message

        if msg is None:
            return None
        if msg.error():
            if msg.error().code() != KafkaException._PARTITION_EOF:
                print(msg.error())
            return None

        # Assuming the message is a JSON string
        data = json.loads(msg.value().decode('utf-8'))
        return data

    except Exception as e:
        print('Exception occurred: {}'.format(e))

    finally:
        c.close()
