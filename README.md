IT-OCR - Image to Text OCR

IT-OCR extracts text from image using trending OCR technologies.

UI and backend is done using django, so to successfully run the project you need to follow some steps.

Installation Steps

1. Install djnago

2. Project use opencv for image related task, so install opencv using below command.
        pip install opencv-python

3. Project is based on OCR technologies, so we need to install easyocr.
     pip install easyocr

4. EasyOCR uses pytorch library in backend, so pytorch need to install on local device.
     4.1 In some cases PyTorch latest version creates problem for easyocr to import torch, So It is advisible to install pytorch using below command for windows.
           pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
    Note:- If you have preinstalled torch, It is advisable to install torch using above command inorder to successfully run the project.

Now Installation is over.

Steps to run project.

1. Go to folder where manage.py file is located.
2. open that folder in cmd.
3. write command 'python manage.py runserver'.
4. Copy url link and paste it in any browser and project will run successfully.
