import os
import psutil
import time
ospc= os.name
fichier_Log = open("Monitoring.txt","a")
monitoring = bool(True)
slp = int(input("Combien de temps voulez-vous entre deux executions ?"))
def os():
    if ospc == "nt":
        fichier_Log.write("L'Os de l'ordinateur est Windows","\n")
    else :
        fichier_Log.write("L'Os de l'ordinateur n'est pas Windows","\n")
def cpu ():
    x= psutil.cpu_percent(1)
    fichier_Log.write("Le CPU est utiliser à {} %","\n".format(x))
    if x >= 70:
        print("Attention : Surcharge du processeur.")
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser à {} %","\n".format(y))
    if y >= 70:
        print("Attention : Surcharge de la RAM.")

os()
while monitoring == True :
    fichier_Log = open("Monitoring.txt","a")
    time.sleep(slp)
    cpu()
    ram()
    fichier_Log.close()
