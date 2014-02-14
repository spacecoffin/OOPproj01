#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION

#classInfo - This function will process the first five lines of the input file that gives information about the course.

def classInfo(fileIn):
    #fileIn should be passed the name of the file to be operated on (preceded by its path if it is not within either the current working directory or the search path)
    f = open(fileIn, 'r')
    infoList = []
    x = 5
    while x > 0:
        line = f.readline()
        parts = line.split(':', 1)
        field = parts[1] # convert to a string so that it can be stripped of leading and trailing whitespace in the line of code below
        infoList.append(field.strip())
        x -= 1
    infoAsStr = "{0[0]}, {0[1]}\n{0[2]}\n{0[3]}\n{0[4]}\n".format(infoList)
    print(infoAsStr)
    f.close()

#gradingInfo - This function should process the three lines in the input file that contain information about the numbers and weights of homeworks, quizzes, and exams.
#You can assume the following. Every class will have at least one homework and one exam. A class may or may not have a quiz. Each homework carries the same weight and so does each quiz (if there is one) and each exam. The weightage of homeworks, quizzes, and exams add up to 100.

def gradingInfo(fileIn):
    f = open(fileIn, 'r')
    f.close()

def main():
    inputFile = "gradesS.in"
    classInfo(inputFile)
    gradingInfo(inputFile)

main()
