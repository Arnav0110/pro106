from statistics import correlation
import plotly.express as px
import csv 
import numpy as np

def getSourceData(data_path):
    marks = []
    present = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            present.append(float(row['Days Present']))
    return{'x': marks, 'y': present}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print('correlation between the percentage vs days present : ', correlation[0,1])

def setUp():
    data_path = 'Student Marks vs Days Present.csv'
    data_source = getSourceData(data_path)
    findCorrelation(data_source)

setUp()
