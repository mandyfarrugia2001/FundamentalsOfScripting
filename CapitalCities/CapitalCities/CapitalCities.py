#Importing built-in Python modules to be used in this program.
import random #To generate random country and capital city from the text file.

"""
These values represent the final score,
thus values change according to user's guesses.
"""
timesWon = 0
timesLost = 0

def returnListCountries():
    """
    Filling list with countries and capital cities delimited by a dash.
    The text file will then be populated with all elements in the list.
    """
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
    
    #Return list to be used in populateTextFile function.
    return countriesCities

"""
Accepts only one parameter (read/write rights accordingly).
In case of issues with loading the text files,
the author has taken care of handling I/O related exceptions.
"""
def accessFile(mode):
    """
    By default, the try block should be executed,
    it contains potentially erroneous code.
    In case an exception arises, run the except block
    to prevent the program from crashing.
    """
    try:
        #By default, we will only be using the text file created in populateTextField function.
        textFile = open("countries.txt", mode)
        return textFile
    except IOError:
        #Print a so-to-speak user-friendly error message.
        print("Could not access file! Try again later.")

#Display the amount of times the user lost and won after all questions are answered.
def displayScore():
    #f and {} embody string interpolation.
    print(f"Total times won: {timesWon}\nTotal times lost: {timesLost}\n")

def generateQuiz():
    """
    The scores are now accessible within generateQuiz()
    as they have been declared as global.

    The randomly generated country and capital city
    has been retrieved from splitData().

    The user will be asked to guess the capital city
    of the country generated at random.

    If the user's guess is correct, a message is displayed
    and they are awarded one point. (increment timesWon by 1)

    The author has taken input validation into consideration,
    thus numeric input and blank spaces are penalized
    as though they are incorrect answers.
    Display a message and increment timesLost by 1.
    Same applies for incorrect guesses.
    """
    global timesWon
    global timesLost

    #Retrieve values from splitData function.
    country, capitalCity = splitData()

    #Prompt user to guess the capital city of the randomly generated country.
    guessCapitalCity = input(f"What is the capital city of {country}?: ")

    """
    Input validation stage:
    1) If the input matches the capital city stored in its variable,
        award user with one point and display a message.
        (increment timesWon by 1)
    2) If If the input contains numbers or input is blank,
        increment timesLost by 1 and display a message.
        Same applies for incorrect guesses.
    """
    if guessCapitalCity == capitalCity:
        print("Correct!\n\n")
        timesWon += 1
    elif guessCapitalCity.isdigit() or guessCapitalCity == "":
        print("Numeric input and blank spaces are not allowed!", end='\n\n')
        timesLost += 1
    else:
        print(f"Incorrect! The answer was {capitalCity}.", end='\n\n')
        timesLost += 1

def splitData():
    """
    Split the country and capital city.
    Store each of them in their own variable.
    Then return the two values for use in other functions.
    """

    #Access the file created in populateTextFile.
    file = accessFile("r").read().splitlines() #Read and split each line.
    #Select a random line from the text file.
    randomData = random.choice(file)
    #Get the index representing the first occurrence of the dash.
    delimiter = randomData.find('-')
    #Get the country from the first character to the delimiter.
    country = randomData[0:delimiter]
    #Exclude the delimiter and get the remaining characters representing the capital city.
    capitalCity = randomData[(delimiter + 1):]
    #Return country and capitalCity for use in other functions.
    return(country, capitalCity)

def populateTextFile():
    #Prepare the text file for creation.
    file = accessFile("w")

    """
    Return the list from returnListCountries function.
    Stored in a variable to avoid having to refer
    to the function all the time.
    """
    countriesCities = returnListCountries()

    #Copy every element in the list to the text file.
    for index in range(len(countriesCities)):
        #Leave a blank line between one element and another.
        file.write(countriesCities[index] + '\n')

    #It is important to close I/O operations.
    file.close()

#Call the populateTextFile within the main method.
populateTextFile() #Create the text file.

#Ask three questions.
for index in range(3):
    generateQuiz()

#Display the score after all the questions are answered.
displayScore()
