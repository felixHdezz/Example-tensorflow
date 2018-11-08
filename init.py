#importing libraries - tensorflow
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def init():
    print ("starting python...")

    #importing the database
    dataset = pd.read_csv("../dataset/MOdelling_database.csv")
    
    _X = dataset.iloc[:,2:13].values
    _Y = dataset.iloc[:, 4].values

    print (_X)
    
    print (_Y)
    
    print (tf.__version__)

if __name__ == "__main__":
    init()
