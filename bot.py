import time
from typing import Type
from serialAsync import Connection
from settings import Settings
from keyboard import KeyboardInterface
from mouse import MouseInterface
import asyncio

class Facade:

    def __init__(self, keyboard: Type[KeyboardInterface], mouse: Type[MouseInterface],port,baudrate):
        self.settings = Settings()
        self.keyboard = keyboard
        self.mouse = mouse
        self.port = port
        self.baudrate = baudrate
        # self.connection = Connection(self.settings.com_port, self.settings.baund_rate)
        self.connection = None
        self.loop = asyncio.get_event_loop()

    async def __aenter__(self):
        print("Entering context")
        self.connection = await serial_asyncio.create_serial_connection(
            self.loop,
            lambda: Connection(self.port, self.baudrate),
            limit=0
        )
        return self
        # print("Entering context")
        # await self.connection.connect(None)
        # return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        self.connection.transport.close()
        await self.connection.wait_closed()
        # print("Exiting context")
        # await self.connection.close_connection()

    async def pressKey(self, key):
        await self.connection.send_command(self.mouse.mouse_press(key))

    async def releaseKey(self, key):
        await self.connection.send_command(self.mouse.mouse_release(key))

    async def move(self, x, y):
        await self.connection.send_command(self.mouse.moveTo(x, y))

    def dragAndDrop(self, x, y, x1, y1, duration, KEY=1):
        self.move(x, y)
        time.sleep(1)
        self.pressKey(KEY)
        time.sleep(1)
        self.move(x1, y1)
        time.sleep(1)
        self.releaseKey(KEY)

    async  def click(self, key, x=None, y=None):
        await self.connection.send_command(self.mouse.click(key, x, y))

    async  def kbPress(self, key):
        await self.connection.send_command(self.keyboard.kbdPress(key))

    async  def kbWrite(self, char):
        await self.connection.send_command(self.keyboard.kbdWrite(char))

    async  def kbRelease(self, key):
        await self.connection.send_command(self.keyboard.kbdRelease(key))

    async  def kbReleaseAll(self):
        await self.connection.send_command(self.keyboard.kbdReleaseAll())

    async  def kbPrint(self, str):
        await self.connection.send_command(self.keyboard.kbdPrint(str))


