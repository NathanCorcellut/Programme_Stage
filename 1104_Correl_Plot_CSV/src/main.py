#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

def generateTypedListFromExcelFile(nameOfFilePath, positionOfFirstValueLine, positionOfFirstValueColumn, 
                                   previousCellSeparator = ';', previsousDecimalSeparator = ',',
                                   desiredType = float):
    contenu = []

    with open(nameOfFilePath,"r") as file:
        idx_line = 0
        for line in file :
            liste = []
            info = ""
            for i in range(len(line)) :
                caracter = line[i]
                if caracter == previousCellSeparator  or  i == (len(line)-1):
                    if len(liste) >= positionOfFirstValueColumn and idx_line >= positionOfFirstValueLine:
                        info = info.replace(previsousDecimalSeparator,'.')
                        liste.append(desiredType(info))
                    else :
                        liste.append(info)
                    info = ""
                else:
                    info += caracter
            contenu.append(liste)
            idx_line += 1

    return contenu


def extractXYListsFromTxtFile(nameOfFilePath):
    liste =[]
    return liste

    
contenu = generateTypedListFromExcelFile("./data/24A010072_20241015_090520_USZ_MESS.csv", 1, 2)


print(contenu)

