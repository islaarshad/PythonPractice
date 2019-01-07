

def main():
        with open("senateText.txt") as f:
                lines = f.read().splitlines()

        newList = []
        for i in range(1, len(lines)):
                newList.append(lines[i])

        j = 0
        N = 2
        subList = [newList[n:n+N] for n in range(0, len(newList), N)]

        myString = ""
        for m in range(len(subList)):
                stringList = subList[m][1].split()
                stringList = list(map(int, stringList))
                myString = myString +  "Case #" + str(m + 1) + ": "+ " ".join(printPartyNames(int(subList[m][0]), stringList)) + "\n"
                print(myString)
                

        with open('outputFileLargeSenateEvacuation.txt', 'w') as f:
                print(myString, file = f)
       



       



def printPartyNames(num, senators):
        partyDic = dict()
        #tempDic = dict()
        isFound = False
        myList = []
        for i in range(num):
                partyString = "".join(getLetters(i))
                partyDic[partyString] = senators[i]

        i = 0
        j = 0
        while isFound == False:
                for i in partyDic:
                        j = i
                        for j in partyDic:
                                #print("TEMP DIC ", tempDic)
                                #print(i, ", ", j)
                                partyDic[i] = partyDic[i] - 1
                                partyDic[j] = partyDic[j] - 1
                                if (instanceChecker(partyDic) == 0):
                                        #print("AFTER ", partyDic)
                                        #save that instance
                                        #tempDic = partyDic
                                        theString = i + j
                                        myList.append(theString)
                                elif (instanceChecker(partyDic) == 1):
                                        partyDic[i] = partyDic[i] + 1
                                        partyDic[j] = partyDic[j] + 1
                                        #print("IF NOT CHANGED ", partyDic)
                                        #tempDic = partyDic
                                elif (instanceChecker(partyDic) == -1):
                                        theString = i + j
                                        myList.append(theString)
                                        isFound = True
                for t in partyDic:
                        #print("TEMP DIC ", tempDic)
                        #print(t)
                        partyDic[t] = partyDic[t] - 1
                        if (instanceChecker(partyDic) == 0):
                                #print("AFTER ", partyDic)
                                #tempDic = partyDic
                                myList.append(t)
                                #tempDic = partyDic
                        elif (instanceChecker(partyDic) == 1):
                                partyDic[t] = partyDic[t] + 1
                                #print("IF NOT CHANGED ", partyDic)
                                #tempDic = partyDic
                        elif (instanceChecker(partyDic) == -1):
                                myList.append(t)
                                isFound = True
        return myList
        
        


def instanceChecker(someDic): #error right here
        sum = 0
        for i in someDic:
                if (someDic[i] < 0):
                        return 1
                sum = sum + someDic[i]
        #print("SUM ", sum)    
        if sum == 0:
                return -1
        
        #print("SOME DIC ", someDic)
        for k in someDic:
                if someDic[k] / sum > .50:
                        #print("MY K ", someDic[k])
                        return 1
        return 0




def getLetters(myIndex):
    for i in range(65, 65 + 26):
        if myIndex + 65 == i:
            return chr(i)
       



















            

if __name__ == "__main__":
    main()