import time

import pika


def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange="", routing_key=queue_name, body=message)

    print(f"Sent '{message}'")
    connection.close()


def receive_message(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f"Received {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    QUEUE_NAME = "test_queue"
    send_message(QUEUE_NAME, "Hello, World!")
    time.sleep(10)
    receive_message(QUEUE_NAME)
