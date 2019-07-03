columns = 8
rows = 256 // columns
for i in range(rows) :
    for j in range(columns):
        number =j * rows + i
        print(number, chr(number), end = '\t|\t')
    print( )