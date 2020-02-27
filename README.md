## USE PYTHON 3x

## INSTALLATION GUIDE:

## Install virtual environment: 
`virtualenv -p python3 envname` 
## Activate the environment: 
`source envname/bin/activate`
## Install the requirements using requirements.txt file: 
`$ pip install -r requirements.txt`

## Run the file: 
`$ python detect.py`

## About the project:
* This project aims to detect facial region and plot landmark points in an image.
* It uses `cv2` and `dlib` library for the same. //explain
* dat file
* The output is in the form of a text file, which contains coordinates of all the 68 landmark points of each face detected in the image.
* The output also shows an image, wherein along with the landmarks, the jawline of the individual can also be traced.


## Output	
![screenshot](hike_scr.png)
