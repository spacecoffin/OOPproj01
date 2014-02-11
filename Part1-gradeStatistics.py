#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION


#classInfo - This function will process the first five lines of the input file that gives information about the course.
#All we need to do is take the appropriate info (thought of as a field) and format it to output as required
def classInfo(fileIn): #fileIn should be the name of the file to be operated on
    f = open(fileIn, 'r')
    #create variable for each field, setting each equal to the appropriate string
    #read line 1, set variable "course" equal to text after ":", ignoring whitespace
    #read line 2, set variable "year" equal to text after ":", ignoring whitespace
    #read line 3, set variable "university" equal to text after ":", ignoring whitespace
    #read line 4, set variable "instructor" equal to text after ":", ignoring whitespace
    #read line 5, set variable "title" equal to text after ":", ignoring whitespace
    #plug each variable into the output format and print
        #-or- do we want to pass the vals of the vars for later use?
    f.close()
    


main()