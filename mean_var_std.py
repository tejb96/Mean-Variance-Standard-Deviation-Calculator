import numpy as np

def calculate(list):
  arr = np.array(list)
  arr2 = arr.reshape(3, 3)
  print(arr2)
  max1= np.max(arr2, axis=0)
  max2= np.max(arr2, axis=1)
  max= np.max(arr2)
  min1=np.min(arr2, axis=0)
  min2=np.min(arr2, axis=1)
  min= np.min(arr2)
  mean1=np.mean(arr2, axis=0)
  mean2=np.mean(arr2, axis=1)
  mean= np.mean(arr2)
  var1=np.var(arr2,axis=0)
  var2=np.var(arr2,axis=1)
  var=np.var(arr2)
  std1=np.std(arr2,axis=0)
  std2=np.std(arr2,axis=1)
  std=np.std(arr2)
  calculations = [max1,max2,max, min1, min2,min, mean1,mean2,mean,var1, var2, var, std1,std2,std]
  
  return calculations