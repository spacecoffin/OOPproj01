# Finds the number of combinations of k different items possible within a list of n total items.
def choices(nVar, kVar):
    # 1st base case: there are no more items to find within the list of n items.
    if kVar == 0:
        return 1
    # 2nd base case: there are more items being sought than there are items in the list.
    elif kVar > nVar:
        return 0
    # Recursive case: search for k - 1 items in a list of size n - 1, add that to a search for k items in a list of size n - 1.
    else:
        return choices(nVar - 1, kVar - 1) + choices(nVar - 1, kVar)

# User is prompted for input from main() in the form of non-negative integers.
def main():
    likes = 0
    needs = 0
    while True:
        likes = int(input("Number of courses you like: "))
        if likes < 0:
            continue
        else:
            break
    while True:
        needs = int(input("Number of courses you can register for: "))
        if likes < 0:
            continue
        else:
            break
    combos = choices(likes, needs)
    print("Total number of ways of choosing {} out of {} courses: {}".format(needs, likes, combos))
    
main()