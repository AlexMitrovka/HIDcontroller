#include <AsyncStream.h>
#include <Keyboard.h>
#include <AbsMouse.h>

AsyncStream<100> serial(&Serial, '\n');

void setup() {
  Serial.begin(9600);
  AbsMouse.init(1680, 1050);
  Keyboard.begin();
  serial.setEOL(';');
}

void loop() {
  if (serial.available()) {
      processCommand(serial.buf);
    }
}

void processMouseCommand(char *command) {
  int key;
  int x, y;
  switch (command[0]) {
    case 'M':
      switch (command[1]) {
        case 'P': // press
          key = atoi(&command[2]);
          AbsMouse.press(key);
          Serial.write(1);
          break;
        case 'R': // release
          key = atoi(&command[2]);
          AbsMouse.release(key);
          Serial.write(1);
          break;
        case 'C': // click
          key = atoi(&command[2]);
          AbsMouse.press(key);
          delay(25);
          AbsMouse.release(key);
          Serial.write(1);
          break;
        case 'V': // move
          x = atoi(&command[2]);
          y = atoi(strchr(&command[2], ',') + 1);
          Serial.println(x);
          Serial.println(y);
          AbsMouse.move(x, y);
          Serial.write(1);
          break;
      }
      break;
  }
}

void processKeyboardCommand(char *command) {
  int key;
  switch (command[0]) {
    case 'K':
      switch (command[1]) {
        case 'P': // press
          key = atoi(&command[2]);
          Keyboard.press(key);
          Serial.write(1);
          break;
        case 'R': // release
          key = atoi(&command[2]);
          Keyboard.release(key);
          Serial.write(1);
          break;
        case 'W': // write
          key = atoi(&command[2]);
          Keyboard.write(key);
          Serial.write(1);
          break;
        case 'T': // print
          Keyboard.print(&command[2]);
          Serial.write(1);
          break;
      }
      break;
    case 'R': // release all
      Keyboard.releaseAll();
      Serial.write(1);
      break;
  }
}

void processCommand(char *command) {
  if (command[0] == 'M') {
    processMouseCommand(command);
  } else if (command[0] == 'K') {
    processKeyboardCommand(command);
  }
}
