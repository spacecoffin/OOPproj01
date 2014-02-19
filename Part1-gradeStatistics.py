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
    return infoAsStr
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
    gradeInfoDict = dict(zip(['numHws', 'weightHws', 'numQuizzes', 'weightQuizzes', 'numExams', 'weightExams'], gradeInfoList))
    return gradeInfoDict
    # Should an exception be raised if the weight of each type of work does not add up to 100?
    f.close()

def studentScores(fileIn):
    #studentScores - This function should process the remainder of the file. You may want to compute the letter grade of each student while processing the scores. This can be made as a nested function.
    f = open(fileIn, 'r')
    headerList = []
    x = 0
    while x < 1:
        line = f.readline()
        line = line.casefold()
        if "name" and "ssn" in line:
            i = 0
            hchar = line[i]
            aheader = ''
            while i < len(line):
                hchar = line[i]
                if hchar.isalpha():
                    while hchar.isalpha():
                        aheader = aheader + hchar
                        i += 1
                        hchar = line[i]
                    headerList.append(aheader)
                    aheader = ''
                elif hchar.isnumeric():
                    i += 1
                elif hchar.isspace():
                    i += 1
            x += 1
            line = f.readline()
    achar = 'a'
    names = []
    ssns = []
    opts = []
    posts = []
    gradesList = []
    hwGrades = []
    quizGrades = []
    examGrades = []
    numGrades = []
    letterGrades = []
    while achar:
        achar = ''
        aname = ''
        while not achar.isnumeric():
            aname = aname + achar
            achar = f.read(1)
        aname = aname.strip()
        names.append(aname)
        assn = ''
        y = 11
        while y > 0:
            assn = assn + achar
            achar = f.read(1)
            y -= 1
        ssns.append(assn)
        aopt = ''
        while achar.isspace():
            achar = f.read(1)
        z = 3
        while z > 0:
            aopt = aopt + achar
            achar = f.read(1)
            z -= 1
        opts.append(aopt)
        apost = ''
        if 'F' in aopt:
            while achar.isspace():
                achar = f.read(1)
            apost = achar
            posts.append(apost)
        if 'UD' in aopt:
            apost = 'N'
            posts.append(apost)
        achar = f.read(1)
        agrade = ''
        anumgrade = 0
        agradeList = []
        while achar is not '\n':
            achar = f.read(1)
            if not achar:
                break
            if achar.isnumeric():
                while achar.isnumeric():
                    agrade = agrade + achar
                    achar = f.read(1)
                anumgrade = int(agrade)
                agradeList.append(anumgrade)
                agrade = ''
            elif achar.isspace():
                continue
        def gradeProcessing(agradeList):
        # Add check that numX of assignment type X from gradingInfo matches the number of headers for that type of assignment.
            gradingDict = gradingInfo(fileIn)
            i = 0
            hwTotal = 0
            quizTotal = 0
            examTotal = 0
            while i < len(agradeList):
                field = headerList[i+4]
                if 'hw' in field:
                    hwTotal = hwTotal + agradeList[i]
                elif 'quiz' in field:
                    quizTotal = quizTotal + agradeList[i]
                elif 'exam' in field:
                    examTotal = examTotal + agradeList[i]
                i += 1
            # THE ROUNDING SHOULD BE MOVED TO THE STATS FUNCTION WHERE THE NUMBERS ARE PRINTED
            hwGrade = (hwTotal / gradingDict['numHws']) * (gradingDict['weightHws'] * 0.01)
            examGrade = (examTotal / gradingDict['numExams']) * (gradingDict['weightExams'] * 0.01)
            if gradingDict['numQuizzes'] < 1:
                numGrade = round(hwGrade + examGrade)
                quizGrade = -1
            else:
                quizGrade = (quizTotal / gradingDict['numQuizzes']) * (gradingDict['weightQuizzes'] * 0.01)
                numGrade = round(hwGrade + examGrade + quizGrade)
            if numGrade >= 90:
                letterGrade = 'A'
            elif numGrade >= 80:
                letterGrade = 'B'
            elif numGrade >= 70:
                letterGrade = 'C'
            elif numGrade >= 60:
                letterGrade = 'D'
            else:
                letterGrade = 'F'
            return list([hwGrade, quizGrade, examGrade, numGrade, letterGrade])
        gradesList = gradeProcessing(agradeList)
        hwGrades.append(gradesList[0])
        quizGrades.append(gradesList[1])
        examGrades.append(gradesList[2])
        numGrades.append(gradesList[3])
        letterGrades.append(gradesList[4])
    o = 0
    while o < len(opts):
        if 'P/F' in opts[o]: # keep having trouble with these string equivalences
            if letterGrades[o] in ('A', 'B', 'C'):
                letterGrades[o] = 'P'
            elif letterGrades[o] in ('D', 'F'):
                letterGrades[o] = 'F'
            # else: throw exception?
        o += 1
    return list(zip(names, ssns, opts, posts, hwGrades, quizGrades, examGrades, numGrades, letterGrades))
        # Information fields about the students should be pulled from left to right.
        # To pull the names: Read the str pulled from the io from left to right, char by char. Create a new string for the student's name. Read a char then check if it is a number. If it is not, append it to the string (to later be appended to a list of all the student's info). If it is a number, strip the string using strip(), create a new sting for the student's SSN and append it to that.
    f.close()

def stats():
    #This function should output information based on user input. You may want to have nested functions that are invoked for different user inputs.
    reply = 'x'
    gradeData = studentScores(inputFile)
    def highLowAvg(gradeData):
        s = 0
        totalList = []
        while s < len(gradeData):
            if 'AUD' not in gradeData[s][2]:
                totalList.append(gradeData[s][7])
            s += 1
        totalList = sorted(totalList)
        hiLoAvg = []
        hiLoAvg.extend([totalList[-1], totalList[0], sum(totalList) / len(totalList)])
        return hiLoAvg
    while reply:
        reply = input('(S)ummarize, (F)ull Display, (R)ange, or (Q)uit: ')
        if reply == 'Q' or reply == 'q':
            break
        elif reply == 'S' or reply == 's':
            print(classInfo(inputFile))
            headers = 'Id\tHws\tQuizzes\tExams\tTotal\tGrade'
            print(headers)
            dashes = ''
            i = 45 # temporary solution for appropriate length of dash line, accounting for each field delimited by a tab as 8 spaces and adding 5 more for each char in 'Grade'.
            while i > 0:
                dashes = dashes + '-'
                i -= 1
            print(dashes)
            # while loop for printing <student grades>
            i = 0
            # loop for length of list, incrementing i each time. i is then used as an index for querying each student's information tuple from the gradeData list while the index for the needed field of student information is hardcoded.
            while i < len(gradeData):
                if 'Y' in gradeData[i][3]:
                    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4}\t{5}".format(gradeData[i][1][-4:], round(gradeData[i][4], 2), round(gradeData[i][5], 2), round(gradeData[i][6], 2), gradeData[i][7], gradeData[i][8]))
                i += 1
            totalStats = highLowAvg(gradeData)
            print("Highest:\t\t\t{}\nLowest:\t\t\t\t{}\nAverage:\t\t\t{:>.2f}".format(totalStats[0], totalStats[1], totalStats[2]))
                  
def main():
    global inputFile; inputFile = "gradesS.in"
    classInfo(inputFile)
    gradingInfo(inputFile)
    print(studentScores(inputFile))
    stats()

main()
