from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2


#image path
path_img = 'face2.jpg'

#output stored in file 
path_dat = 'shape_predictor_68_face_landmarks.dat'


# initializes dlib's face detector
detector = dlib.get_frontal_face_detector()

#creates landmark points
predictor = dlib.shape_predictor(path_dat)


# loads the input image, resize it, and convert it to grayscale
image = cv2.imread(path_img)
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def plot_jawline(shape):
	'''input: takes shape array having
	coordinates of landmark points and
	plots the jawline of the detected face'''

	jaw_points = []

	#only the first 17 points contribute to the jawline
	for i in range(17):
		jaw_points.append([shape[i]])
	jaw_points = np.array(jaw_points)
	cv2.polylines(image, [jaw_points], 0, (153, 76, 0), 3)


def plot_landmarks(shape):
	'''input: takes shape array having
	coordinates of landmark points and
	plots all the landmarks points on the face'''

	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), 1)


def store_points(shape, i):
	'''input: takes shape array having
	coordinates of landmark points and
	stores their coordinates in a text file'''

	with open('points.txt', 'a') as my_data_file:
		my_data_file.write('Person '+str(i) + '\n')
		for (x, y) in shape:
			my_data_file.write(str([x , y]) + '\n')



# detects faces in grayscale
rects = detector(gray, 1)

#for plotting landmark points on the face
for (i, rect) in enumerate(rects):
	
	# determine the facial landmarks for the face region, then
	shape = predictor(gray, rect)

	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	shape = face_utils.shape_to_np(shape)

	# convert dlib's rectangle to a OpenCV-style bounding box
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 204), 2)

	
	cv2.putText(image, "Person #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
	


	plot_landmarks(shape)
	plot_jawline(shape)
	store_points(shape, i+1)

# show the output image 
cv2.imshow("Landmark image", image)
cv2.waitKey(0)