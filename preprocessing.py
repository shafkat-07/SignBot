import pandas as pd     # data manipulation
import numpy as np      # arrays and matrices
import os               # get file path

def preprocessing():

    # Paths to datasets 
    train_path = os.path.abspath("archive/sign_mnist_train.csv")
    test_path = os.path.abspath("archive/sign_mnist_test.csv")

    # Storing test and training data into dataframes
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    
    # Converting data frame to arrays 
    train_array = np.array(train_data)
    test_array = np.array(test_data)

    # Mapping input(x_train, x_test) to output(y_train, y_test)

    # y = labels (first column)
    y_train = train_data['label'].values         # y = ( 0, 5, 3, e.t.c)
    y_test = test_data['label'].values

    # x = pixels (exluding 1'st column)
    x_train = train_array[: , 1 : ]
    x_test = test_array[ : , 1 : ]

    # Converting to dtype 64 
    x_train = x_train.astype('float64')
    x_test = x_test.astype('float64')

    # Normalizing data (values of pixels between 0 and 1)
    x_train /= 255.0 
    x_test /= 255.0

    # Reshaping to 28 x 28 dimension with 1 channel (greyscale)
    num_rows_train = x_train.shape[0]
    num_rows_test = x_test.shape[0]

    x_train = x_train.reshape(num_rows_train, 28, 28, 1)
    x_test = x_test.reshape(num_rows_test, 28, 28, 1)

    return x_train, x_test, y_train, y_test
