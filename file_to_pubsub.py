from google.cloud import pubsub_v1
import time

publisher = pubsub_v1.PublisherClient()

topic_name = 'projects/corded-shard-360618/topics/data_stream_from_file_new'
try:
    publisher.create_topic(topic_name)
except Exception as e:
    print('Topic already exists')

with open('food_daily.csv') as f_in:
    for line in f_in:
        data = line
        future = publisher.publish(topic_name, data=data)
        print(future.result())
        time.sleep(1)
