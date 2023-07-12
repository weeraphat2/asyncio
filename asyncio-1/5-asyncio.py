#create by 6310301022 Weeraphat Thongnoi

# example of waiting for all tasks to complete

import random
import asyncio
import time

# coroutine for a task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

#main coroutine
async def main():
    # create many tasks 
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    #wait for all tasks to complete #ALL_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report its details
    print(f'{time.ctime()} All done')

#start the asyncio program
asyncio.run(main())

# Wed Jul 12 21:17:22 2023 >task 9 done with 0.030183848182936512
# Wed Jul 12 21:17:22 2023 >task 4 done with 0.04435036583328311
# Wed Jul 12 21:17:22 2023 >task 7 done with 0.11951637227530154
# Wed Jul 12 21:17:22 2023 >task 3 done with 0.1300030187776644
# Wed Jul 12 21:17:22 2023 >task 0 done with 0.17648314621999872
# Wed Jul 12 21:17:22 2023 >task 6 done with 0.2325117840170311
# Wed Jul 12 21:17:22 2023 >task 1 done with 0.3088570321440426
# Wed Jul 12 21:17:23 2023 >task 8 done with 0.7338261424830007
# Wed Jul 12 21:17:23 2023 >task 2 done with 0.957876805908235
# Wed Jul 12 21:17:23 2023 >task 5 done with 0.9918168669759446
# Wed Jul 12 21:17:23 2023 All done