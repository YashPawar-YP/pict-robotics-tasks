Arduino LED Control using Push button

1.Description:-
The Arduino control led project demonstrates how to controll a led using a push button. Each button press toggles the led between blinking and off states.

2.Components:-
- Arduino Uno (simulated using Wokwi)
- LED
- Push Button
- 220Ω Resistor
- Jumper Wires

3.Wiring:-
- LED anode → Pin 13
- LED cathode → 220Ω resistor → GND
- Push button → Pin 2 and GND
- Button is configured using INPUT_PULLUP

4.Working:-
- The led pin is connected to pin 13 and the push button is connected to pin 2.
- When the program starts, the led is turned off.
- The button is set using 'INPUT_PULLUP', so the button gives reading LOW when it is pressed.
- The Arduino continuously checks the state of the button in the loop.
- When the button is pressed once, the program changes the blink mode from off to on.
- In blink phase, the led turns on and off with a delay, which makes it blink.
- When the button is pressed again, the blink mode is turned off and the led stops blinking.

5.Simulation:-
This Arduino project is built and tested using Wokwi simulator.