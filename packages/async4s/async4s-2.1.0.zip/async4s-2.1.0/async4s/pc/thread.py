#!/usr/bin/env python

"""
Producer-Consumer模型
"""

from __future__ import annotations

from queue import Queue
import abc
import threading


class Producer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._buffer: Queue = None

    @abc.abstractmethod
    def run(self):
        pass

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        self._buffer = buffer


class Consumer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._buffer: Queue = None

    @abc.abstractmethod
    def run(self):
        pass

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        self._buffer = buffer


class Manager(object):
    def __init__(self, producer: Producer, consumer: Consumer, buffer_size=1024):
        self._producer = producer
        self._consumer = consumer
        buffer = Queue(buffer_size)
        self._producer.buffer = buffer
        self._consumer.buffer = buffer
        self._producer_manager: threading.Thread = None
        self._consumer_manager: threading.Thread = None

    def start(self):
        self._producer_manager = threading.Thread(target=self._producer.run, name=self._producer.__class__.__name__, daemon=True)
        self._consumer_manager = threading.Thread(target=self._consumer.run, name=self._consumer.__class__.__name__, daemon=True)
        self._producer_manager.start()
        self._consumer_manager.start()

    def wait(self):
        self._producer_manager.join()
        self._consumer_manager.join()
