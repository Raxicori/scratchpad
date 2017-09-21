import os, sys
'''
This script will take an input file and it will output the file in reverse line order to reversed_<filename>
It is intended to be used as a way to reserve a list, but it will reverse any file with multiple lines.
'''
def read_file_to_list(filename):
    '''Given a filename, open the file and save each line as an item in a list.'''
    returnList=[]
    f = open(filename, 'r')
    for line in f:
        returnList.append(line)
    f.close()
    return returnList

def reverse_list(inputList):
    '''Reverse the contents of <inputList>.'''
    outputList=[]
    for i in range(len(inputList)):
        outputList.append(inputList.pop())
    return outputList

def output_to_file(filename, outputList):
    '''Save <outputList> to a file called <filename>.'''
    f= open(filename, 'w')
    for el in outputList:
        f.write(str(el))
        print el
    f.close
    print "List written to: "+str(filename)

def main(argv):
    inputList = read_file_to_list(argv[0])
    outputList = reverse_list(inputList)
    output_to_file("reversed_"+str(argv[0]), outputList)
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))