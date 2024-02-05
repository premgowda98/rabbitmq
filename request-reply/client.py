import pika
import uuid

def on_message(ch, method, prop, body):
    print('This is the response', body)

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

reply_queue = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_message)

channel.queue_declare(queue='request')


channel.basic_publish(exchange='', routing_key='request', body="Take this and get response",
                        properties=pika.BasicProperties(reply_to=reply_queue.method.queue,
                                                        correlation_id=str(uuid.uuid4())))

print('Starting client')

channel.start_consuming()