#create by 6310301022 Weeraphat Thongnoi

#example of starting many tasks and getting access to al tasks
import asyncio
import time

# coroutine for a task
async def task_coroutine(value):
    #report a message
    print(f'{time.ctime()} task {value} is running')
    #block for a moment
    await asyncio.sleep(1)

# define a main coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    #allow some of the tasks time to start
    await asyncio.sleep(0.1)
    #get all tasks
    tasks = asyncio.all_tasks()
    #report all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name}, {task.get_coro()}')
    #await for all tasks to complete
    for task in started_tasks:
        await task

#start the asyncio program
asyncio.run(main()) 

# Wed Jul 12 20:55:21 2023 main coroutine started
# Wed Jul 12 20:55:21 2023 task 0 is running
# Wed Jul 12 20:55:21 2023 task 1 is running
# Wed Jul 12 20:55:21 2023 task 2 is running
# Wed Jul 12 20:55:21 2023 task 3 is running
# Wed Jul 12 20:55:21 2023 task 4 is running
# Wed Jul 12 20:55:21 2023 task 5 is running
# Wed Jul 12 20:55:21 2023 task 6 is running
# Wed Jul 12 20:55:21 2023 task 7 is running
# Wed Jul 12 20:55:21 2023 task 8 is running
# Wed Jul 12 20:55:21 2023 task 9 is running
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9220>, <coroutine object task_coroutine at 0x00000257A3BFC660>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9630>, <coroutine object task_coroutine at 0x00000257A3BFC890>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9080>, <coroutine object main at 0x00000257A3BFC580>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9490>, <coroutine object task_coroutine at 0x00000257A3BFC7B0>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB98A0>, <coroutine object task_coroutine at 0x00000257A3BFC9E0>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB92F0>, <coroutine object task_coroutine at 0x00000257A3BFC6D0>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9700>, <coroutine object task_coroutine at 0x00000257A3BFC900>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9150>, <coroutine object task_coroutine at 0x00000257A3BFC5F0>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB9560>, <coroutine object task_coroutine at 0x00000257A3BFC820>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB93C0>, <coroutine object task_coroutine at 0x00000257A3BFC740>
# Wed Jul 12 20:55:21 2023 > <built-in method get_name of _asyncio.Task object at 0x00000257A3BB97D0>, <coroutine object task_coroutine at 0x00000257A3BFC970>