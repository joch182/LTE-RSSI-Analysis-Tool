import os
import glob
from openpyxl import Workbook
import pandas as pd
from scipy.stats.stats import pearsonr
from openpyxl.utils.dataframe import dataframe_to_rows
import math

files = (glob.glob(r'C:\Users\j00363316.CHINA\Desktop\RSSI Traces Cluster Trial\*.csv'))

workbook = Workbook()
sheet = workbook.active

Results = {
    "Cell": [],
    "Ant0 vs Ant1": [],
    "Ant0 vs Ant2": [],
    "Ant0 vs Ant3": [],
    "Ant1 vs Ant2": [],
    "Ant1 vs Ant3": [],
    "Ant2 vs Ant3": []
}

''' Magic Happens here! '''

for i in range(len(files)):
    df = pd.read_csv(files[i],skiprows=9)
    Results['Cell'].append(os.path.splitext(os.path.basename(files[i]))[0])
    Results['Ant0 vs Ant1'].append(pearsonr(df.iloc[:,104],df.iloc[:,105])[0])
    if math.isnan(Results['Ant0 vs Ant1'][i]):
        Results['Ant0 vs Ant1'][i] = -1
    Results['Ant0 vs Ant2'].append(pearsonr(df.iloc[:,104],df.iloc[:,106])[0])
    if math.isnan(Results['Ant0 vs Ant2'][i]):
        Results['Ant0 vs Ant2'][i] = -1
    Results['Ant0 vs Ant3'].append(pearsonr(df.iloc[:,104],df.iloc[:,107])[0])
    if math.isnan(Results['Ant0 vs Ant3'][i]):
        Results['Ant0 vs Ant3'][i] = -1
    Results['Ant1 vs Ant2'].append(pearsonr(df.iloc[:,105],df.iloc[:,106])[0])
    if math.isnan(Results['Ant1 vs Ant2'][i]):
        Results['Ant1 vs Ant2'][i] = -1
    Results['Ant1 vs Ant3'].append(pearsonr(df.iloc[:,105],df.iloc[:,107])[0])
    if math.isnan(Results['Ant1 vs Ant3'][i]):
        Results['Ant1 vs Ant3'][i] = -1
    Results['Ant2 vs Ant3'].append(pearsonr(df.iloc[:,106],df.iloc[:,107])[0])
    if math.isnan(Results['Ant2 vs Ant3'][i]):
        Results['Ant2 vs Ant3'][i] = -1
dataF = pd.DataFrame(data=Results)

''' Magic Ends here! '''

for r in dataframe_to_rows(dataF, index=False, header=True):
    sheet.append(r)

workbook.save(filename="Results.xlsx")