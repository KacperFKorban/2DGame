import pygame

def LoadMap(mapSource):
    booleanMap = []                         #initial list of lists
    with open(mapSource) as m:              
        for line in m:
            singleLine = list(line)         #getting every line as a list of characters
            singleLine = singleLine[:-1]    #erasing line feed
            booleanMap.append(singleLine)   #appending list to list of lists
    
    return booleanMap


#testing function call
#mapka = LoadMap('./map')
#print(mapka)