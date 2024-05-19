import random

weather = ['C', 'P', 'H']
games = ['B', 'S', 'C']

firstDayWeather = random.randint(0, 2)

weatherFile = open("WEATHER_OUT", "w")
gameFile = open("GAME_OUT", "w")

currWeather = weather[firstDayWeather]
weatherFile.write(currWeather)

gameProb = random.uniform(0, 1)

if currWeather == 'C':
    if gameProb <= 0.7:
        currGame = 'B'
    elif 0.7 < gameProb <= 0.9:
        currGame = 'S'
    else:
        currGame = 'C'

if currWeather == 'P':
    if gameProb <= 0.6:
        currGame = 'B'
    elif 0.6 < gameProb <= 0.9:
        currGame = 'S'
    else:
        currGame = 'C'

if currWeather == 'H':
    if gameProb <= 0.1:
        currGame = 'B'
    elif 0.1 < gameProb <= 0.2:
        currGame = 'S'
    else:
        currGame = 'C'

gameFile.write(currGame)

for i in range(199):
    weatherProb = random.uniform(0, 1)
    gameProb = random.uniform(0, 1)

    if currWeather == 'C':
        if 0.5 < weatherProb <= 0.8:
            currWeather = 'P'
        if weatherProb > 0.8:
            currWeather = 'H'
        if gameProb <= 0.7:
            currGame = 'B'
        elif 0.7 < gameProb <= 0.9:
            currGame = 'S'
        else:
            currGame = 'C'

    if currWeather == 'P':
        if weatherProb <= 0.2:
            currWeather = 'C'
        if weatherProb > 0.7:
            currWeather = 'H'
        if gameProb <= 0.6:
            currGame = 'B'
        elif 0.6 < gameProb <= 0.9:
            currGame = 'S'
        else:
            currGame = 'C'

    if currWeather == 'H':
        if weatherProb <= 0.4:
            currWeather = 'C'
        if 0.4 < weatherProb <= 0.6:
            currWeather = 'P'
        if gameProb <= 0.1:
            currGame = 'B'
        elif 0.1 < gameProb <= 0.2:
            currGame = 'S'
        else:
            currGame = 'C'

    weatherFile.write(currWeather)
    gameFile.write(currGame)

weatherFile.close()
gameFile.close()


