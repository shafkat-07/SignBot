import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt 

# File that completes preprocessing 
import preprocessing
# File that builds model 
from model import model_gen

def main():
    x_train, x_test, y_train, y_test = preprocessing.preprocessing()
    mod = model_gen()

    mod.fit(x_train, y_train, batch_size = 512, epochs = 50, verbose = 1, validation_data = (x_test, y_test))
    


main()