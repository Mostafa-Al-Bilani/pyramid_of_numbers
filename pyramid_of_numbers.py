rows = int(input("choose number of rows:"))

for columns in range(1, rows + 1): #we use the range of (1, rows + 1) to start from 1 and include the number chosen by the user   
        print(columns, end = "") # we print the i and end"" is used to print on the same line
        for j in range(1, columns): #  This loop iterates for the columns.
            print(columns, end = "")
        print() # Move to the next line after finishing the current row.