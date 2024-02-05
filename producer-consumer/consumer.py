import pika
import time
import random

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

queue = 'letterbox'

channel.queue_declare(queue=queue)

def on_message(ch, method, properties, body):
    time.sleep(2)
    print('New message recieve:', body)


# channel.basic_consume(queue=queue,auto_ack=True, on_message_callback=on_message)

# competing consumers
def on_message(ch, method, properties, body):
    process_time = random.randint(1,6)
    print('New message recieve:', body, 'takes', process_time, 's to process')
    time.sleep(process_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('Processing completed')

channel.basic_qos(prefetch_count=1) # waits until prev message is processed
channel.basic_consume(queue=queue, on_message_callback=on_message)


print('Strating to consume from', queue)

channel.start_consuming()