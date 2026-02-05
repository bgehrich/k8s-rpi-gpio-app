# based on https://code-workbench.com/2025/04/10/enabling-gpio-use-from-kubernetes-pod/

from flask import Flask
from gpiozero import Button, LED 
from signal import pause

app = Flask(__name__)

led = LED(26) # Assuming LED on GPIO 17
button = Button(4)

@app.route('/led/')
def led_status():
    if led.is_active:
        return "Turning is on"
    else:
       return "Turning is off"

@app.route('/led/on')
def turn_on():
    led.on()
    return "Turning LED on"

@app.route('/led/off')
def turn_off():
    led.off()
    return "Turning LED off"


@app.route('/button/')
def button_status():
    if button.is_active:
        return "Button is on"
    else
        return "Button is off"
    

if __name__ == '__main__':
    print("app started")
    app.run(host='0.0.0.0', port=5000)
