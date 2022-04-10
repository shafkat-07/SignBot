from pyexpat import model
import numpy as np
from keras.models import load_model

# File that completes preprocessing 
import preprocessing
# File that builds model 
from model import model_gen
from predict import predict

def main():
     # if model exists, load existing one else save model 
    try: 
        mod = load_model('image_model')
    except OSError:
        x_train, x_test, y_train, y_test = preprocessing.preprocessing()
        # create model 
        mod = model_gen()
        mod.fit(x_train, y_train, batch_size = 512, epochs = 50, verbose = 1, validation_data = (x_test, y_test))
        mod.save('image_model')
    filename = "w"
    prediction = predict(filename, mod)
    print(prediction)

main()