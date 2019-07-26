import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__) #starting flask
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#define actuators GPIOs
led1 = 35
led2 = 36
led3 = 37
led4 = 38


# Define pins as output and turns OFF at startup 
GPIO.setup(led1, GPIO.OUT, initial= GPIO.LOW)    
GPIO.setup(led2, GPIO.OUT, initial= GPIO.LOW) 
GPIO.setup(led3, GPIO.OUT, initial= GPIO.LOW)    
GPIO.setup(led4, GPIO.OUT, initial= GPIO.LOW) 


	
@app.route("/")#creation of landing page
def index():
	# Read LED Status
	led1status = GPIO.input(led1)
	led2status = GPIO.input(led2)
	led3status = GPIO.input(led3)
	led4status = GPIO.input(led4)
        #storing into variables to pass to html file
	templateData = {
              'led1sts'  : led1status,
              'led2sts'  : led2status,
              'led3sts' : led3status,
              'led4sts'  : led4status,
       }
	return render_template('index.html', **templateData)   #redirecting landing page to use external file and passing data to itled'  : ledSts,
              

@app.route("/<deviceName>/<action>")
def control(deviceName, action):
        if deviceName == 'led1':
                actuator = led1
        if deviceName == 'led2':
                actuator = led2
        if deviceName == 'led3':
                actuator = led3
        if deviceName == 'led4':
                actuator = led4
        if action == "on":
                GPIO.output(actuator, GPIO.HIGH)
        elif action == "off":
                GPIO.output(actuator, GPIO.LOW)
        # Read LED Status
	led1status = GPIO.input(led1)
	led2status = GPIO.input(led2)
	led3status = GPIO.input(led3)
	led4status = GPIO.input(led4)
        #storing into variables to pass to html file
	templateData = {
              'led1sts'  : led1status,
              'led2sts'  : led2status,
              'led3sts' : led3status,
              'led4sts'  : led4status,
       }
	return render_template('index.html', **templateData)   #redirecting landing page to use external file and passing data to itled'  : ledSts,
              
        
if __name__ == "__main__": #starts flask server on specified IP address
   app.run(host="0.0.0.0", port=80, debug=True)

        


