import pika
from pika.exchange_type import ExchangeType

def on_message(ch, method, prop, body):
    print('Message recived on sub1', body)

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message)

channel.start_consuming()