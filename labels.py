import pandas as pd
from pandas.io.json import json_normalize

filePath= "C:/@DriveE/@ Ryerson/@Conference Papers/AnomalyDetection/packages/anomalyDet36/"
fileName = "combined_labels.json"
inputFile = filePath + fileName


my_dict = dict(inputFile)
df = pd.DataFrame.from_dict(my_dict, orient='index')

#df = pd.DataFrame.from_dict(json_normalize(inputFile), orient='columns')
print(df)