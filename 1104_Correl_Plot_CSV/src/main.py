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




def extractXYListsFromTxtFile(nameOfFilePath):
    # It returns a list of list of list as built:
    # [ [ ["label_1"], [X_1], [Y_1] ] , 
    #   [ ["label_2"], [X_2], [Y_2] ] ,
    #   [ ["label_3"], [X_3], [Y_3] ] ]

    final_liste = []
    with open(nameOfFilePath,"r") as file:
        label, X, Y = [], [], []
        writing = False
        for line in file:
            if line == ')\n':
                writing = False
                final_liste.append([label, X, Y])
                label, X, Y = [], [], []

            elif writing == True :
                x, temp = line.split('\t')
                y = temp.split('\n')[0]
                X.append(float(x))
                Y.append(float(y))

            elif "label " in line:
                writing = True
                temp = line.split(' ')[1]
                lab = temp.split(')')[0]
                label.append(lab)
                
    return final_liste


def generateGraphsFromXYLists(XYList, nameOfOutputPathAndName):
    for graph in XYList:
        label, X, Y = graph
        #Graphs
        plt.scatter(X, Y, s=1)
        plt.legend(label)

    #Ajout des titres et de la grille
    plt.title("Velocity Magnitude") #Titre principal
    plt.xlabel("Position")          #Titre de l'axe horizontal (X)
    plt.ylabel("Velocity")  #Titre de l'axe vertical (Y)
    plt.grid(True)          #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig(nameOfOutputPathAndName) #sous le nom "Q5-loi_rang-taille_terres.png"
    plt.close() #Fermeture 'propre' du graphe


def calculateMeanVelocity(PositionValues, VelocityValues):
    sum = 0
    for i in range(len(PositionValues)-1):
        sum += (VelocityValues[i] + VelocityValues[i+1]) * (PositionValues[i+1] - PositionValues[i]) /2.0
    mean_velocity = sum / (PositionValues[-1] - PositionValues[0])   
    return mean_velocity

contenu = generateTypedContentFromExcelFile("./data/24A010072_20241015_090520_USZ_MESS.csv", 1, 2)

liste = extractXYListsFromTxtFile("./data/velocity_captors.txt")

generateGraphsFromXYLists(liste, "./output/Velocity_Position.png")

c2 = extractXYListsFromTxtFile("./data/velocity_profile.txt")

generateGraphsFromXYLists(c2, "./output/3plotsofprofile.png")

label_1down, X_1down, Y_1down = liste[0]
vitesse_moyenne_1down = calculateMeanVelocity(X_1down, Y_1down)

print("La vitesse moyenne le long de {}, vaut {} ".format(label_1down[0], vitesse_moyenne_1down))

label_2down, X_2down, Y_2down = liste[1]
vitesse_moyenne_2down = calculateMeanVelocity(X_2down, Y_2down)

print("La vitesse moyenne le long de {}, vaut {} ".format(label_2down[0], vitesse_moyenne_2down))

label_mid, X_mid, Y_mid = c2[2]
vit_moy_mid = calculateMeanVelocity(X_mid, Y_mid)

print("La vitesse moyenne le long de {}, vaut {} ".format(label_mid[0], vit_moy_mid))

for i in range(0, 360):
    print(" --- multipliée par cos({} deg) =".format(i), vit_moy_mid * math.cos(i * 3.14159235897932384626/180))