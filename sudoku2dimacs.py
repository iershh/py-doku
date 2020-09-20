import math

def sudoku2dimacs(sudoku):
    '''encode a given puzzle in DIMACS format'''
    '''input is a single sudoku line e.g.: ...3..4114..3... for 4x4'''
    '''only works when values of the puzzle are integers'''
    
    sudoku_values = [] # each clause/row in a DIMACS file
    sudoku = sudoku.strip() # remove white spaces
    rc = math.sqrt(len(sudoku)) # nr of rows/columns
    
    for i, value in enumerate(sudoku):
        # only look at the non-empty values
        if value != ".":
            # for each value get the row/column position
            row = (i // int(rc)) + 1 # row nr remains same for each rc values
            column = (i % int(rc)) + 1 # col nr is 1 till rc for each rc values
            rcv = f'{row}{column}{value} 0'
            sudoku_values.append(rcv)
    # list to string with \n between each clause        
    dimacs_sudoku = "\n".join(sudoku_values)
    return dimacs_sudoku