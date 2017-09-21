import os, sys

"""Script that will take a grid and print out the highest diagonal product
"""

def Usage():
    """Function to print correct usage of the script
    """
    print "Correct Usage:"
    print "python diagonalProduct.py <grid file>"

def calculate_highest_row_product(rows):
    print rows[0]

def import_grid(gridFile):
    f = open(gridFile, 'r')
    f2 = open(gridFile, 'r')
    lines = f2.read().splitlines()
    retlines=[]
    for el in lines:
        row = el.split()
        retlines.append(row) 
    return f.read(), retlines

def extract_columns(rows):
    columns = []
    for row in rows:
        columns.append([])
    for row in rows:
        marker = 0
        for el in row:
            columns[marker].append(el)
            marker = marker +1
    return columns

def generate_right_diagonals(rows):
    right_diagonals = []
    
    for row in rows:
        for el in row:
            right_diagonals.append([])
            
    
    return right_diagonals

def main(argv):

    if len(argv) !=1:
        Usage();
        sys.exit();
        
    grid, rows = import_grid(argv[0])
    #print grid
    print rows
    columns = extract_columns(rows)
    print columns
    right_diagonals = generate_right_diagonals(rows)

if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))