
def printmath(row):
    for cal in range(1,row+1):
        print(cal*row,end=" ")
    print("")


for row in range(1,10):
    print(printmath(row))


