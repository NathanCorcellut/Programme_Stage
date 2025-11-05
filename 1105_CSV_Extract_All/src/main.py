#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

def generateTypedContentFromExcelFile(nameOfFilePath, positionOfFirstValueLine, positionOfFirstValueColumn, 
                                   previousCellSeparator = ';', previsousDecimalSeparator = ',',
                                   desiredType = float):
    content = []

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
            content.append(liste)
            idx_line += 1

    return content


    
contenu = generateTypedContentFromExcelFile("./data/24A010072_20241015_090520_USZ_MESS.csv", 1, 2)



indices = []
debits = []
ecarts_debit = []
for i in range(1, len(contenu)):
    indices.append(i)
    debits.append(contenu[i][2])
    if i == 1:
        ecarts_debit.append(0)
    else:
        ecarts_debit.append(abs(debits[i-1]-debits[i-2]))

plt.scatter(indices, debits, s=0.1)
plt.scatter(indices, ecarts_debit, s=0.1)

plt.legend("debits")

#Ajout des titres et de la grille
plt.title("Debit au cours du temps") #Titre principal
plt.xlabel("Time")          #Titre de l'axe horizontal (X)
plt.ylabel("Debit")  #Titre de l'axe vertical (Y)
plt.grid(True)          #Ajout de la grille

#Sauvegarde du résultat 
plt.savefig("./output/debits_extraits.png", dpi = 500) #sous le nom "Q5-loi_rang-taille_terres.png"
plt.close() #Fermeture 'propre' du graphe