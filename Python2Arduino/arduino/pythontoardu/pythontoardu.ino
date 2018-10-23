#define  LED 13

void setup(){
  pinMode(LED,OUTPUT);
}
void loop(){
  if(Serial.available()>0){
    char dataPython = Serial.read();
    Serial.println(dataPython);
  }
}

