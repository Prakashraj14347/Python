def pascal(row,column):
    if (column==1):
        return 1
    if (column==row):
        return 1
    upLeft=pascal(row-1,column-1)
    upRight=pascal(row-1,column)
    return upLeft+upRight
for r in range(1,7):
    for c in range(1,r+1):
        print(pascal(r,c),end=" ")
    print("")