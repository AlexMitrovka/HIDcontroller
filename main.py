import time
from src.keyboard import Keyboard
from src.mouse import Mouse
from src.controller import ArduinoController

keyboard = Keyboard()
mouse = Mouse()
facade = ArduinoController(keyboard, mouse)
interval = float(0.025)

def main():
    with facade:
            time.sleep(10)
            facade.kbWrite('n')

if __name__ == '__main__':
    main()