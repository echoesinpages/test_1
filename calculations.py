import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  #the above block gets a exception if the list does not have nine numebrs , its like a constraint
  
  #creating a matrix of 3x3 size
  matrix = np.array(list).reshape((3,3))

  #creating a dictionary
  calculations = {}

  #calculations for mean
  calculations['mean'] = [matrix.mean(axis=0).tolist(), 
                        matrix.mean(axis=1).tolist(),
                        matrix.mean()]
  
  ##calculations for variance
  calculations['variance'] = [matrix.var(axis=0).tolist(), 
                          matrix.var(axis=1).tolist(),
                          matrix.var()]

  ##calculations for standard deviation
  calculations['standard deviation'] = [matrix.std(axis=0).tolist(), 
                        matrix.std(axis=1).tolist(),
                        matrix.std()]

  ##calculations for maximum
  calculations['max'] = [matrix.max(axis=0).tolist(), 
                        matrix.max(axis=1).tolist(),
                        matrix.max()]

  ##calculations for minimum
  calculations['min'] = [matrix.min(axis=0).tolist(), 
                        matrix.min(axis=1).tolist(),
                        matrix.min()]

  ##calculating the sum
  calculations['sum'] = [matrix.sum(axis=0).tolist(), 
                        matrix.sum(axis=1).tolist(),
                        matrix.sum()]

  return calculations
