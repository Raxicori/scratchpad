import sys, os

"""Script that will take a number and print out all primes below that number
"""

def Usage():
    """Function to print correct usage of the script
    """
    print "Correct Usage:"
    print "python primesBelow.py <integer>"

def generate_dict(length):
    """Take an integer and create a dictionary of every number between 2 and that integer paired with 'True'
    """
    primeDict = {}
    index = 2
    
    while (index < length):
        primeDict[index]=True
        index = index+1
    
    return primeDict

def eliminate_non_primes(primes_dict, highest):
    """Take a dict of ints paired with True and return only the prime numbers
    """
    for i in range(2, highest):
        if primes_dict[i] == True:
            loop =1
            for j in range(i**2, highest, i*loop):
                primes_dict[j]=False
                loop = loop+1
    
    primes = []
    for i in range(2, highest):
        if primes_dict[i] == True:
            primes.append(i)
    
    return primes

def main(argv):

    if len(argv) !=1:
        Usage();
        sys.exit();
        
    highest = int(argv[0])
        
    numbers = generate_dict(highest)
    primes = eliminate_non_primes(numbers, highest)
    print primes
        
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))