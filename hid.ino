#include <AsyncStream.h>
#include <Keyboard.h>
#include <AbsMouse.h>
AsyncStream<100> serial(&Serial, '\n');

void setup() {
  Serial.begin(9600);
  AbsMouse.init(1680, 1050);
  Keyboard.begin();
}

void loop() {
  if (serial.available()) {
    String data = serial.buf;
    String command = "";
    for (int i = 0; i < data.length(); i++) {
      if (data.charAt(i) == ';') {
        processCommand(command);
        command = "";
      } else {
        command += data.charAt(i);
      }
    }

    if (command != "") {
      processCommand(command);
    }
  }
}

void processCommand(String command) {
  // розділити команду на параметри та обробити її
  // наприклад:
  if (command.startsWith("MP")) {
    int key = command.substring(3).toInt();
    mousePress(key);
  } else if (command.startsWith("MR")) {
    int key = command.substring(3).toInt();
    mouseRelease(key);
  } else if (command.startsWith("MC")) {
    int button = command.substring(3).toInt();
    clickMouse(button);
  } else if(command.startsWith("MV")) {
    String params = command.substring(3);
    int x = params.substring(0, params.indexOf(",")).toInt();
    int y = params.substring(params.indexOf(",") + 1).toInt();
    moveMouse(x, y);
  } else if(command.startsWith("KR")) {
    int key = command.substring(3).toInt();
      keyRelease(key);
  } else if(command.startsWith("KP")) {
     int key = command.substring(3).toInt();
      keyPress(key);
  } else if(command.startsWith("KRA")) {
     keyReleaseAll();
  } else if(command.startsWith("KW")) {
    int symbol = command.substring(3).toInt();
    keyWrite(symbol);
  } else if(command.startsWith("PT")) {
    String str = command.substring(3);
    keyPrint(str);
  }
}
//comand exaple:
//MV,X,Y; CLICK,KEY;
//MP,KEY; MR,KEY;
//KP,KEY;
// #define MOUSE_LEFT 01
// #define MOUSE_RIGHT 02
// #define MOUSE_MIDDLE 04
void mousePress(int button){
    AbsMouse.press(button);
}
void mouseRelease(int button){
    AbsMouse.release(button);
}

void clickMouse(int button){
    mousePress(button);
    delay(25);
    mouseRelease(button);
}

void moveMouse(int x, int y){
  AbsMouse.move(x, y);
}

void keyPress(int key){
   Keyboard.press(key);
}

void keyReleaseAll(){
  Keyboard.releaseAll();
}

void keyRelease(int key){
  Keyboard.release(key);
}

void keyWrite(int key){
  Keyboard.write(key);
}

void keyPrint(String text) {
  Serial.print(text);
   Keyboard.print(text);
}
