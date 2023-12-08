import os
import psutil
import time
import config
ospc= os.name
fichier_Log = open(config.nom_Fichier,time.time,"a")
monitoring = bool(True)
def os():
    if ospc == "nt":
        fichier_Log.write("L'Os de l'ordinateur est Windows","\n")
    else :
        fichier_Log.write("L'Os de l'ordinateur n'est pas Windows","\n")
def cpu ():
    x= psutil.cpu_percent(1)
    fichier_Log.write("Le CPU est utiliser à {} %","\n".format(x))
    if x >= config.cpu:
        print("Attention : Surcharge du processeur.")
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser à {} %","\n".format(y))
    if y >= config.ram:
        print("Attention : Surcharge de la RAM.")

os()
while monitoring == True :
    fichier_Log = open(config.nom_Fichier,time.time,"a")
    time.sleep(config.slp)
    cpu()
    ram()
    fichier_Log.close()
