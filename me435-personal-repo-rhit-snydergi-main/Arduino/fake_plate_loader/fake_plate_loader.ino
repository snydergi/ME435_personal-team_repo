bool isStringComplete = false;
String inputString = "";

void setup(){
    Serial.begin(19200);
    inputString.reserve(200);
}

void loop(){
    if(isStringComplete){
        if(inputString.equals("RESET")){
            Serial.println("READY,  SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
        } else if(inputString.equals("INITIALIZE")){
            Serial.println("READY,  SAGIAN PE Loader, ROM Ver. 1.1.6, 12APR2001");
        } else if(inputString.startsWith("MOVE ")){
            Serial.println("READY");
        } else if(inputString.startsWith("X-AXIS")){
            Serial.println("READY");
        } else if(inputString.startsWith("Z-AXIS")){
            Serial.println("READY");
        } else if(inputString.equals("GRIPPER OPEN")){
            Serial.println("READY, OPEN");
        } else if(inputString.equals("GRIPPER CLOSE")){
            Serial.println("READY, CLOSED, PLATE");
        } else if(inputString.equals("LOADER STATUS")){
            Serial.println("READY, POSITION ");
        } else {
            Serial.print("Unkown command --> ");
            Serial.println(inputString);
        }
        inputString = "";
        isStringComplete = false;
    }
}

void serialEvent(){
    while(Serial.available()){
        char inChar = (char) Serial.read();
        if(inChar == '\n'){
            isStringComplete = true;
        } else {
            inputString += inChar;
        }
    }
}