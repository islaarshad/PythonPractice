import math


#Bullseye
def main():
        myPie = 3.14
        with open("bullseyeSmallInput.txt") as f:
                lines = f.read().splitlines()

        for i in range(1, len(lines)):
                myRad, myPaint = map(int, lines[i].split(" "))
                paint = myPaint * myPie
                print("Case #" + str(i) + ": " + str(howManyCircles(myRad, paint, myPie)))





def howManyCircles(radius, paint, myPie):

        #print("Original Paint ", paint)
        #print("Original Radius ", radius)
        isBlack = False
        myBlackCounter = 1
        while paint > 0:
                if isBlack == False:
                        next_white = myPie * radius * radius
                        #print("WHITE ", next_white, " with Radius ", radius)
                        isBlack = True
                else:
                        #print("COUNTER ", myBlackCounter)
                        next_black = myPie * radius * radius
                        #print("-----------------------")
                        #print("BLACK ", next_black, " with Radius ", radius)
                        black_ring = round(next_black - next_white)
                        #print("BLACK RING " + str(black_ring) + " BY " + str(next_black) + " - " + str(next_white))
                        temppaint = paint
                        paint = paint - black_ring
                        #print("Paint " + str(paint) + " = " + str(temppaint) + " - " + str(black_ring))
                        #print("-----------------------")

                        if (paint < 0):
                                return myBlackCounter - 1
                        elif (paint == 0):
                                return myBlackCounter
                        else:
                                myBlackCounter = myBlackCounter + 1
                        isBlack = False
                radius = radius  + 1
        #print(myBlackCounter)


        










if __name__ == "__main__":
    main()