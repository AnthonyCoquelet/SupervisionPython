import os
import psutil
import time
fichier_Log = open("Monitoring.txt","a")
def cpu ():
    x= psutil.cpu_percent(1)
    fichier_Log.write("Le CPU est utiliser a {} %.".format(x))
    fichier_Log.write("\n")
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser a {} %.".format(y))
    fichier_Log.write("\n")
def tout():
    cpu()
    ram()
tout()
