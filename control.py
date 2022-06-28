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

    def control(self, label):
        print(label)
        if label == 'N' or label == 'R' or label == 'O':
            self.empty_count = 0
            if label != 'O':
                self.non_compostable_count+=1
                self.led.on() #non compostable detected
            else:
                self.non_compostable_count = 0
        else:
            self.empty_count+=1
        if self.empty_count > 5 or self.non_compostable_count > 2:
            self.non_compostable_count = 0 #reset since user cleared the chamber
            self.empty_count = 6 #cap the empty count to prevent overflow 
            self.motor_control.off()
        else:
            self.motor_control.on()

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
