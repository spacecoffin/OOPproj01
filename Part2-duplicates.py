# Read each line in the input file and write each one to consecutive indexes in an array/list.
# Input is the name (and path, if needed) of the file to be read.
def importer(fileIn):
    nameArray = []
    for line in open(fileIn):
        nameArray.append(line.strip())
    return nameArray

# Check to see if there are any duplicate items in the array created from the input file.
# Returns 'true' if there are duplicates and 'false' if there are not.
def duplicates(nameArray):
    # 1st base case: There are one or fewer items in the array.
    if len(nameArray) <= 1:
        return False
    # 2nd base case: The first item in the array appears elsewhere in the array.
    if nameArray[0] in nameArray[1:]:
        return True
    # Recursion case: Check the base cases against an the same array, excluding the first item.
    else:
        return duplicates(nameArray[1:])

def main():
    arrayFromFile = importer("names.dat")
    if duplicates(arrayFromFile):
        print('There are duplicate names.')
    else:
        print('There are NO duplicate names.')

main()