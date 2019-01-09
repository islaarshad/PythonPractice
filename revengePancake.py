

#https://code.google.com/codejam/contest/6254486/dashboard#s=p1
def main():
    
    with open("largeRevengePancakes.txt") as f:

        lines = f.read().splitlines()



    lineNum = lines[0]

    for i in range(1, int(lineNum) +  1):
        myString = "Case #" + str(i) +": " + str(stringProcess(lines[i]))
        print(myString)




def stringProcess(processString):
    isPlus = False
    stringList = list(processString)
    flipCounter = 0
    index = 0
    while(checkPluses(stringList) == False):
        if stringList[0] == "+":
            isPlus = True
        else:
            isPlus = False
        if isPlus:
            while index < len(stringList) and stringList[index] != "-":
                stringList[index] = "-"
                index = index + 1
            flipCounter = flipCounter + 1
        else:
            while index < len(stringList) and stringList[index] != "+":
                stringList[index] = "+"
                index = index + 1
            flipCounter = flipCounter + 1
        index = 0
    return flipCounter


def checkPluses(stringList):
    if "-" in stringList:
        return False
    return True


if __name__ == "__main__":
    main()