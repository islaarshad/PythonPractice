

#https://code.google.com/codejam/contest/6254486/dashboard#s=p1
def main():
   #Read an input file
    with open("largeRevengePancakes.txt") as f:
        lines = f.read().splitlines()


	#Number of line to read
    lineNum = lines[0]
	#Read in the strings and return the number of flips required to make the string all
	#'+' and output in the format below
    for i in range(1, int(lineNum) +  1):
        myString = "Case #" + str(i) +": " + str(stringProcess(lines[i]))
        print(myString)



#This function takes in a string of order '+' and '-' and returns the 
#lowest number of flips it would take a subsequent list of '+' and '-' to become
#all '+'
def stringProcess(processString):
	#Boolean to check if the entire string is all '+'
    isPlus = False
	#Convert the string to a list since we want the contents mutated
    stringList = list(processString)
    flipCounter = 0
    index = 0
	#This while loop runs until all contents of the list are '+'
    while(checkPluses(stringList) == False):
	#Change the value of the boolean declared above based on the first element in the list
        if stringList[0] == "+":
            isPlus = True
        else:
            isPlus = False
		#If the starting element is '+', flip everthing until a '-' occurs
        if isPlus:
            while index < len(stringList) and stringList[index] != "-":
                stringList[index] = "-"
                index = index + 1
			#This equals one flip
            flipCounter = flipCounter + 1
		#If the starting element is '-', flip everthing until a '+' occurs
        else:
            while index < len(stringList) and stringList[index] != "+":
                stringList[index] = "+"
                index = index + 1
			#This equals one flip
            flipCounter = flipCounter + 1
		#Set the index o the starting position
        index = 0
	#Return the number of flips
    return flipCounter

#This function checks if a string list has a '-' in it or not
def checkPluses(stringList):
    if "-" in stringList:
        return False
    return True


if __name__ == "__main__":
    main()