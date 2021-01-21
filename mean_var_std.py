import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')

  arr = np.array(list).reshape(3,3)
  mean1 = np.mean(arr, axis=0).tolist()
  mean2 = np.mean(arr, axis=1).tolist()
  meanf = np.mean(arr.flatten())
  var1 = np.var(arr, axis=0).tolist()
  var2 = np.var(arr, axis=1).tolist()
  varf = np.var(arr.flatten())
  sd1 = np.std(arr, axis=0).tolist()
  sd2 = np.std(arr, axis=1).tolist()
  sdf = np.std(arr.flatten())
  max1 = np.max(arr, axis=0).tolist()
  max2 = np.max(arr, axis=1).tolist()
  maxf = np.max(arr.flatten())
  min1 = np.min(arr, axis=0).tolist()
  min2 = np.min(arr, axis=1).tolist()
  minf = np.min(arr.flatten())
  sum1 = np.sum(arr, axis=0).tolist()
  sum2 = np.sum(arr, axis=1).tolist()
  sumf = np.sum(arr.flatten())

  calculations = {
    'mean': [mean1, mean2, meanf],
    'variance': [var1, var2, varf],
    'standard deviation': [sd1, sd2, sdf],
    'max': [max1, max2, maxf],
    'min': [min1, min2, minf],
    'sum': [sum1, sum2, sumf]
  }

  print(calculations)

  return calculations