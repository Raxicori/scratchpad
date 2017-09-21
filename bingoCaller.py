import os, sys, random

def main(argv):
    numbers = [i for i in range(1,101)]
    while len(numbers) >0:
        random.shuffle(numbers)
        raw_input("Press enter for the next number.")
        print
        print "The next number is: "+str(numbers.pop(0))
        print 

if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))
