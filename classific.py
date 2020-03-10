# USAGE
# python test_network.py --model santa_not_santa.model --image images/examples/santa_01.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
def identify(x):
    cam=cv2.VideoCapture(x)
    ret, image = cam.read()
    # cv2.imshow("df",image)
    # cv2.waitKey(0S
    image = cv2.resize(image, (200, 200))
    image = image[50:150, 50:150]
    # cv2.imshow("ed",image)
    # cv2.waitKey(0)
    # load the image
    #image = cv2.imread(path)
    orig = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (28, 28))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network
    print("[INFO] loading network...")
    model = load_model("smart_dustbin.model")

    # classify the input image
    (notSanta, santa) = model.predict(image)[0]

    # build the label
    label = "Paper" if santa > notSanta else "Plastic"
    return label
print(identify(0))
# proba = santa if santa > notSanta else notSanta
# label = "{}: {:.2f}%".format(label, proba * 100)

# # draw the label on the image
# output = imutils.resize(orig, width=400)
# cv2.putText(output, label, (10, 40),  cv2.FONT_HERSHEY_SIMPLEX,
# 	1.2, (0, 0, 255), 4)

# # show the output image
# cv2.imshow('hey', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()