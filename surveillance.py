import os
import psutil
import time
import config
import alrtEmail
monitoring = bool(True)
fichier_Log = open(config.nom_Fichier,"a")

def cpu ():
    x= psutil.cpu_percent(1)
    if x >= config.cpu:
        fichier_Log.write("Attention : Surcharge du processeur.")
    else:
        fichier_Log.write("Le CPU est utiliser à {} %".format(x))
        fichier_Log.write("\n")
def ram():
    y=psutil.virtual_memory().percent
    if y >= config.ram:
        fichier_Log.write("Attention : Surcharge du la RAM.")
        fichier_Log.write("\n")
    else:
        fichier_Log.write("La RAM est utiliser à {} %".format(y))
        fichier_Log.write("\n")

while monitoring == True :
    fichier_Log = open(config.nom_Fichier,"a")
    time.sleep(config.slp)
    cpu()
    ram()
    fichier_Log.close() 
