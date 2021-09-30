import pandas as pd
from pandas.io.parsers import read_csv

def line2list(data):
    ##this function convert row in Data to list
    #Data Type is Dictionary
    l = len(data['From_Bus'])
    
    line = []
    header = ['From_Bus','To_Bus','R','X','G','B','Max_Mvar','Y/2']
    
    for i in range(1,l+1):
        temp = []
        for h in header:
            temp.append(data[h][i])
        line.append(temp)
        
    
    return line

    
def read_line():
    
    #s = read_csv("line_data.csv",delimiter=';')
    
    data = pd.read_csv("line_data.csv",delimiter=';', index_col=0, skiprows=0)
    
    
    print(data)
    
    data = data.to_dict()
    
    line = line2list(data)
    
    return line


def max_line(data):
    # Keymax = max(data['BusB'], key= lambda x: data['BusB'][x])
    # maxi = data['BusB'][Keymax]
    # Keymax = max(data['BusE'], key= lambda x: data['BusE'][x])
    # maxj = data['BusE'][Keymax]
    # return max(maxi,maxj)
    l = len(data)
    temp = []
    for i in range(0,l):
        temp.append(data[i][0])
        temp.append(data[i][1])    
    m = max(temp)
    
    return m
    
def YMatrix(data,Max):
    Y=[]
    temp = []
    for i in range(0,Max):
        temp = []
        for j in range(0,Max):
            temp.append(0)
        Y.append(temp)


    for k in range(0,len(data)):
        i = data[k][0]-1
        j = data[k][1]-1
        Y[i][j] = -(data[k][4]+data[k][5]*1j)
        Y[j][i]=Y[i][j]
        Y[i][i] = Y[i][i] -Y[i][j] + (data[k][7])*1j
        Y[j][j] = Y[j][j] -Y[i][j] + (data[k][7])*1j

    return Y



def Save_matrix(data):
    file = open('matrix.csv','a')
    s = "Index;"
    for  i in range(1,len(data)+1):
         s = s+str(i)+";"  
    file.write(s[:len(s)-1]+"\n")
    l = 1
    for line in data:
        stru = ""
        for i in range(0,len(data)):
            stru = stru+str(line[i])+";"
        stru = stru.replace('(','')
        stru = stru.replace(')','')
        if line == data[len(data)-1]:
            file.write(str(l)+";"+stru[:len(stru)-1])
        else:
            file.write(str(l)+";"+stru[:len(stru)-1]+"\n")
        l= l +1

    file.close
    
    
    

line = read_line()
Max = max_line(line)
matris = YMatrix(line,Max)
Save_matrix(matris)
# print(matris)