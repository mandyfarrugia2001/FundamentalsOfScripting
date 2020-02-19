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

def accessFile(file, mode):
    textFile = open(file, mode)
    return textFile

def populateTextFile():
    file = accessFile("countries.txt", "w")
    countriesCities = returnListCountries()
    for index in range(len(countriesCities)):
        file.write(countriesCities[index] + '\n')
    file.close()
    
populateTextFile()




