import pika

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

def on_message(ch, method, properties, body):
    print('New message recieve:', body)


channel.basic_consume(queue='letterbox',auto_ack=True, on_message_callback=on_message)

print('Strating to consume')

channel.start_consuming()