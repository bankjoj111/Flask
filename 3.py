from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

# กำหนดหมายเลขพิน GPIO สำหรับหลอด LED
LED1_PIN = 17  # เปลี่ยนเป็นหมายเลขพินที่คุณใช้
LED2_PIN = 27  # เปลี่ยนเป็นหมายเลขพินที่คุณใช้


GPIO.setmode(GPIO.BCM)  
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

# สถานะของหลอด LED
led1_status = 'OFF'
led2_status = 'OFF'

@app.route('/')
def index():
    return render_template_string('''
        <h1>LED Control</h1>
        <p>LED 1 is {{ led1_status }}</p>
        <p>LED 2 is {{ led2_status }}</p>
        
        <form method="POST" action="/led1/on">
            <button type="submit">Turn LED 1 ON</button>
        </form>
        <form method="POST" action="/led1/off">
            <button type="submit">Turn LED 1 OFF</button>
        </form>
        <form method="POST" action="/led2/on">
            <button type="submit">Turn LED 2 ON</button>
        </form>
        <form method="POST" action="/led2/off">
            <button type="submit">Turn LED 2 OFF</button>
        </form>
    ''', led1_status=led1_status, led2_status=led2_status)

@app.route('/led1/on', methods=['POST'])
def led1_on():  
    global led1_status
    led1_status = 'ON'
    GPIO.output(LED1_PIN, GPIO.HIGH)  # เปิด LED 1
    return index()

@app.route('/led1/off', methods=['POST'])
def led1_off():
    global led1_status
    led1_status = 'OFF'
    GPIO.output(LED1_PIN, GPIO.LOW)  # ปิด LED 1
    return index()

@app.route('/led2/on', methods=['POST'])
def led2_on():
    global led2_status
    led2_status = 'ON'
    GPIO.output(LED2_PIN, GPIO.HIGH)  # เปิด LED 2
    return index()

@app.route('/led2/off', methods=['POST'])
def led2_off():
    global led2_status
    led2_status = 'OFF'
    GPIO.output(LED2_PIN, GPIO.LOW)  # ปิด LED 2
    return index()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    GPIO.cleanup()  # ทำความสะอาด GPIO
    return "Shutting down...", 200

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()  # ทำความสะอาด GPIO เมื่อโปรแกรมหยุด

