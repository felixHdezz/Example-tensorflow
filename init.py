#importing libraries - tensorflow
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#definition function init
def init():
    print ("starting python...")

    #importing the database

    dataset = pd.read_csv("MOdelling_database.csv")
    
    _X = dataset.iloc[:,2:13].values
    _Y = dataset.iloc[:, 4].values

    print (_X)
    
    print (_Y)

    #print in colosole the tensorflow current version
    print (tf.__version__)

#is function main
if __name__ == "__main__":
    #calling function init
    init()
