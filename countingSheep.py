import time


#Problem URL: https://code.google.com/codejam/contest/6254486/dashboard
def main():
    #Read in the lines of input file
    with open("sheepLarge.txt") as f:
        lines = f.read().splitlines()

    #Go in for the number of lines
    for i in range(1, len(lines)):
        #Print the right way on console
        myString = "Case #" + str(i) + ": " + countingSheeps(int(lines[i]))
        print(myString)
    
#This function takes in the number that is later maniplated to contain all numbers from 0 to 9 (as it is multiplyied by incrementing numbers)
#If so, the function returns the last number when all numbers from 0 to 9 were included, else it
#return INSOMNIA!
def countingSheeps(num):
    #This was a little hack I developed, instead of making a function go on forever, I timed it strategically so that I can determine if it goes on forever or not
    start_time = time.time()
    insomnia = False
    #This list is used to report the last number that was parsed to fulfil the presense of the numbers 0 to 9
    finalList = []
    #This list which determines if all the numbers from 0 to 9 are present or not
    isAll = [False, False, False, False, False, False, False, False, False, False]
    strNum = str(num)
    index = 1
    retainNum = num
    #Run the while loop until all the values in isAll are True
    while(isAllTrue(isAll) == False):
        #Start the time
        now = time.time()
        #Mulitply the number subsequently by the incrementing index variable
        num = num * index
        strNum = str(num)
        finalList.append(strNum)
        #This loop oes through all the indexes of isAll[] (which has index 0 to 9) and it checks if the strNum string has any number == index of isAll[], if yes,
        #that index in isAll[] is set to true
        for i in range(len(isAll)):
            for j in range(len(strNum)):
                if (int(strNum[j])== i):
                    isAll[i] = True
        #we check if isAll is true, if yes, this will be the last iteration of this while loop
        isAllTrue(isAll)
        num = retainNum
        #Increment the index
        index = index + 1
        #Now we check if the loop has been going on for a certain period of time, if yes, we set insomnia boolean to True and get out of the loop
        if now - start_time > 3:
            insomnia = True
            break
    if insomnia == True:
       return "INSOMNIA"
    else:
        #Else, we print the last number in finaList[]
        return finalList[len(finalList) - 1]


#This function returns true of all values in a list passed are True, else it returns false
def isAllTrue(someList):
    for i in range(len(someList)):
        if someList[i] == False:
            return False
    return True
    


if __name__ == "__main__":
    main()