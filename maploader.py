import pygame

def loadMap(mapSource):                     #mapSource is a path to a textfile
    booleanMap = []                         #initial list of lists
    with open(mapSource) as m:              
        for line in m:
            singleLine = list(line)         #getting every line as a list of characters
            singleLine = singleLine[:-1]    #erasing a line feed
            booleanMap.append(singleLine)   #appending a line to list of lists
    return booleanMap                       #boleanMap[Y-axis][X-axis]


#testing function call
#sciezka = './map'
#mapka = loadMap(sciezka)
#print(mapka)