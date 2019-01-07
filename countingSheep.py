import time



def main():
    
    with open("sheepLarge.txt") as f:
        lines = f.read().splitlines()


    for i in range(1, len(lines)):
        
        myString = "Case #" + str(i) + ": " + countingSheeps(int(lines[i]))
        print(myString)
    

def countingSheeps(num):

    start_time = time.time()
    insomnia = False
    finalList = []
    isAll = [False, False, False, False, False, False, False, False, False, False]
    strNum = str(num)
    index = 1
    retainNum = num
    while(isAllTrue(isAll) == False):
        now = time.time()
        num = num * index
        strNum = str(num)
        finalList.append(strNum)
        for i in range(len(isAll)):
            for j in range(len(strNum)):
                if (int(strNum[j])== i):
                    isAll[i] = True
        isAllTrue(isAll)
        num = retainNum
        index = index + 1
        if now - start_time > 3:
            insomnia = True
            break
    if insomnia == True:
       return "INSOMNIA"
    else:
        #print(isAll)
        return finalList[len(finalList) - 1]



def isAllTrue(someList):
    for i in range(len(someList)):
        if someList[i] == False:
            return False
    return True
    


if __name__ == "__main__":
    main()