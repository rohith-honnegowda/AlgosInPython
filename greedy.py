gasStations = [0, 250, 375, 550, 750, 950, 1250, 1375, 1500]
maxDistance = 600
currentRefill = 0
numOfRefills = 0
maxRefills = len(gasStations) - 1
lastRefill = currentRefill
while currentRefill <= maxRefills:
        lastRefill = currentRefill
        if currentRefill == maxRefills:
                print("Value of CUrrent refill %d"% currentRefill)
                print("Last refills was at: %d"% lastRefill)
                print("===================================================")
                break
        while (currentRefill < maxRefills) and ((gasStations[currentRefill + 1] - gasStations[lastRefill]) <= maxDistance):
                print("===================================================")
                print("Current gas station: %d"% gasStations[currentRefill])
                print("number of refills: %d"% numOfRefills)
                print("Last refills was at: %d"% gasStations[lastRefill])
                print("===================================================")
                
                currentRefill = currentRefill + 1
        if currentRefill == lastRefill:	
            break
        if currentRefill < maxRefills:
            numOfRefills = numOfRefills + 1
	
print("The min number of refills possible is: %d"% numOfRefills)	