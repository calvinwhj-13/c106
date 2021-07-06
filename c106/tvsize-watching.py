import csv
import plotly.express as px
import numpy as np 

def getDataSource(data_path) :
    watching = []
    tvsize = []

    with open(data_path) as csv_file :
        df = csv.DictReader(csv_file)
        for row in df :
            tvsize.append(float(row('Size of TV'))) 
            watching.append(float(row('Average time spent watching TV in a week')))
    return{'x' : tvsize, 'y' : watching}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource['x'], dataSource['y']) 
    print('correlation : \n-->', correlation[0, 1])

def setupMain() :
    path = 'data/tvsize-watching.csv'
    dataSource = getDataSource(path)
    findCorrelation(dataSource)
setupMain() 