import time
import threading

from keyboard import Keyboard
from mouse import Mouse
from bot import Facade
import asyncio

keyboard = Keyboard()
mouse = Mouse()
facade = Facade(keyboard, mouse, port='COM135', baudrate=9600)
inveterval = float(1.25)
""""""
start_time = time.time()
async def my_async_function():
        async with facade as b:
            for i in range(1,21):
                await b.kbPrint('Hello')
                await b.move(500,500)
                await b.move(100, 800)
asyncio.run(my_async_function())
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")