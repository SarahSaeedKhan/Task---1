TD_list = []
x = int(input('enter no of rows'))
y = int(input('enter no of columns'))


for row in range(x):
    col = []
    for column in range(y):
        col.append(row*column)
    TD_list.append(col)
print(TD_list)
