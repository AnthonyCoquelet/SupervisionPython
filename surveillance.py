import os
import psutil
import time
ospc= os.name
fichier_Log = open("Monitoring.txt","a")
def os():
    if ospc == "nt":
        fichier_Log.write("L'Os de l'ordinateur est Windows.")
        fichier_Log.write("\n")
    else :
        fichier_Log.write("L'Os de l'ordinateur n'est pas Windows.")
        fichier_Log.write("\n")
def cpu ():
    x= psutil.cpu_percent(1)
    fichier_Log.write("Le CPU est utiliser a {} %.".format(x))
    fichier_Log.write("\n")
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser a {} %.".format(y))
    fichier_Log.write("\n")
def tout():
    os()
    cpu()
    ram()
tout()
