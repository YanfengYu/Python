'''
使用协程，计算输入的四个整数，并计算打印出(a+b)*(c+d)
'''
import asyncio
import threading

async def sum(a,b):
    print("计算开始，当前的进程是：{}".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("计算结束，当前的进程是：{}".format(threading.currentThread()))
    return r

loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1,2),sum(3,4))
loop.run_until_complete(task)
r1,r2 = task.result()
print(int(r1)*int(r2))
loop.close()