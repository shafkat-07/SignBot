import pandas as pd     # data manipulation
import numpy as np      # arrays and matrices
import os               # get file path

def preprocessing():

    # Paths to datasets 
    train_path = os.path.abspath("sign_mnist_train.csv")
    test_path = os.path.abspath("sign_mnist_test.csv")

    # Storing test and training data into dataframes
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    
    # ollecting training data
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
    
    #Defining the Convolutional Neural Network
    model = 0

    cnn_model.fit(x_train, y_train, batch_size = 512, epochs = 50, verbose = 1, validation_data = (x_test, y_test))


### HIS CODE BELOW #######################


train = pd.read_csv('archive/sign_mnist_train.csv')
test = pd.read_csv('archive/sign_mnist_test.csv')


train_set = np.array(train, dtype = 'float32')
test_set = np.array(test, dtype='float32')

# training data set code
X_train = train_set[:, 1:] / 255
y_train = train_set[:, 0]

X_test = test_set[:, 1:] / 255
y_test = test_set[:,0]


X_train = X_train.reshape(X_train.shape[0], *(28, 28, 1))
X_test = X_test.reshape(X_test.shape[0], *(28, 28, 1))