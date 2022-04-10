from keras_preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import Sequential
import cv2

def predict(filename, mod):
    img_array = cv2.imread(f'test_pics/{filename}.jpg', )
    img_array = img_array[:,:,0]
    img_array = img_array / 255
    new_array = cv2.resize(img_array, (28, 28))
    new_array = new_array.reshape(1, 28, 28, 1)
    prediction = mod.predict(new_array)
    prediction = np.argmax(prediction[0])
    return prediction


