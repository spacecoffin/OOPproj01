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
    infoAsStr = "{0[0]}, {0[1]}\n{0[2]}\n{0[3]}\n{0[4]}\n".format(classInfoList)
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

    def makeHeaders(openObj):
        headers = []
        x = 0
        while x < 1:
            line = openObj.readline()
            line = line.lower() # UPDATED: Changed from str.casefold() (New in Python 3.3) to str.lower() for backward compatibility.
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
        print("We're at the top")
        print("\"{}\"".format(achar))
        try:
            achar = openObj.read(1)
        except EOFError:
            print("EOF in main while 1")
            continue
        else:
            if achar.isspace():
                try:
                    achar = openObj.read(1)
                except EOFError:
                    print("EOF in space killer")
                    continue
        aname = ''
        print("\"{}\": Right above previous error".format(achar))
        while not achar.isnumeric():
            aname = aname + achar
            try:
                achar = openObj.read(1)
            except EOFError:
                print("EOF in aname")
                break
        aname = aname.strip()
        print(aname)
        assn = ''
        y = 11
        while y > 0:
            assn = assn + achar
            achar = openObj.read(1)
            y -= 1
        print(assn)
        aopt = ''
        while achar.isspace():
            achar = openObj.read(1)
        z = 3
        while z > 0:
            aopt = aopt + achar
            achar = openObj.read(1)
            z -= 1
        print(aopt)
        apost = ''
        if 'F' in aopt:
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
            while achar != '\n':
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
            def gradeProcessing(agradeList):
                gradingDict = gradingInfo(fileIn)
                i = 0
                hwTotal = 0
                quizTotal = 0
                examTotal = 0
                print("{} in grading".format(aname))
                while i < len(agradeList):
                    field = headerList[i+4]
                    if 'hw' in field:
                        hwTotal = hwTotal + agradeList[i]
                    elif 'qz' in field:
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
        if 'UD' in aopt:
            while achar != '\n':
                achar = openObj.read(1)
            print("{} ain't being graded".format(aname))
            continue
    print("We're about to PassFail")
    print(list(opts))
    for i in range(len(opts)):
        print("We're PassFailing")
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
    def highLowAvg(gradeData):
        totalList = []
        s = 0
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
            print("\n{:<38}{:>5}\n{:<38}{:>5}\n{:<38}{:>5.2f}".format('Highest:', totalStats[0], 'Lowest:', totalStats[1],'Average:', totalStats[2]))
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
            print("\n{:<57}{:>5}\n{:<57}{:>5}\n{:<57}{:>5.2f}".format('Highest:', totalStats[0], 'Lowest:', totalStats[1],'Average:', totalStats[2]))
        elif reply == 'R' or reply == 'r':
            while True:
                scoreRange = sorted(list(map(int, input('Enter the range separated by \',\': ').split(','))))
                if len(scoreRange) != 2:
                    continue
                else:
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
