from time import sleep
import cv2
from gpiozero import LED
from lobe import ImageModel

model = ImageModel.load('./waste_classifier')

#define LED pins
led = LED(17)
motor_control = LED(27)
empty_count = 0
non_compostable_count = 0


def take_photo():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
    cv2.imwrite('./img.jpg', image)
    cam.release()

def control(label):
    print(label)
    if label == 'N' or label == 'R' or label == 'O':
        empty_count = 0
        if label != 'O':
            non_compostable_count+=1
            led.on() #non compostable detected
        else:
            non_compostable_count = 0
    else:
        empty_count+=1
    if empty_count > 5 or non_compostable_count > 2:
        non_compostable_count = 0 #reset since user cleared the chamber
        empty_count = 6 #cap the empty count to prevent overflow 
        motor_control.off()
    else:
        motor_control.on()

while True:
    take_photo()
    result = model.predict_from_file('./img.jpg')
    control(result.prediction)
    sleep(1)
