from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import append
import csv
import pandas as pd
import math as mt


def mat2list(mat): ### Convert Dictionary Y to List 
    l = len(mat['1'])
    
    line = []
    
    
    for i in range(1,l+1):
        temp = []
        for h in range(1,l+1):
            temp.append(eval(mat[str(h)][i]))
        line.append(temp)

    return line

 
def read_matrix():### Read CSV file and convert to dictionary
    data = pd.read_csv("matrix.csv",delimiter=';', index_col=0, skiprows=0)
    
    
    # print(data)
    
    data = data.to_dict()
    
    line = mat2list(data)
    
    return line 


def Bus2list(buslist):### Convert Bus Data to list

    l = len(buslist['Bus'])
    
    header = ["Bus","BusType","V","Delta","Pload","Qload","Pgen","Qgen","Qmin","Qmax"]
    
    line = []
    
    for i in range(1,l):
        temp = []
        for h in header:
            temp.append(buslist[h][i])
        line.append(temp)
    
    return line

    
def read_Bus():### Read CSV file to dictionary
    data = pd.read_csv("Bus_data.csv",delimiter=';', index_col=0, skiprows=0)
    
    
    print(data)
    
    data = data.to_dict()
    
    line = Bus2list(data)
    
    return line 

def volt_new(bus,volt_old):
    new_volt = 1
    return new_volt
    
def q_new(bus,volt):
    
    return bus

def goas_sidel(bus,Ymat):

    return bus

Ymat = read_matrix()
Bus = read_Bus()

