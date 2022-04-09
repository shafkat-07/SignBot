import os
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    # reading in test and training data into dataframe
    test_data = pd.read_csv("archive/sign_mnist_test.csv")
    train_data = pd.read_csv("archive/sign_mnist_train.csv")
    
    # collecting training data
    y_train = train_data['label'].values
    train_data = train_data.drop(columns=['label']) # dropping label column
    x_train = train_data.to_numpy()[1:]

    # reshaping x data to 28x28 array
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
    x_train = x_train.astype('float64')/ 255.0

    print(x_train)
    # collecting test data
    y_test = test_data['label'].values
    test_data = test_data.drop(columns=['label']) # dropping label column
    x_test = test_data.to_numpy()[1:]
    #print(x_test)
    

    
main()
