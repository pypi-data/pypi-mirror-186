# Program to multiply two matrices using nested loops

def m_3x1(X, Y):
    # result is 3x1
    result = [[0],
             [0],
             [0]]
             
    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    #return 3x1 matrix         
    return result

def m_3x2(X, Y):
    # result is 3x2
    result = [[0,0],
             [0,0],
             [0,0]]

    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    #return 3x2 matrix        
    return result

def m_3x3(X, Y):
    # result is 3x3
    result = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    #return 3x3 matrix        
    return result
