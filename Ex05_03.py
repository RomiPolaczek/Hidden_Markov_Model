weatherFile = open("WEATHER_OUT", "r")
hmmFile = open("HMM_OUT", "r")

weatherOutput = weatherFile.read()
hmmOutput = hmmFile.read()

truePositive = 0
falsePositive = 0
trueNegative = 0
falseNegative = 0

for i in range(200):
    if weatherOutput[i] == 'H':
        if hmmOutput[i] == 'H':
            truePositive += 1
        elif hmmOutput[i] != 'H':
            falseNegative += 1
    if weatherOutput[i] != 'H':
        if hmmOutput[i] == 'H':
            falsePositive += 1
        elif hmmOutput[i] != 'H':
            trueNegative += 1

print("The number of True Positive is: ", truePositive)
print("The number of False Positive is: ", falsePositive)
print("The number of True Negative is: ", trueNegative)
print("The number of False Negative is: ", falseNegative)

weatherFile.close()
hmmFile.close()
