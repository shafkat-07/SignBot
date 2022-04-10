import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Dense
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import BatchNormalization
from keras.callbacks import ReduceLROnPlateau
import warnings
warnings.filterwarnings('ignore')

def letter(label):
    return chr(65 + label)

def main():
    # reading in test and training data into dataframe
    test_data = pd.read_csv("archive/sign_mnist_test.csv")
    train_data = pd.read_csv("archive/sign_mnist_train.csv")
    

    # collecting training data
    y_train = train_data['label'].values
    y_train = to_categorical(y_train, num_classes=25) 
    train_data = train_data.drop(columns=['label']) # dropping label column
    x_train = train_data.to_numpy()
    
    # reshaping x data to 28x28 array
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
    x_train = x_train.astype('float64')/ 255.0
    #print(x_train.shape)

    # collecting test data
    y_test = test_data['label'].values
    test_data = test_data.drop(columns=['label']) # dropping label column
    x_test = test_data.to_numpy()
    y_test = to_categorical(y_test, num_classes=25)
    #print(x_test)
    
    model = Sequential()

    model.add(Conv2D(32, (3,3), strides = 1, padding = "Same",activation ="relu", input_shape =(28,28,1)))
    model.add(MaxPool2D((2,2),strides = 2,padding ="Same"))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3,3), strides = 1, padding = "Same",activation ="relu"))
    model.add(MaxPool2D((2,2),strides = 2,padding ="Same"))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3,3), strides = 1, padding = "Same",activation ="relu"))
    model.add(MaxPool2D((2,2),strides = 2,padding ="Same"))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(128, activation = "relu"))
    model.add(Dropout(0.3))
    model.add(Dense(25,activation = "softmax"))
    model.summary()
    model.compile(loss="sparse_categorical_crossentropy",optimizer='adam',metrics=['accuracy'])
    train_datagen = ImageDataGenerator(rescale = 1./255,
    rotation_range = 40,
    height_shift_range=0.2,
    width_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

    validation_datagen = ImageDataGenerator(rescale = 1./255)
    history = model.fit_generator(train_datagen.flow(x_train ,y_train,batch_size=32), steps_per_epoch = len(x_train)/32, epochs=15, validation_data = validation_datagen.flow(x_test, y_test, batch_size=32), validation_steps = len(x_test)/32)

main()
