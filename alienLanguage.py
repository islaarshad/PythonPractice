

#Problem URL: https://code.google.com/codejam/contest/90101/dashboard
def main():

    #Open a file to read
    with open("largeInputAlienLanguage.txt") as f:
        lines = f.read().splitlines()

    #extract how many lines of input to read from
    a, b ,c = lines[0].split(' ')

    int_a = int(a)
    int_b = int(b)
    int_c = int(c)

    #Declare a dictionary, ine for the source words taken and one for the final output
    targetDic = []
    sourceWordDic = []
    #read the words to be checked the language against
    lineCounter = 1
    for lineNum in range(int_b):
        targetDic.append(lines[lineNum + 1])
        lineCounter = lineCounter + 1
        
    #Read the alien language syntax
    for i in range(int_c):
        sourceWordDic.append(lines[lineCounter + i])
    
    myCounter = 0
    my_dic = {}
    #Go through both the appended dictionaries check if there is a match, if it is, increment a counter
    for s in range(len(sourceWordDic)):
        for t in range(len(targetDic)):
            if (inChecker(targetDic[t], sourceWordDic[s]) == True):
                myCounter = myCounter + 1
            my_dic[s + 1] = myCounter
        myCounter = 0

            
    #Print the final dictionary items and their counts
    for key, value in my_dic.items():
        print("Case #",key, ": ", value, sep = '')

#This function checks whether a target word is equivalent to the source word (alien syntax)
def inChecker(target, sourceWord):
    i = 0
    j = 0
    #Declaring the lenght of the target word
    targetLength = len(target)
    myCount = 0
    hasFound = False
    #Declaring the length of the source word as source indexing later on
    sourceCounter = len(sourceWord)
    
    #Go through the source word and check if there is a "(" present
    while i < len(sourceWord):
        if sourceWord[i] != "(":
            #If the word at the index is within the target and source word, increment the count
            if myCount < len(target) and target[myCount] == sourceWord[i]:
                myCount = myCount + 1
            #Keep in track of the seperate count to see if "(" was present
            j = j + 1
        #If "(" was not present at all
        else:
            sourceCounter = sourceCounter - 1
            j = j + 1
            #Check if the ")" was present
            while sourceWord[j] != ")":
                sourceCounter = sourceCounter - 1
                #Check to see that if the target word is not found if the index of the target word and source word is the same
                if myCount < len(target) and hasFound == False and target[myCount] == sourceWord[j]:
                    myCount = myCount + 1
                    #The word has been found
                    hasFound = True
                #increment the instance of find ")"
                j = j + 1
            #Once outside of ")", set hasFound to False
            hasFound = False
            #increment the instance of find ")"
            j = j + 1
        #Critical, make sure that j become i because we want increment i more than once!
        i = j
        
    #Check to see if myCount was the index length of source word and myCount was equal to target length
    #Better would have been sourceCounter == targetLength, but this works
    if myCount == sourceCounter and myCount == targetLength:
        return True
    return False

    
            

if __name__ == "__main__":
    main()