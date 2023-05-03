def check_inputs(X, y):

  # Convert inputs to numpy arrays
  X = np.asarray(X)
  y = np.asarray(y)

  if X.shape.__len__() != 2:
    raise ValueError("X should be a 2D array!")
  
  if y.shape.__len__() != 1:
    raise ValueError("y should be a 1D array!")
  
  if X.shape[0] != y.shape[0]:
    raise ValueError("X and y lenghtes are inconsistent!")
  
  if not np.issubdtype(X.dtype, np.number) or np.isnan(X).any():
    raise ValueError("All values in X must be numeric and there can be no NaNs!")
  
  if not np.issubdtype(y.dtype, np.number) or np.isnan(y).any():
      raise ValueError("All values in y should be numeric and there can be no NaNs!")
  
  return X, y
   
check_inputs(X, df['Y'])

