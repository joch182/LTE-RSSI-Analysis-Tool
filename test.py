import glob
data_in = "C:/Users/j00363316.CHINA/Desktop/RSSI Traces Cluster Trial"
files = (glob.glob(data_in+"/*.csv"))
#files = (glob.glob(r'C:\Users\j00363316.CHINA\Desktop\RSSI Traces Cluster Trial\*.csv'))

print(files)