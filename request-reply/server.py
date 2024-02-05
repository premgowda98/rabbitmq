import pika
import time

def on_message(ch, method, prop, body):
    print('Request revived', body, prop.correlation_id)
    time.sleep(3)
    ch.basic_publish('', routing_key=prop.reply_to, body=f'sent from server {prop.correlation_id}')

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

reply_queue = channel.queue_declare(queue='request')

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_message)
channel.start_consuming()