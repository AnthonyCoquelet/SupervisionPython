import os
import psutil
import time
ospc= os.name
def os():
    if ospc == "nt":
        print("L'Os de l'ordinateur est Windows")
    else :
        print("L'Os de l'ordinateur n'est pas Windows")
def cpu ():
    x= psutil.cpu_percent(1)
    print("Le CPU est utiliser à {} %".format(x))
def ram():
    y=psutil.virtual_memory().percent
    print("La RAM est utiliser à {} %".format(y))

os()
cpu()
ram()
