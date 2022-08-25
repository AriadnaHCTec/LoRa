/*
Made by:Raúl López Musito 
        A01378976@tec.mx
Modified (DD/MM/YY): 
        Raúl López  17/08/2022 Creation 
*/

#include <LoRa.h>
#include "boards.h"

int counter = 0;

int cm = 0;
String incomingByte;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
    initBoard();
    // When the power is turned on, a delay is required.    
    delay(1500);

    Serial.println("LoRa Sender");
    LoRa.setPins(RADIO_CS_PIN, RADIO_RST_PIN, RADIO_DI0_PIN);
    if (!LoRa.begin(LoRa_frequency)) {
        Serial.println("Starting LoRa failed!");
        while (1);
    }
}

void loop()
{
    //Serial.print("Sending packet: ");
    
    
    
    
    /*cm = 0.01723 * readUltrasonicDistance(13, 2);
    Serial.println(cm);*/
    if (Serial.available() > 0) {
      // read the incoming byte:
      incomingByte = Serial.readString();
  
      // say what you got:
      Serial.print("I received: ");
      Serial.println(incomingByte);
      LoRa.print(incomingByte);
      LoRa.endPacket();
    }
    // send packet
    /*LoRa.beginPacket();
    //LoRa.print("hello ");
    LoRa.print(cm);
    LoRa.endPacket();*/

#ifdef HAS_DISPLAY
    if (u8g2) {
        char buf[256];
        u8g2->clearBuffer();
        u8g2->drawStr(0, 12, "Transmitting: OK!");
        snprintf(buf, sizeof(buf), "Sending: %s", incomingByte);
        u8g2->drawStr(0, 30, buf);
        u8g2->sendBuffer();
    }
#endif
    /*counter++;
    delay(5000);*/
}
