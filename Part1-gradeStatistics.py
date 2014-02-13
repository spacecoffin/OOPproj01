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
    #read line 1, set variable "course" equal to text after ":", ignoring whitespace
        #to do this: readline 1 as a str, then have it read by char up to the ':'
    line = f.readline()
    parts = line.split(':', 1)
    course = parts[1]
    print(course.strip())
    #read line 2, set variable "semester" equal to text after ":", ignoring whitespace
    line = f.readline()
    parts = line.split(':', 1)
    semester = parts[1]
    print(semester.strip())
    #read line 3, set variable "university" equal to text after ":", ignoring whitespace
    line = f.readline()
    parts = line.split(':', 1)
    university = parts[1]
    print(university.strip())
    #read line 4, set variable "instructor" equal to text after ":", ignoring whitespace
    line = f.readline()
    parts = line.split(':', 1)
    instructor = parts[1]
    print(instructor.strip())
    #read line 5, set variable "title" equal to text after ":", ignoring whitespace
    line = f.readline()
    parts = line.split(':', 1)
    title = parts[1]
    print(title.strip())
    #plug each variable into the output format and print
        #-or- do we want to pass the vals of the vars for later use?
    f.close()
    
def main():
    classInfo("gradesS.in")

main()
