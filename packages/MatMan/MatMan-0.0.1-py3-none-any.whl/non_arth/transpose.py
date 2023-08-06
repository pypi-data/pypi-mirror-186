# Program to transpose a matrix using a nested loop

def trans_1x3(X):
    result = [[0],
             [0],
             [0]]

    # iterate through rows
    for i in range(len(X)):
       # iterate through columns
       for j in range(len(X[0])):
           result[j][i] = X[i][j]

    for r in result:
       print(r)
       
def trans_2x3(X):
    result = [[0,0],
             [0,0],
             [0,0]]

    # iterate through rows
    for i in range(len(X)):
       # iterate through columns
       for j in range(len(X[0])):
           result[j][i] = X[i][j]

    for r in result:
       print(r)

def trans_3x3(X):
    result = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    # iterate through rows
    for i in range(len(X)):
       # iterate through columns
       for j in range(len(X[0])):
           result[j][i] = X[i][j]

    for r in result:
       print(r)
