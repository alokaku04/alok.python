def grid(row, column):
        for rows in range(0, row):
                for columns in range(0, column):
                        print ('+', end='')
                        for z in range(0, 4):
                                print ('-', end='')
                print ('+')
                for y in range(0, 4):
                        for columns in range(0, column):
        
        for columns in range(0, column):
                        print ('+', end='')
                        for z in range(0, 4):
                                print ('-', end='')
        print ('+')
grid(2, 2)
grid(4, 4)