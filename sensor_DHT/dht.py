# dht11 모듈을 사용하기 위해서는 사전에 설치가 필요
# 터미널을 실행하여 아래 명령어를 입력하여 설치할 수 있음
# pip install dht11
import RPi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

pin = 5
instance = dht11.DHT11(pin)

# 라즈베리 파이의 GPIO 21번 핀이 DHT 센서의 데이터 핀(2번 핀)에 연결된 상태인 경우


try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: % -3.1f C" % result.temperature)
            print("Humidity: % -3.1f %%" % result.humidity)
    		
        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()


