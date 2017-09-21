import os, sys
import primesBelow

"""Script that will take a number and print out the sum of all primes below that number
"""

def Usage():
    """Function to print correct usage of the script
    """
    print "Correct Usage:"
    print "python sumPrimes.py <integer>"
    
def sum_list(listToSum):
    count = 0
    for el in listToSum:
        count = count + el
    return count

def main(argv):

    if len(argv) !=1:
        Usage();
        sys.exit();
        
    highest = int(argv[0])
        
    numbers = primesBelow.generate_dict(highest)
    primes = primesBelow.eliminate_non_primes(numbers, highest)
    total = sum_list(primes)
    print total
        
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))