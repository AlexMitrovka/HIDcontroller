import json
import asyncio
from mouse import Mouse

# self.pos = []
# self.filename = 'pos.json'
# self.mouse = Mouse()

 def start_stop_task(self):
        if self.is_running:
            self.is_running = False
            # Зупинити скрипт
        else:
            self.is_running = True
            # Запустити скрипт

    async def start(self):
        while True:
            event = await asyncio.to_thread(keyboard.read_event)
            if event.event_type == 'down':
                if event.name == 'f2':
                    self.record_mouse_pos()
                elif  event.name == 'f3':
                    self.save_mouse_pos()

    def stop(self):
        keyboard.unhook_all()

    def stop(self):
        keyboard.unhook_all()

    # def get_cursor_position(self):
    #     point = POINT()
    #     ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    #     return point.x, point.y

    def record_mouse_pos(self):
        self.pos.append(self.mouse.get_cursor_position())

    def save_mouse_pos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.pos,f)

    def mouse_release(self, key):
        pass

#keyboard_example = KeyboardExample()

# Создайте асинхронный цикл и запустите метод start() объекта KeyboardExample в цикле
#async def main():
#    await keyboard_example.start()

#asyncio.run(main())