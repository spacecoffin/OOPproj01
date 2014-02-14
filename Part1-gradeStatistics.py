#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION

#classInfo - This function will process the first five lines of the input file that gives information about the course.
#All we need to do is take the appropriate info (thought of as a field) and format it to output as required

def classInfo(fileIn):
    #fileIn should be passed the name of the file to be operated on (preceded by its path if it is not within either the current working directory or the search path)
    f = open(fileIn, 'r')
    #create variable for each field, setting each equal to the appropriate string
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
    print(infoList) 
    f.close()
    
def main():
    classInfo("gradesS.in")

main()
