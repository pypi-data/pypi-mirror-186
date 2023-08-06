#!/usr/bin/env python

"""
Master-Worker模型-协程实现方式
"""

from __future__ import annotations

import asyncio
from asyncio.futures import Future
from typing import List
import abc

__all__ = ["Master", "Worker"]


class Worker(metaclass=abc.ABCMeta):
    def __init__(self):
        self._master: Master = None

    @abc.abstractmethod
    async def run(self):
        pass

    def done_callback(self, result: Future):
        pass

    @property
    def master(self):
        return self._master

    @master.setter
    def master(self, master: Master):
        self._master = master


class Master(object):
    def __init__(self):
        self._workers: List[Worker] = []

    def add(self, worker: Worker):
        worker.master = self
        self._workers.append(worker)

    async def start(self, loop=None):
        tasks = []
        for worker in self._workers:
            task = asyncio.ensure_future(worker.run(), loop=loop)
            task.add_done_callback(worker.done_callback)
            tasks.append(task)
        return await asyncio.gather(*tasks, loop=loop)
