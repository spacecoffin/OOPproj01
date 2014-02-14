#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION

#classInfo - This function will process the first five lines of the input file that gives information about the course.

def classInfo(fileIn):
    #fileIn should be passed the name of the file to be operated on (preceded by its path if it is not within either the current working directory or the search path)
    f = open(fileIn, 'r')
    classInfoList = []
    x = 5
    while x > 0:
        line = f.readline()
        parts = line.split(':', 1)
        field = parts[1] # convert to a string so that it can be stripped of leading and trailing whitespace in the line of code below
        classInfoList.append(field.strip())
        x -= 1
    infoAsStr = "{0[0]}, {0[1]}\n{0[2]}\n{0[3]}\n{0[4]}\n".format(classInfoList)
    print(infoAsStr)
    f.close()

#gradingInfo - This function should process the three lines in the input file that contain information about the numbers and weights of homeworks, quizzes, and exams.

def gradingInfo(fileIn):
    f = open(fileIn, 'r')
    #Begin reading at appropriate line and perform same readline & split at ':', but then take parts[1], split it again at ',' then convert the remaining parts into ints. Store the ints in a list to later be returned by the function.
    gradeInfoList = []
    l = 0
    n = 0
    while l < 1:
        line = f.readline()
        if "Homeworks" in line:
            l += 1
        else:
            n += 1
    x = 3
    while x > 0:
        line = f.readline(n)
        parts = line.split(':', 1)
        numStr = parts[1]
        numList = numStr.split(',', 1)
        gradeInfoList.append(int(i) for i in numList) #I should probably add a safety check like an 'isnum' here
        x -= 1
        n += 1
    print(gradeInfoList)
    f.close()

def main():
    inputFile = "gradesS.in"
    classInfo(inputFile)
    gradingInfo(inputFile)

main()
