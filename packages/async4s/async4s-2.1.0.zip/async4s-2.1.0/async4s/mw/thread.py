#!/usr/bin/env python

"""
Master-Worker模型-多线程实现方式
"""

from __future__ import annotations

from concurrent.futures import Future, ThreadPoolExecutor
import abc

__all__ = ["Master", "Worker"]

class Worker(metaclass=abc.ABCMeta):
    def __init__(self):
        self._master: Master = None

    @abc.abstractmethod
    def run(self):
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
    def __init__(self, max_workers: int = None):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def start(self, worker: Worker):
        worker.master = self
        self._executor.submit(worker.run).add_done_callback(worker.done_callback)

    def wait(self):
        self._executor.shutdown()
