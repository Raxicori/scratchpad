import os, sys, random

def printBoard(board):
    print "Your board is:"
    for i in range(1,6):
        print board[i]
        
def main(argv):
    bingoBoard = {1:[], 2:[], 3:[], 4:[], 5:[]}
    numbers = [i for i in range(1,101)]
    random.shuffle(numbers)
    
    for el in bingoBoard:
        for i in range(0,5):
            if el==3 and i==2:
                bingoBoard[el].append("X")
            else:
                bingoBoard[el].append(numbers.pop(0))
            
    printBoard(bingoBoard)

if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))
