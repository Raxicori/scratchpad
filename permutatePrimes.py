import os, sys
import primesBelow

def remove_below(numbers, lowest):
    """Take a list of numbers and remove everything below <lowest>
    """
    remaining=[]
    for el in numbers:
        if el > lowest:
            remaining.append(el)
    return remaining

def main(argv):
    lowest = int(argv[0])
    highest = int(argv[1])
    numbers = primesBelow.generate_dict(highest)
    print "Numbers Generated"
    primes = primesBelow.eliminate_non_primes(numbers, highest)
    print "Primes Isolated"
    primes = remove_below(primes, 1234)
    print primes
        
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))