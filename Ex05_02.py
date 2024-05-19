import numpy as np
import math

transitionMatrix = [
    [0.5, 0.3, 0.2],
    [0.2, 0.5, 0.3],
    [0.4, 0.2, 0.4]
]

outputMatrix = [
    [0.7, 0.2, 0.1],
    [0.6, 0.3, 0.1],
    [0.1, 0.1, 0.8],
]


def change_letter_to_index(game_char):
    if game_char == 'B':
        return 0
    elif game_char == 'S':
        return 1
    else:
        return 2


def change_index_to_letter(weather_index):
    if weather_index == 0:
        return 'C'
    elif weather_index == 1:
        return 'P'
    else:
        return 'H'


vArr = np.empty((200, 3))
pArr = np.empty((200, 3), dtype=int)
hArr = np.empty(200, dtype=int)
for i in range(200):
    hArr[i] = 0


with open('GAME_OUT', 'r') as gameFile:
    gameOutput = gameFile.read()

x0 = change_letter_to_index(gameOutput[0])

for weather in range(3):
    vArr[0][weather] = outputMatrix[weather][x0]*float(1/3)

for i in range(1, 200):
    xi = change_letter_to_index(gameOutput[i])
    for weather in range(3):
        uMax = vArr[i - 1][0] + math.log(transitionMatrix[0][weather])
        index = 0
        for j in range(1, 3):
            u = vArr[i-1][j] + math.log(transitionMatrix[j][weather])
            if u > uMax:
                index = j
                uMax = u
        vArr[i][weather] = math.log(outputMatrix[weather][xi]) + uMax
        pArr[i][weather] = index

hmmFile = open("HMM_OUT", "w")
hArr[199] = np.argmax([pArr[199][0], pArr[199][1], pArr[199][2]])
for i in range(198, -1, -1):
    hArr[i] = pArr[i+1][hArr[i+1]]
for i in range(200):
    hmmFile.write(change_index_to_letter(hArr[i]))

hmmFile.close()
