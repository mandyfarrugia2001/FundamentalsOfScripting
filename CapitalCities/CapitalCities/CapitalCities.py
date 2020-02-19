import random

timesWon = 0
timesLost = 0

def returnListCountries():
    countriesCities = ["Albania-Tirana", "Andorra-Andorra la Vella",
                       "Armenia-Yerevan", "Austria-Vienna",
                       "Azerbaijan-Baku", "Belarus-Minsk",
                       "Belgium-Brussels", "Bosnia and Herzegovina-Sarajevo",
                       "Bulgaria-Sofia", "Croatia-Zagreb",
                       "Cyprus-Nicosia", "Czech Republic-Prague",
                       "Denmark-Copenhagen", "Estonia-Tallinn",
                       "Finland-Helsinki", "France-Paris",
                       "Georgia-Tbilisi", "Germany-Berlin",
                       "Greece-Athens", "Hungary-Budapest",
                       "Iceland-Reykjavik", "Ireland-Dublin",
                       "Italy-Rome", "Kazakhstan-Astana",
                       "Kosovo-Pristina", "Latvia-Riga",
                       "Liechtenstein-Vaduz", "Lithuania-Vilnius",
                       "Luxembourg-Luxembourg city", "Macedonia (FYROM)-Skopje",
                       "Malta-Valletta", "Moldova-Chisinau", "Monaco-Monaco city",
                       "Montenegro-Podgorica", "Netherlands-Amsterdam",
                       "Norway-Oslo", "Poland-Warsaw", "Portugal-Lisbon",
                       "Romania-Bucharest", "Russia-Moscow", 
                       "San Marino-San Marino city", "Serbia-Belgrade",
                       "Slovakia-Bratislava", "Spain-Madrid",
                       "Sweden-Stockholm", "Switzerland-Bern",
                       "Turkey-Ankara", "Ukraine-Kyiv", 
                       "United Kingdom-London"]
    
    return countriesCities

def accessFile(mode):
    try:
        textFile = open("countries.txt", mode)
        return textFile
    except IOError:
        print("Could not access file! Try again later.")

def displayScore():
    print(f"Total times won: {timesWon}\nTotal times lost: {timesLost}\n")

def generateQuiz():
    global timesWon
    global timesLost

    country, capitalCity = splitData()

    guessCapitalCity = input(f"What is the capital city of {country}?: ")
    if guessCapitalCity != capitalCity:
        print(f"Incorrect! The answer was {capitalCity}.", end='\n\n')
        timesLost += 1
    elif guessCapitalCity.isdigit() or guessCapitalCity == "":
        print("Numeric input and blank spaces are not allowed!", end='\n\n')
        timesLost += 1
    else:
        print("Correct!\n\n")
        timesWon += 1

def splitData():
    file = accessFile("r").read().splitlines()
    randomData = random.choice(file)
    delimiter = randomData.find('-')
    country = randomData[0:delimiter]
    capitalCity = randomData[(delimiter + 1):]
    return(country, capitalCity)

def populateTextFile():
    file = accessFile("w")
    countriesCities = returnListCountries()
    for index in range(len(countriesCities)):
        file.write(countriesCities[index] + '\n')
    file.close()
    
populateTextFile()

for index in range(3):
    generateQuiz()
displayScore()
