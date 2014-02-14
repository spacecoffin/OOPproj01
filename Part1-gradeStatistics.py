#CS 113 Homework Assignment 1
#Due: February 16, 2014
#Reed Rosenberg
#UPDATE TO PROPER DOCUMENTATION

def classInfo(fileIn):
    #classInfo - This function will process the first five lines of the input file that gives information about the course.
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

def gradingInfo(fileIn):
    #gradingInfo - This function should process the three lines in the input file that contain information about the numbers and weights of homeworks, quizzes, and exams.
    f = open(fileIn, 'r')
    #Begin reading at appropriate line and perform same readline & split at ':', but then take parts[1], split it again at ',' then convert the remaining parts into ints. Store the ints in a list to later be returned by the function.
    gradeInfoList = []
    x = 3
    y = 0
    while x > 0:
        line = f.readline()
        if "Homeworks" in line:
            y += 1
        if y > 0:
            parts = line.split(':', 1)
            numStr = parts[1]
            numList = numStr.split(',', 1)
            numInts = [int(i) for i in numList]
            gradeInfoList.append(numInts[0]) #I should probably add a safety check like an 'isnum' here
            gradeInfoList.append(numInts[1])
            x -= 1
    return gradeInfoList # I feel like extracting these values for use in a dictionary that would be returned would be overkill for this program.
    # Should an exception be raised if the weight of each type of work does not add up to 100?
    f.close()

def studentScores(fileIn):
    #studentScores - This function should process the remainder of the file. You may want to compute the letter grade of each student while processing the scores. This can be made as a nested function.
    f = open(fileIn, 'r')
    x = 0
    while x < 1:
        line = f.readline()
        line = line.casefold()
        if "name" and "ssn" in line:
            x += 1
            line = f.readline()
            print("Dashes: {0}".format(line))
    while line:
        line = f.readline()
        print(line)
    f.close()


def main():
    inputFile = "gradesS.in"
    classInfo(inputFile)
    gradingInfo(inputFile)
    print(gradingInfo(inputFile))
    studentScores(inputFile)

main()
