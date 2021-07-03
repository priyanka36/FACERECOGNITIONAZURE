import numpy as np
import cv2
from face_detection.settings import *

def detect_face(image):
	# load our serialized model from disk
	print("[INFO] loading model...")
	net = cv2.dnn.readNetFromCaffe(prototxt_file,caffe_model)

	# load the input image and construct an input blob for the image
	# by resizing to a fixed 300x300 pixels and then normalizing it
	# image = cv2.imread(image_path)
	# import pdb;pdb.set_trace()
	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the detections and
	# predictions
	print("[INFO] computing object detections...")
	net.setInput(blob)
	detections = net.forward()

	# 
	detected_boxes = []
	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections[0, 0, i, 2]
		# import pdb;pdb.set_trace()
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > confidence_value:
			# compute the (x, y)-coordinates of the bounding box for the
			# object
			
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			# 
			detected_boxes.append(box)
	 
			# draw the bounding box of the face along with the associated
			# probability
			# text = "{:.2f}%".format(confidence * 100)
			# y = startY - 10 if startY - 10 > 10 else startY + 10
			# cv2.rectangle(image, (startX, startY), (endX, endY),
			# 	(0, 0, 255), 2)
			# cv2.putText(image, text, (startX, y),
			# 	cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
		else:
			# return "No faces found"
			pass
	# import pdb;pdb.set_trace()
	# import pdb;
	# pdb.set_trace()
	return detected_boxes
	
	# # show the output image
	# cv2.imshow("Output", image)
	# cv2.waitKey(0)

if __name__ == '__main__':
	input_image = "/home/priyanka/face_recognition_azure/api_scripts/shushant.jpg"
	image = cv2.imread(input_image)
	result = detect_face(image)

	print(result)