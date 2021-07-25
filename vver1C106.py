import plotly.express as cs
import csv
import numpy as mp
def getdatasrc(datapath):
    marks=[]
    days=[]
    with open(datapath) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}
def findcorolation(datasrc):    
    correlation=mp.corrcoef(datasrc["x"],datasrc["y"])
    print("correlation between marks and and days absent",correlation[0,1])
def setup():
    datapath="D:\Daksh\WhiteHatJr\projects whitehat\C106\Student Marks vs Days Present.csv"
    datasrc=getdatasrc(datapath)
    findcorolation(datasrc)
setup()    




















