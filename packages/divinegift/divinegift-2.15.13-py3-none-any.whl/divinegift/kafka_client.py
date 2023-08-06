import uuid
from typing import Optional, Union, List

from divinegift import main
from divinegift import logger
from divinegift.errors import ProducerNotSetError, ConsumerNotSetError

try:
    from confluent_kafka import Producer, Consumer, KafkaError, TopicPartition
    from confluent_kafka import OFFSET_STORED, OFFSET_BEGINNING, OFFSET_END
except ImportError:
    raise ImportError("confluent_kafka isn't installed. Run: pip install -U confluent_kafka")
try:
    from confluent_kafka import avro
    from confluent_kafka.avro import AvroProducer, AvroConsumer
    from confluent_kafka.avro.serializer import SerializerError
    from confluent_kafka.avro.error import ClientError
except ImportError:
    pass
try:
    from divinegift.string_avro import StringAvroConsumer
except NameError:
    pass


class KafkaConsumer:
    def __init__(self, logger_: Optional[logger.Logger] = None, avro_consumer=False, key_string=False, **configs):
        self.consumer: Union[Consumer, AvroConsumer, None] = None
        self.logger: Optional[logger.Logger] = None
        self.avro_consumer: bool = False

        try:
            self.init_consumer(logger_, avro_consumer, key_string, **configs)
        except Exception as ex:
            pass

    def init_consumer(self, logger_: Optional[logger.Logger] = None, avro_consumer=False, key_string=False, **configs):
        self.logger = logger_ if logger_ else logger.Logger()
        self.avro_consumer = avro_consumer
        if not self.avro_consumer:
            self.consumer = Consumer(**configs)
        else:
            try:
                if key_string:
                    self.consumer = StringAvroConsumer({**configs})
                else:
                    self.consumer = AvroConsumer({**configs})
            except NameError:
                raise Exception("confluent_kafka[avro] isn't installed. Run: pip install -U confluent_kafka[avro]")
            except ClientError as ex:
                raise ClientError(str(ex))

    def close(self):
        if self.consumer:
            self.consumer.close()
            self.consumer = None
            self.avro_consumer = False
        else:
            raise ConsumerNotSetError('Set consumer before!')

    def subscribe(self, topics: Union[str, List], partition=None, offset=OFFSET_STORED):
        if partition is not None and offset != OFFSET_STORED:
            if isinstance(topics, List):
                for topic in topics:
                    self.set_offset(topic, partition, offset)
                    self.logger.log_info(f'[*] Consumer assigned to topic [{topic}] on partition [{partition}] and offset [{offset}]')
            else:
                self.set_offset(topics, partition, offset)
                self.logger.log_info(f'[*] Consumer assigned to topic [{topics}] on partition [{partition}] and offset [{offset}]')
        else:
            if isinstance(topics, str):
                topics = [topics]
            self.consumer.subscribe(topics)
            self.logger.log_info(f'[*] Consumer subscribed to topic {topics}')

    def set_offset(self, topic: str, partition: int, offset: int):
        if self.consumer:
            topic_p = TopicPartition(topic, partition, offset)

            self.consumer.assign([topic_p])
            self.consumer.seek(topic_p)
        else:
            raise ConsumerNotSetError('Set consumer before!')

    def consume_(self, num_messages=1, timeout=10):
        for msg_index in range(num_messages):
            msg = self.consumer.poll(timeout)
            if msg is None:
                continue
            if msg.error():
                self.logger.log_err(f"{'Avro' if self.avro_consumer else ''}Consumer error: {msg.error()}")
                continue
            self.logger.log_info(f'[<] Message received from {msg.topic()} ({msg.offset()} [{msg.partition()}])')
            self.logger.log_debug(f'[*] Received message: {msg.value()}')
            yield msg

    def consume(self, num_messages=1, timeout=10):
        for msg in self.consume_(num_messages=num_messages, timeout=timeout):
            yield msg

    def commit(self, message=None, *args, **kwargs):
        """
        .. py:function:: commit([message=None], [offsets=None], [asynchronous=True])

          Commit a message or a list of offsets.

          The ``message`` and ``offsets`` parameters are mutually exclusive. If neither is set, the current partition assignment's offsets are used instead. Use this method to commit offsets if you have 'enable.auto.commit' set to False.

          :param confluent_kafka.Message message: Commit the message's offset+1. Note: By convention, committed offsets reflect the next message to be consumed, **not** the last message consumed.
          :param list(TopicPartition) offsets: List of topic+partitions+offsets to commit.
          :param bool asynchronous: If true, asynchronously commit, returning None immediately. If False, the commit() call will block until the commit succeeds or fails and the committed offsets will be returned (on success). Note that specific partitions may have failed and the .err field of each partition should be checked for success.
        """
        if message:
            self.consumer.commit(message=message, *args, **kwargs)
        else:
            self.consumer.commit()

    def consume_txt(self, num_messages=1, timeout=10):
        for msg in self.consume_(num_messages=num_messages, timeout=timeout):
            if self.avro_consumer:
                yield msg.value()
            else:
                yield msg.value().decode('utf-8')


class KafkaProducer:
    def __init__(self, logger_: Optional[logger.Logger] = None, avro_producer=False, value_schema=None, key_schema=None,
                 **configs):
        self.producer: Union[Producer, AvroProducer, None] = None
        self.logger: Optional[logger.Logger] = None
        self.avro_producer: bool = False

        try:
            self.init_producer(logger_, avro_producer, value_schema, key_schema, **configs)
        except Exception as ex:
            pass

    def init_producer(self, logger_: Optional[logger.Logger] = None, avro_producer=False,
                      value_schema=None, key_schema=None, **configs):
        self.logger = logger_ if logger_ else logger.Logger()
        self.avro_producer = avro_producer
        if not self.avro_producer:
            self.producer = Producer(**configs)
        else:
            try:
                if not key_schema:
                    key_schema = '{"type": "string"}'
                self.producer = AvroProducer({**configs},
                                             default_value_schema=avro.loads(value_schema),
                                             default_key_schema=avro.loads(key_schema))
            except NameError:
                raise Exception("confluent_kafka isn't installed. Run: pip install -U confluent_kafka[avro]")
            except ClientError as ex:
                raise ClientError(str(ex))

    def close(self):
        if self.producer:
            self.producer = None
            self.avro_producer = False
        else:
            raise ProducerNotSetError('Set producer before!')

    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            self.logger.log_info(f'Message delivery to {msg.topic()} failed: {err}')
            self.logger.log_debug(dir(msg))
            self.logger.log_debug(msg)
        else:
            self.logger.log_info(f'[>] Message delivered to {msg.topic()} [{msg.partition()}]')

    def produce(self, topic, message, key=None, partition=None, headers=None):
        if self.producer is not None:
            self.producer.poll(0)
            if not key:
                key = str(uuid.uuid4())
            if not self.avro_producer:
                key = key.encode('utf-8')
                if isinstance(message, str):
                    message = message.encode('utf-8')
                else:
                    json_obj = main.Json()
                    json_obj.set_data(message)
                    message = json_obj.dumps().encode('utf-8')

            if not partition:
                self.producer.produce(topic=topic, value=message, key=key,
                                      on_delivery=self.delivery_report, headers=headers)
            else:
                self.producer.produce(topic=topic, value=message, key=key,
                                      partition=partition, on_delivery=self.delivery_report, headers=headers)
            self.producer.flush()
        else:
            raise ProducerNotSetError('Set producer before!')


class KafkaClient:
    def __init__(self, logger_: Optional[logger.Logger] = None):
        self.producer: Optional[KafkaProducer] = None
        self.avro_producer = False
        self.consumer: Optional[KafkaConsumer] = None
        self.avro_consumer = False
        self.logger = logger_ if logger_ else logger.Logger()

    def set_producer(self, **configs):
        self.producer = KafkaProducer(logger_=self.logger, avro_producer=False, **configs)

    def set_producer_avro(self, value_schema: str, **configs):
        self.producer = KafkaProducer(logger_=self.logger, avro_producer=True, value_schema=value_schema, **configs)

    def close_producer(self):
        self.producer.close()

    def set_consumer(self, **configs):
        self.consumer = KafkaConsumer(logger_=self.logger, avro_consumer=False, key_string=False, **configs)

    def set_consumer_avro(self, key_string=False, **configs):
        self.consumer = KafkaConsumer(logger_=self.logger, avro_consumer=True, key_string=key_string, **configs)

    def close_consumer(self):
        self.consumer.close()

    def send_message(self, topic, messages):
        if isinstance(messages, list):
            for message in messages:
                self.producer.produce(topic, message)
        else:
            self.producer.produce(topic, messages)

    def read_messages(self, topic, partition=None, offset=OFFSET_STORED):
        self.consumer.subscribe(topic, partition, offset)
        while True:
            for msg in self.consumer.consume(num_messages=1, timeout=10):
                if msg is None:
                    continue
                yield msg


if __name__ == '__main__':
    pass
