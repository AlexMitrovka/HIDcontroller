from keyboard import Keyboard
import asyncio
keyboard_example = Keyboard()


async def main():
   await keyboard_example.start()
asyncio.run(main())