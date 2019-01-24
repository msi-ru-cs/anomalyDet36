from anomaly_likelihood import AnomalyLikelihood
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import math

filePath= "C:/@DriveE/@ Ryerson/@Conference Papers/AnomalyDetection/packages/anomalyDet36/data/"
fileName = "raw_alpha_realAWSCloudwatch_ec2_cpu_utilization_5f5533.csv"
inputFile = filePath + fileName
dataframe = pd.read_csv(inputFile, header=0)

df = dataframe[["timestamp", "value", "error"]]
print(df.head(5))

df = df.values
print(df.shape)

n = len(df[:,0])
m = len(df[1,:])
result = np.empty_like(df)
print(result.shape)

anomalyLikelihood = AnomalyLikelihood()
#anomalyProbability = anomalyLikelihood.anomalyProbability(value, anomalyScore, timestamp)

for i in range(n):
  anomalyProbability = anomalyLikelihood.anomalyProbability(df[i,1], df[i,2], df[i,0])
  #anomalyProbability = anomalyLikelihood.anomalyProbability(51.8460, 0.95, 1)
  result[i,0] = i
  result[i, 1] = df[i, 1]
  result[i, 2] = anomalyProbability

print(result[385:450, :])


#Creates two subplots and unpacks the output array immediately
plt.figure(figsize=(8,8))


plt.subplot(2,1,1)
plt.plot(result[:,0], result[:,1], c="b", label="Data Points")
plt.legend(loc="upper right")
#plt.title('Data Points')

plt.subplot(2,1,2)
plt.plot(result[:,0], df[:,2], c="g", label="Error")
plt.legend(loc="upper right")

#plt.subplot(3,1,3)
plt.plot(result[:,0], result[:,2], c="r", label="Anomaly Likelihood")
plt.legend(loc="upper right")

plt.show()

