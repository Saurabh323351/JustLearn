# #!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_send_queue')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='email_send_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



# class RabbitMqConsumerService:
#
#     def __init__(self):
#         self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#         self.channel=self.connection.channel()
#         self.channel.queue_declare(queue='email_send_queue')
#
#     def callback(self, method, properties, body):
#         print(" [x] Received %r" % body)
#
#     def receiver(self):
#
#         self.channel.basic_consume(
#             queue='email_send_queue', on_message_callback=self.callback, auto_ack=True)
#
#         print(' [*] Waiting for messages. To exit press CTRL+C')
#
#         self.channel.start_consuming()
#
#
# rabbitmq=RabbitMqConsumerService()
#
# rabbitmq.receiver()
