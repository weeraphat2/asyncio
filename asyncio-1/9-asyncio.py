#example of an asynchronous iterator with async for loop
import asyncio
import time

#define an asynchronous iterator
class AsyncIterator():
    #constructor, define some state
    def __init__(self):
        self.counter = 0
    
    #create an instance of the iterator
    def __aiter__(self):
        return self

    #return the next awaitable
    async def __anext__(self):
        # check for no furture items
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the couter
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        #return the couter value
        return self.counter

#main coroutine
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(f'{time.ctime()} {time}')
#execut the asyncio program
asyncio.run(main())

# Wed Jul 19 14:45:09 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:10 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:11 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:12 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:13 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:14 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:15 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:16 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:17 2023 <module 'time' (built-in)>
# Wed Jul 19 14:45:18 2023 <module 'time' (built-in)>