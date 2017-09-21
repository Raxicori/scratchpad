import os, sys
import primesBelow

def isPandigital(number):
    """Returns True if <number> is pandigital, False otherwise
    """
    sNumber = str(number)
    if len(sNumber) > 9:
        return False
    else:
        digits = []
        n = len(sNumber)
        for i in range(1,n+1):
            digits.append(i)
        for el in sNumber:
            try:
                digits.remove(int(el))
            except(ValueError):
                return False
                sys.exit();
        return True

def main(argv):
    
    highest = int(argv[0])
    numbers = primesBelow.generate_dict(highest)
    print "Numbers Generated"
    primes = primesBelow.eliminate_non_primes(numbers, highest)
    print "Primes Isolated"
    highest = 0
    for el in primes:
        if isPandigital(el):
            highest = el
    print highest
        
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))