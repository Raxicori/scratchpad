import sys

def countSymbols(string, symbol):
    count=0
    for el in string:
        if el==symbol:
            count=count+1
    return count

def main(argv):
    if len(argv) != 1:
        print "One email address at a time."
        print "Email address should not contain any spaces."
        sys.exit(0)
    address=str(argv[0])
    atCount=countSymbols(address, '@')
    if atCount != 1:
        print "Email address should contain one \"@\"symbol."
        print "This address contains "+str(atCount)+" and is invalid."
        sys.exit(0)
    splitAddress=address.split('@')
    dotCount=countSymbols(splitAddress[1], '.')
    if (dotCount  <1) or (dotCount >2):
        print "Email address should contain one or two \".x\" extension(s)."
        print "This address contains "+str(dotCount)+" and is invalid."
        sys.exit(0)
    print "Congratulations, "+address+" is a valid email address!"
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))