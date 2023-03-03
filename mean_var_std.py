import numpy as np

def calculate(list):

  if(len(list)!=9):
    raise ValueError('List must contain nine numbers.')
  else:    
  
    arr = np.array(list)
    arr2 = arr.reshape(3, 3)
    
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
    sum1=np.sum(arr2,axis=0)
    sum2=np.sum(arr2,axis=1)
    sum=np.sum(arr2)
    
    calculations = {'mean':[mean1.tolist(),mean2.tolist(),mean.tolist()], 
  'variance':[var1.tolist(),var2.tolist(),var.tolist()], 'standard deviation':[std1.tolist(),std2.tolist(),std.tolist()],'max': [max1.tolist(),max2.tolist(),max.tolist()], 'min': [min1.tolist(),min2.tolist(),min.tolist()], 'sum': [sum1.tolist(),sum2.tolist(),sum.tolist()]} 
  
  
  return calculations