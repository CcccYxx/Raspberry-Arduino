# Tflite with Raspberry Pi

## Raspberry Pi OS
All code is tested using a Raspberry Pi 3 (1GB RAM) with Raspberry Pi OS (32-bit). 

## How to run 
1. Clone the repo onto your raspberry pi:\
`git clone https://github.com/CcccYxx/Raspberry-tflite.git` 
2. Go to the root of this Repo and run the quick setup code: (make sure python3 and pip is installed):\
`chmod 777 ./get_pi_req.sh`\
`./get_pi_req.sh`
3. Run the python script:(make sure a USB webcam is connected, and the GPIO pin connection is as specified in `control.py`):\
`./python3 control.py`\
You will see predicted label being printed out in current terminal.


## Reference

- The model was trained using [Lobe](https://www.lobe.ai/) with [this](https://www.kaggle.com/datasets/sapal6/waste-classification-data-v2) dataset.

- The quick setup scrip is adapted and modified from [this](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/get_pi_requirements.sh) tutorial.