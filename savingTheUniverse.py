#https://code.google.com/codejam/contest/32013/dashboard
def main():
    searchEngine = ['Yeehaw', 'NSM', 'Dont Ask', 'B9', 'Googol']
    queries = ['Yeehaw', 'Yeehaw', 'Googol', 'B9', 'Googol', 'NSM', 'B9', 'NSM', 'Dont Ask', 'Googol']
    #print(findPartArr(searchEngine, queries))

    lastIndex = findLastIndex(searchEngine, queries)
    
    #print(lastIndex)
    arrIndex = 0
    changeArr = []
    i = 0
    switch = 0
    alterArr = queries
    while i < len(alterArr):

        changeArr = alterArr[i:]
        print(changeArr)
        
        if findLastIndex(searchEngine, changeArr) is None:
            return
        i = i + findLastIndex(searchEngine, changeArr)
        print(i)
        while i < findLastIndex(searchEngine, changeArr):
            i = i + 1
        switch = switch + 1
        print(i)
        print("SWITCH " + str(switch))
        

    
        




def findLastLetter(arr):
    return arr[len(arr) - 1]


# Check if there is no variable (where we auto return 0)
def findLastIndex(searchEngine, queries):
    #go until all the values in the search engines are encountered at atleast once in the queries array
    
    engineLen = len(searchEngine)
    hits = 0
    saveArr = []
    for i in range(len(queries)):
        for j in range(len(searchEngine)):
            if queries[i] == searchEngine[j]:
                saveArr.append(queries[i])
                #print(queries[i] + " have " + str(saveArr.count(queries[i])) + " occurances")
                if saveArr.count(queries[i]) == 1:
                    hits = hits + 1
                    if hits == engineLen:
                        return len(saveArr) - 1
                



if __name__ == "__main__":
    main()

