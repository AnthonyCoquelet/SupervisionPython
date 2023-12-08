import os
import psutil
import time
ospc= os.name
fichier_Log = open("Monitoring.txt")
def os():
    if ospc == "nt":
        fichier_Log.write("L'Os de l'ordinateur est Windows")
    else :
        fichier_Log.write("L'Os de l'ordinateur n'est pas Windows")
def cpu ():
    x= psutil.cpu_percent(1)
    fichier_Log.write("Le CPU est utiliser à {} %".format(x))
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser à {} %".format(y))

os()
cpu()
ram()
