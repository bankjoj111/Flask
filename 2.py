from flask import Flask, render_template_string
import RPi.GPIO as GPIO
app = Flask(__name__)

LED1_PIN = 17  
LED2_PIN = 27 


GPIO.setmode(GPIO.BCM)  
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)


led1_status = 'OFF'
led2_status = 'OFF'

@app.route('/')
def index():
    return render_template_string('''
        <h1>LED Control</h1>
        <p>LED 1 is {{ led1_status }}</p>
        <p>LED 2 is {{ led2_status }}</p>
        
    ''', led1_status=led1_status, led2_status=led2_status)

@app.route('/led1/on')
def led1_on():
    global led1_status
    led1_status = 'ON'
    GPIO.output(LED1_PIN, GPIO.HIGH)  # เปิด LED 1
    return index()


@app.route('/led1/off')
def led1_off():
    global led1_status
    led1_status = 'OFF'
    GPIO.output(LED1_PIN, GPIO.LOW)  # ปิด LED 1
    return index()

@app.route('/led2/on')
def led2_on():
    global led2_status
    led2_status = 'ON'
    GPIO.output(LED2_PIN, GPIO.HIGH)  # เปิด LED 2
    return index()

@app.route('/led2/off')
def led2_off():
    global led2_status
    led2_status = 'OFF'
    GPIO.output(LED2_PIN, GPIO.LOW)  # ปิด LED 2
    return index()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
