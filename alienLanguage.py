

#Subtract approprite j from the len(sourceWord) until the final len(sourceWord) is 5 which is not equal to len(target) meaning they are not the same

def main():


    with open("large_practice.txt") as f:
        lines = f.read().splitlines()

    a, b ,c = lines[0].split(' ')
    
    #print(a)
    #print(b) #number of target words
    #print(c) # number of sourcewords

    int_a = int(a)
    int_b = int(b)
    int_c = int(c)


    targetDic = []
    sourceWordDic = []

    lineCounter = 1
    for lineNum in range(int_b):
        targetDic.append(lines[lineNum + 1])
        lineCounter = lineCounter + 1
        
    #print("TARGET DIC ", targetDic)
    #print("LineCounter ", lineCounter)

    for i in range(int_c):
        sourceWordDic.append(lines[lineCounter + i])
    
    #print("SourceWordDic ", sourceWordDic)

    myCounter = 0
    my_dic = {}

    for s in range(len(sourceWordDic)):
        for t in range(len(targetDic)):
            if (inChecker(targetDic[t], sourceWordDic[s]) == True):
                myCounter = myCounter + 1
            my_dic[s + 1] = myCounter
        myCounter = 0
    #print("MY_DICT ", my_dic)
            

    for key, value in my_dic.items():
        print("Case #",key, ": ", value, sep = '')


    #target = "acea" 
    #sourceWord = "(abc)(bcd)(cde)a" 
    #print(inChecker(target, sourceWord))

def inChecker(target, sourceWord):
    i = 0
    j = 0
    targetLength = len(target)
    #print(targetLength)
    myCount = 0
    hasFound = False
    sourceCounter = len(sourceWord)
    
    
    while i < len(sourceWord):
        
        if sourceWord[i] != "(":
           # print("SOURCE WORD OUTSIDE: ", sourceWord[i])
            if myCount < len(target) and target[myCount] == sourceWord[i]:
                #print("TARGET AT MYCOUNT O ", target[myCount])
                myCount = myCount + 1
            j = j + 1
            
        else:
            sourceCounter = sourceCounter - 1
            j = j + 1
            while sourceWord[j] != ")":
                #print("SOURCE WORD INSIDE: ", sourceWord[j])
                sourceCounter = sourceCounter - 1
                #print("TARGET AT MYCOUNT I", target[myCount])
                if myCount < len(target) and hasFound == False and target[myCount] == sourceWord[j]:
                    myCount = myCount + 1
                    hasFound = True
                j = j + 1
            
            #if hasFound == False:
                #myCount = -1
                #break
            hasFound = False
            j = j + 1
            
        i = j
        

    #print("Source Counter ", sourceCounter)
    #print("MyCount ", myCount)
    #print(myCount)
    #print(targetLength)
    if myCount == sourceCounter and myCount == targetLength:
        #print(target, " is in the ", sourceWord)
        return True
    
        #print(target, "is not in the", sourceWord)
        
    return False

    
            

if __name__ == "__main__":
    main()