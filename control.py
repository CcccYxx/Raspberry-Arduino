from time import sleep
import cv2
from gpiozero import LED
from lobe import ImageModel

class Img_detect:
    def __init__(self, led_pin = 17, motor_c_pin = 27):
        self.model = ImageModel.load('./waste_classifier')
        self.led = LED(led_pin)
        self.motor_control = LED(motor_c_pin)
        self.empty_count = 0
        self.non_compostable_count = 0


    def take_photo(self):
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        cv2.imwrite('./img.jpg', image)
        cam.release()

    def control(self, label, cap = 2):
        '''
        Motor will stop after consequtive non compostable indicated by `cap`
        LED will light up indicating non compostable materials entered 
        '''
        print(label)
        if label == 'N' or label == 'R' or label == 'O':
            self.empty_count = 0
            if label != 'O':
                self.non_compostable_count+=1
                self.led.on() #non compostable detected
            else:
                self.motor_control.on()
                self.led.off()
                self.non_compostable_count = 0
        else:
            self.empty_count+=1
        if self.empty_count > cap or self.non_compostable_count > cap:
            self.non_compostable_count = cap+1 #cap the counter to prevent overflow 
            self.empty_count = cap+1 #cap the empty count to prevent overflow 
            self.motor_control.off()

    def run(self):
        while True:
            self.take_photo()
            result = self.model.predict_from_file('./img.jpg')
            self.control(result.prediction)
            sleep(1)

def main():
    img_detect = Img_detect()
    img_detect.run()

if __name__ == "__main__":
    main()
