def classInfo(fileIn):
    # classInfo - This function will process the first five lines of the input file that gives information about the course.
    # fileIn should be passed the name of the file to be operated on (preceded by its path if it is not within either the current working directory or the search path)
    f = open(fileIn, 'r')
    classInfoList = []
    # UPDATE: Changed from a while loop to a for loop for readability.
    # Eliminates need for declaring 'x' variable outside of the loop's scope.
    for x in range(5):
        line = f.readline()
        parts = line.split(':', 1)
        field = parts[1] # convert to a string so that it can be stripped of leading and trailing whitespace in the line of code below
        classInfoList.append(field.strip())
    infoAsStr = "\n{0[0]}, {0[1]}\n{0[2]}\n{0[3]}\n{0[4]}\n".format(classInfoList)
    return infoAsStr
    f.close()

def gradingInfo(fileIn):
    # gradingInfo - This function should process the three lines in the input file that contain information about the numbers and weights of homeworks, quizzes, and exams.
    f = open(fileIn, 'r')
    # Begin reading at appropriate line and perform same readline & split at ':', but then take parts[1], split it again at ',' then convert the remaining parts into ints. Store the ints in a list to later be returned by the function.
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
            gradeInfoList.append(numInts[0])
            gradeInfoList.append(numInts[1])
            x -= 1
    gradeInfoDict = dict(zip(['numHws', 'weightHws', 'numQuizzes', 'weightQuizzes', 'numExams', 'weightExams'], gradeInfoList))
    return gradeInfoDict
    f.close()

def studentScores(fileIn):
    #studentScores - This function should process the remainder of the file. You may want to compute the letter grade of each student while processing the scores. This can be made as a nested function.
    openObj = open(fileIn, 'r')
    
    # This nested function identifies the line that contains the file's headers and creates a list of those headers to be used for later processing.
    def makeHeaders(openObj):
        headers = []
        x = 0
        while x < 1:
            line = openObj.readline()
            line = line.lower() # UPDATED: Changed from str.casefold() (New in Python 3.3) to str.lower() for backward compatibility.
            if "name" and "ssn" in line: # This is the line identification condition as per provided input.
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
                        headers.append(aheader)
                        aheader = ''
                    elif hchar.isnumeric():
                        i += 1
                    elif hchar.isspace():
                        i += 1
                x += 1
                line = openObj.readline() # This is to force the program to read the dashed separator line so that when information is read from the file to the io buffer again, it picks up reading again after the separator.
        return list(headers)
    
    headerList = makeHeaders(openObj)
    
    # Mass declaration of variables needed for use at many variously nested points of the function.
    achar = ' '
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
    
    # This is the main loop that scans each line of student information and properly stores and itemizes it for later processing.
    while achar:
        aname = ''
        while not achar.isnumeric():
            aname = aname + achar
            achar = openObj.read(1)
        aname = aname.strip()
        assn = ''
        y = 11
        while y > 0:
            assn = assn + achar
            achar = openObj.read(1)
            y -= 1
        aopt = ''
        while achar.isspace():
            achar = openObj.read(1)
        z = 3
        while z > 0:
            aopt = aopt + achar
            achar = openObj.read(1)
            z -= 1
        apost = ''
        if 'F' in aopt: # Only information for students who are receiving either a letter grade or a pass/fail needs to be processed. Once that field is read for a student by the above loops, the code nested within this condition can perform the necessary storage and itemization tasks.
            while achar.isspace():
                achar = openObj.read(1)
            apost = achar
            names.append(aname)
            ssns.append(assn)
            opts.append(aopt)
            posts.append(apost)
            achar = openObj.read(1)
            agrade = ''
            anumgrade = 0
            agradeList = []
            while achar != '\n': # Grades can appear from anywhere after the line's 'Post' field until the end of the line.
                achar = openObj.read(1)
                if not achar:
                    break
                if achar.isnumeric():
                    while achar.isnumeric():
                        agrade = agrade + achar
                        achar = openObj.read(1)
                    anumgrade = int(agrade)
                    agradeList.append(anumgrade)
                    agrade = ''
                elif achar.isspace():
                    continue
            
            # This nested function plugs each student's grades into the grading formula then derives and stores the appropriate letter grade.
            def gradeProcessing(agradeList):
                gradingDict = gradingInfo(fileIn)
                i = 0
                hwTotal = 0
                quizTotal = 0
                examTotal = 0
                discrepancy = len(agradeList) - (len(headerList) - 4)
                if discrepancy > 0: # This condition and its application in the while loop below account for the existence of extra grades.
                    print("\n{0} grade(s) exist for student {1} that do not have a header to specify their assignment type!\nThe first {0} grade(s) from the right hand side of the line have been ommitted.".format(discrepancy, aname))
                while (i + discrepancy) < len(agradeList):
                    field = headerList[i+4]
                    if 'hw' in field:
                        hwTotal = hwTotal + agradeList[i]
                    elif 'qz' in field: # UPDATE: Changed 'quiz' to 'qz' per input provided.
                        quizTotal = quizTotal + agradeList[i]
                    elif 'exam' in field:
                        examTotal = examTotal + agradeList[i]
                    i += 1
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
            # Prevent extra whitespace after the final line of student information from causing the program to loop.
            achar = openObj.read(1)
            while achar.isspace():
                achar = openObj.read(1)
            continue
        
        if 'UD' in aopt:
            while achar != '\n':
                achar = openObj.read(1)
            while achar.isspace():
                achar = openObj.read(1)
            continue
    
    # This loop converts letter grades to their Pass/Fail equivalent for the appropriate students.    
    for i in range(len(opts)):
        if 'P/F' in opts[i]:
            if letterGrades[i] in ('A', 'B', 'C'):
                letterGrades[i] = 'P'
            elif letterGrades[i] in ('D', 'F'):
                letterGrades[i] = 'F'
                
    return list(zip(names, ssns, opts, posts, hwGrades, quizGrades, examGrades, numGrades, letterGrades))
        # Information fields about the students should be pulled from left to right.
        # To pull the names: Read the str pulled from the io from left to right, char by char. Create a new string for the student's name. Read a char then check if it is a number. If it is not, append it to the string (to later be appended to a list of all the student's info). If it is a number, strip the string using strip(), create a new sting for the student's SSN and append it to that.
    f.close()

def stats():
    # This function should output information based on user input.
    reply = 'x'
    gradeData = studentScores(inputFile)
    
    # This nested function adds each student's total score to a list that is operated on in order to later display the highest and lowest scores for the class as well as the class average.
    def highLowAvg(gradeData):
        totalList = []
        s = 0
        while s < len(gradeData):
            totalList.append(gradeData[s][7])
            s += 1
        totalList = sorted(totalList)
        hiLoAvg = []
        hiLoAvg.extend([totalList[-1], totalList[0], sum(totalList) / len(totalList)])
        return hiLoAvg
    
    while True:
        reply = input('(S)ummarize, (F)ull Display, (R)ange, or (Q)uit: ')
        
        # Quit
        if reply == 'Q' or reply == 'q':
            break
        
        # Summarize
        elif reply == 'S' or reply == 's':
            print(classInfo(inputFile))
            print("{:<4}{:^13}{:^7}{:^15}{:^5}      {:^7}".format('Id', 'Hws', 'Quizzes', 'Exams', 'Total', 'Grade'))
            print('{:<}'.format('-' * 57))
            # while loop for printing <student grades>
            i = 0
            # loop for length of list, incrementing i each time. i is then used as an index for querying each student's information tuple from the gradeData list while the index for the needed field of student information is hardcoded.
            while i < len(gradeData):
                if 'Y' in gradeData[i][3]:
                    print("{:<4}{:^13.2f}{:^7.2f}{:^15.2f}{:^6}     {:^7}".format(gradeData[i][1][-4:], round(gradeData[i][4], 2), round(gradeData[i][5], 2), round(gradeData[i][6], 2), gradeData[i][7], gradeData[i][8]))
                i += 1
            totalStats = highLowAvg(gradeData)
            print("\n{:<38}{:>5}\n{:<38}{:>5}\n{:<38}{:>5.2f}\n".format('Highest:', totalStats[0], 'Lowest:', totalStats[1],'Average:', totalStats[2]))
            
        # Full Display
        elif reply == 'F' or reply == 'f':
            print(classInfo(inputFile))
            print("{:<19}{:^4}{:^13}{:^7}{:^15}{:^5}      {:^7}".format('Name', 'Id', 'Hws', 'Quizzes', 'Exams', 'Total', 'Grade'))
            print('{:<}'.format('-' * 76))
            # while loop for printing <student grades>
            i = 0
            # loop for length of list, incrementing i each time. i is then used as an index for querying each student's information tuple from the gradeData list while the index for the needed field of student information is hardcoded.
            while i < len(gradeData):
                if not 'AUD' in gradeData[i][2]:
                    print("{:<19}{:^4}{:^13.2f}{:^7.2f}{:^15.2f}{:^6}     {:^7}".format(gradeData[i][0], gradeData[i][1][-4:], round(gradeData[i][4], 2), round(gradeData[i][5], 2), round(gradeData[i][6], 2), gradeData[i][7], gradeData[i][8]))
                i += 1
            totalStats = highLowAvg(gradeData)
            print("\n{:<57}{:>5}\n{:<57}{:>5}\n{:<57}{:>5.2f}\n".format('Highest:', totalStats[0], 'Lowest:', totalStats[1],'Average:', totalStats[2]))
            
        # Range
        elif reply == 'R' or reply == 'r':
            while True:
                # Prompt the user for input for the range. Reprompts if the input is not in the correct format.
                try:
                    scoreRange = sorted(list(map(int, input('\nEnter the range separated by \',\': ').split(','))))
                except ValueError:
                    print("\nThe input was not in the specified format. Please try again.")
                    continue
                if len(scoreRange) != 2:
                    print("\nPlease enter 2 scores separated by a comma.")
                    continue
                
                else:
                    # Total up the number of students whose score are within the range then display that number and restate the ordered range.
                    i = 0
                    inRange = 0
                    while i < len(gradeData):
                        if gradeData[i][7] >= scoreRange[0] and gradeData[i][7] <= scoreRange[1]:
                            inRange += 1
                        i += 1
                    else:
                        print("{} student(s) have total score between {} and {}.".format(inRange, scoreRange[0], scoreRange[1]))
                    # Print the name of each student whose score is within the specified range.
                    i = 0
                    while i < len(gradeData):
                        if not 'AUD' in gradeData[i][2]:
                            if gradeData[i][7] >= scoreRange[0] and gradeData[i][7] <= scoreRange[1]:
                                print(gradeData[i][0])
                        i += 1
                    break

def main():
    global inputFile; inputFile = "grades.in"
    stats()

main()
