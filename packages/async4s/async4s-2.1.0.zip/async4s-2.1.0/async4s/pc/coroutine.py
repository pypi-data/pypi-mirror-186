#!/usr/bin/env python

"""
Producer-Consumer模型
"""

from __future__ import annotations

import asyncio
import abc


class Producer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._buffer: asyncio.Queue = None

    @abc.abstractmethod
    async def run(self):
        pass

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        self._buffer = buffer


class Consumer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._buffer: asyncio.Queue = None

    @abc.abstractmethod
    async def run(self):
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
        buffer = asyncio.Queue(buffer_size)
        self._producer.buffer = buffer
        self._consumer.buffer = buffer

    async def start(self):
        producer = asyncio.ensure_future(self._producer.run())
        consumer = asyncio.ensure_future(self._consumer.run())
        return await asyncio.gather(producer, consumer)
