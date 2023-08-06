# async4s - 一个简单易用的异步执行模块

![image](https://img.shields.io/badge/made_in-china-ff2121.svg)
[![image](https://img.shields.io/pypi/v/async4s.svg)](https://pypi.org/project/async4s/)
[![image](https://img.shields.io/pypi/l/async4s.svg)](https://pypi.org/project/async4s/)

## About
这是一个简单易用的异步执行模块，可以使原有方法轻松变为异步执行。  

## Requirements
- Python3

## Install
通过pip命令安装：
```shell
pip install async4s
```

## Example
- async by thread
```python
import time

from async4s.mw.thread import Master, Worker

def work(i):
    time.sleep(i)
    return i

def callback(results):
    print(results)

print(time.perf_counter())
workers = [Worker(work, i) for i in range(5)]
m = Master(workers, callback)
print("main")
m.wait()
print(time.perf_counter())
```

- async by asyncio
```python
import time
import asyncio

from async4s.mw.coroutine import Master, Worker


async def work(i):
    await asyncio.sleep(i)
    return i


def callback(results):
    print(results)


print(time.perf_counter())
workders = (Worker(work, i) for i in range(5))
master = Master(workders, callback=callback)
print("main")
master.wait()

print(time.perf_counter())
```

## Release History
### 0.0.1(2021-01-26)
- Birth
### 1.0.0(2021-10-29)
- Master-Worker mode
- both implement by thread and asyncio

## Author
- <a href="mailto:pmq2008@gmail.com">Rocky Peng</a>
