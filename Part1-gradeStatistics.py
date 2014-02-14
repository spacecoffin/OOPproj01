#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION

#classInfo - This function will process the first five lines of the input file that gives information about the course.

def classInfo(fileIn):
    #fileIn should be passed the name of the file to be operated on (preceded by its path if it is not within either the current working directory or the search path)
    f = open(fileIn, 'r')
    #plug each variable into the output format and print
    #-or- do we want to pass the vals of the vars for later use?
    x = 5
    infoList = []
    while x > 0:
        line = f.readline()
        parts = line.split(':', 1)
        field = parts[1] # convert item 1 to a string so that it can be stripped of leading and trailing whitespace in the next line
        infoList.append(field.strip())
        x -= 1
    infoAsStr = "{0[0]}, {0[1]}\n{0[2]}\n{0[3]}\n{0[4]}\n".format(infoList)
    print(infoAsStr)
    f.close()
    
def main():
    classInfo("gradesS.in")

main()
