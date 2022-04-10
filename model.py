from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

def model_gen():
    
    # Initializing model 
    model = Sequential()

    # Input layer /  first convolutional layer with 16 filters
    model.add(Conv2D(64, (3, 3), input_shape = (28,28,1), activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.20))

    # Second layer 
    model.add(Conv2D(128, (3, 3), input_shape = (28,28,1), activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.20))

    # Third layer
    model.add(Conv2D(64, (3, 3), input_shape = (28,28,1), activation='relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.20))

    model.add(Flatten())
    model.add(Dense(units = 512, activation = 'relu'))
    model.add(Dropout(0.25))
    model.add(Dense(units = 25, activation = 'softmax'))

    model.compile(loss ='sparse_categorical_crossentropy', optimizer='adam' ,metrics =['accuracy'])

    return model