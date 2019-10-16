
import pika,json

# 
# class RabbitMqProducerService:
# 
#     # def __init__(self):
#     #     self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     #     self.channel=self.connection.channel()
#     #     self.channel.queue_declare(queue='email_send_queue')


def sender(subject,message,frm,recipient_list):

    # !/usr/bin/env python

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_send_queue')

    message=json.dumps({
        "subject":subject,
        "message":message,
        "frm":frm,
        "recipient_list":recipient_list
    })

    channel.basic_publish(exchange='',
                          routing_key='email_send_queue',
                          body=message)

    print(" [x] Sent 'Hello World!")

    connection.close()



# rabbitmq=RabbitMqProducerService()

# rabbitmq.sender()



