import csv
import plotly.express as px
import numpy as np 

def getDataSource(data_path) :
    icecreamsales = []
    temperature = []

    with open(data_path) as csv_file :
        df = csv.DictReader(csv_file)
        for row in df :
            icecreamsales.append(float(row('Ice-cream Sales'))) 
            temperature.append(float(row('Temperature')))
    return{'x' : temperature, 'y' : icecreamsales}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource['x'], dataSource['y']) 
    print('correlation between temperature and ice cream sales : \n-->', correlation[0, 1])

def setupMain() :
    path = 'data/temp-icecream.csv'
    dataSource = getDataSource(path)
    findCorrelation(dataSource)
setupMain() 