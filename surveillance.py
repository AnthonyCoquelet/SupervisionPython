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
def ram():
    y=psutil.virtual_memory().percent
    fichier_Log.write("La RAM est utiliser à {} %","\n".format(y))

os()
while monitoring == True :
    time.sleep(slp)
    cpu()
    ram()
