import tensorflow as tf
import numpy as np
import cv2
from environment import Environment
from PIL import Image

class Webcam():
    def __init__(self):
        self.key = cv2.waitKey(1)
        self.webcam = cv2.VideoCapture(0)

    def capture(self):
        _, frame = self.webcam.read()
        return frame

labels = {0:"Jumping", 1:"Ducking", 2:"Running"}

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Enable webcam
webcam = Webcam()

# Load the model
model = tf.keras.models.load_model('model.h5')

# Initialize environment
env = Environment("127.0.0.1", 9090)
env.start_game() 

while True:
    try:
        # Capture image from webcam
        raw_image = webcam.capture()

        # Resize image to 224x224 and convert it to numpy array
        resized_image = np.asarray(Image.fromarray(raw_image).resize((224, 224)))

        # Normalize the image
        normalized_image = (resized_image.astype(np.float32) / 127.0) - 1

        # Predict the image class
        prediction = np.argmax(model.predict([[normalized_image]]))

        # Perform the corresponding action to the browser
        env.do_action(prediction)

        # Show result
        text = labels[prediction]
        cv2.putText(raw_image, text, (50, 75,), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
        cv2.imshow("Capturing", raw_image)

        key = cv2.waitKey(1)

    except(KeyboardInterrupt):
        print("Turning off camera.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
