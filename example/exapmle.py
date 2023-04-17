import time
from src.keyboard import Keyboard
from src.mouse import Mouse
from src.controller import ArduinoController
from src.keyboardMod import Key, Button

mouse = Mouse()
keyboard = Keyboard()
arduino = ArduinoController(keyboard, mouse)
text="Hello"
with arduino as a: #with connection port
    a.move(100,100)  #Move 100 100
    a.click(Button.L_BUTTON,100,100) #Move 100 100 and left click
    a.drag_and_drop(100,100,200,200,interval=1.25) #drag star with x 100 y 100 move to 200, 200 and drop defaul interval 0.25
    a.kbWrite('H') #Press and realese H
       for letter in text:
             a.kbWrite(letter)
    a.kbPrint('Hello') #Print Hello fast
    a.kbPress('n')
    a.kbRelease('n')
    a.kbReleaseAll()

    """Всі модифікатори кнопок в классі keyboardMod """
    """Так можна запустити диспетчер завдань"""
        a.kbPress(Key.LEFT_CTRL)
        a.kbPress(Key.LEFT_ALT)
        a.kbPress(Key.DELETE)
        a.kbReleaseAll()
