#example of an asynchronous context manager via async with 
import asyncio
import time

import asyncio

#define an asynchronous context manager
class AsyncContextManager:
    #enter the async context manager
    async def __aenter__(self):
        #report a message
        print(f'{time.ctime()} >entering the context manager')
        #block for a moment
        await asyncio.sleep(0.5)

    #exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        #report a message
        print(f'{time.ctime()} >exiting the context manager')
        #block for a moment
        await asyncio.sleep(0.5)

#define a simple coroutine
async def custom_coroutine():
    #create and use the asynchronous context manager
    async with AsyncContextManager() as manager:
        #report the result
        print(f'{time.ctime()} within the manager')

#start the asyncio program
asyncio.run(custom_coroutine())

# Wed Jul 19 14:45:50 2023 >entering the context manager
# Wed Jul 19 14:45:50 2023 within the manager
# Wed Jul 19 14:45:50 2023 >exiting the context manager