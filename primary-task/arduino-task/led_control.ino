const int ledPin = 13;
const int buttonPin = 2;
bool blinkMode = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    blinkMode = !blinkMode;
    while(digitalRead(buttonPin) == LOW);
      delay(50);
  }
  if (blinkMode) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  } else {
    digitalWrite(ledPin, LOW);  // Keep LED off
  }
}