Управління мишею та клавіатурою через Serial порт 
Ця програма дозволяє керувати мишею та клавіатурою за допомогою Serial порту .

Передумови
Для роботи програми необхідно мати наступні бібліотеки:
AsyncStream.h
Keyboard.h
AbsMouse.h

Контролер Arduino
Це клас Python, який служить оболонкою для Arduino, підключеного через послідовний зв’язок. Клас надає методи керування підключеною клавіатурою та мишею. Він використовує serialConnectмодуль для встановлення та підтримки послідовного з’єднання, settingsмодуль для отримання налаштувань, визначених користувачем, і модулі keyboardта mouseдля надсилання команд на підключені пристрої.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

В HID.ino вкажіть розширення вашого екрану
AbsMouse.init(1680, 1050);

<----------------------------------------->

передумови
Щоб використовувати цей клас, вам потрібно:

Плата Arduino з встановленими бібліотеками Mouseі Keyboard.
Модулі serialConnect, keyboard, mouse, і settingsвстановлені у вашому середовищі Python.
Базове розуміння програмування на Python і Arduino.
Використання
Спочатку імпортуйте необхідні модулі та створіть екземпляр класу:

import time
from keyboard import Keyboard
from mouse import Mouse
from arduino_controller import ArduinoController

keyboard = Keyboard()
mouse = Mouse()
controller = ArduinoController(keyboard, mouse)
Щоб використовувати методи клавіатури, викликайте методи:
kbPress(), kbWrite(), kbRelease(), kbReleaseAll()або kbPrint(), передаючи відповідні аргументи:

controller.kbPress('a')
controller.kbWrite('Hello, world!')
controller.kbRelease('a')
controller.kbReleaseAll()
controller.kbPrint('Hello, world!')
Щоб використовувати методи миші, викликайте методи pressKey(), releaseKey(), move(), drag_and_drop()або click(), передаючи відповідні аргументи:

controller.pressKey(1)  # left mouse button
controller.releaseKey(1)
controller.move(100, 100)
controller.drag_and_drop(100, 100, 200, 200)
controller.click(1, 300, 300)
Зауважте, що click() метод може приймати необов’язкові аргументи xта yаргументи, які вказують позицію курсора миші, де має бути виконано клацання.
