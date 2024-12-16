#Fonctions de configuration du PC
def setProc(): #Fonction pour définir le processeur
    proc=input("Processeur : ")
    return proc

def setRam(): #Fonction pour définir la RAM
    ram=int(input("Quantité de RAM : "))
    return ram

def setStorageSize(): #Fonction pour définir la taille du stockage
    storageSize=int(input("Taille du Stockage : "))
    return storageSize

def setStorageType(): #Fonction pour définir le type de stockage
    storageType=input("Type de Stockage (SSD ou HDD): ")
    while storageType!='SSD' and storageType!='HDD':
        storageType=input("Type de Stockage (SSD ou HDD): ")
    return storageType

def setOS(): #Fonction pour définir le système d'exploitation
    os=input("OS (Windows, Linux, MacOS ou BSD): ")
    while os!='Windows' and os!='Linux' and os!='MacOS' and os!='BSD':
        os=input("OS (Windows, Linux, MacOS ou BSD): ")
    return os


#Fonctions pour extraire les clés et les valeurs du dictionnaire

def displayKey(dico): #Fonction pour extraire les clés du dictionnaire - Répond à la question 2
    for key in dico.keys():
        print(key)

def displayValue(dico): #Fonction pour extraire les valeurs du dictionnaire - Répond à la question 3
    for value in dico.values():
        print(value)

#Fonctions pour extraire les clés et les valeurs du dictionnaire

def extractKey(dico): #Fonction pour extraire les clés du dictionnaire - Répond à la question 4
    keys=[]
    for key in dico.keys():
        keys.append(key)
    return keys

def extractValue(dico): #Fonction pour extraire les valeurs du dictionnaire - Répond à la question 5
    values=[]
    for value in dico.values():
        values.append(value)
    return values

# Fonction des menus

def createPC(dico): #Fonction pour créer un PC - Répond à la question 1
    nom=input("Nom du PC : ")
    proc=setProc()
    ram=setRam()
    storageSize=setStorageSize()
    storageType=setStorageType()
    os=setOS()
    dico[nom]={
        "Processeur":proc,
        "RAM":ram,
        "Taille du Stockage":storageSize,
        "Type de Stockage":storageType,
        "OS":os
    }

def modifyPC(dico): #Fonction pour modifier un PC - Répond à la question 6
    displayKey(dico)
    nom=input("Nom du PC à modifier : ")
    if nom in dico:
        print("1. Modifier le processeur")
        print("2. Modifier la RAM")
        print("3. Modifier la taille du stockage")
        print("4. Modifier le type de stockage")
        print("5. Modifier l'OS")
        print("6. Quitter")
        choix=int(input("Sélectionner une option : "))
        while choix!=6:
            if choix==1:
                proc=setProc()
                dico[nom]["Processeur"]=proc
            elif choix==2:
                ram=setRam()
                dico[nom]["RAM"]=ram
            elif choix==3:
                storageSize=setStorageSize()
                dico[nom]["Taille du Stockage"]=storageSize
            elif choix==4:
                storageType=setStorageType()
                dico[nom]["Type de Stockage"]=storageType
            elif choix==5:
                os=setOS()
                dico[nom]["OS"]=os
            else:
                print("Option invalide")
            if choix in [1,2,3,4,5]:
                print("Paramètre modifié!")
            print("")
            print("1. Modifier le processeur")
            print("2. Modifier la RAM")
            print("3. Modifier la taille du stockage")
            print("4. Modifier le type de stockage")
            print("5. Modifier l'OS")
            print("6. Quitter")
            choix=int(input("Sélectionner une option : "))
    else:
        print("Le PC n'existe pas")

# Fonction de tri
def orderByStorageSize(dico): #Fonction pour trier les PC par taille de stockage - Répond à la question 7
    values=extractValue(dico)
    storageSize=[]
    for value in values:
        storageSize.append(value["Taille du Stockage"][0])
    storageSize.sort()
    for size in storageSize:
        for key,value in dico.items():
            if value["Taille du Stockage"][0]==size:
                print(key,":","Taille du Stockage =",value["Taille du Stockage"][0])

def orderByRAM(dico): #Fonction pour trier les PC par RAM
    values=extractValue(dico)
    ram=[]
    for value in values:
        ram.append(value["RAM"][0])
    ram.sort()
    for r in ram:
        for key,value in dico.items():
            if value["RAM"][0]==r:
                print(key,":","RAM =",value["RAM"][0])

# Fonction de recherche

def exchangePC(dico): #Fonction pour échanger les PC - Répond à la question 8
    nom1=input("Nom du premier PC : ")
    nom2=input("Nom du deuxième PC : ")
    if nom1 in dico and nom2 in dico:
        temp=copyDico(dico[nom1])
        dico[nom1]=dico[nom2]
        dico[nom2]=temp
    else:
        print("Un des PC n'existe pas")

def copyDico(dico): #Fonction pour copier le dictionnaire - Répond à la question 9
    newDico={}
    for key,value in dico.items():
        newDico[key]=value
    return newDico


def getBestPC(dico): #Fonction pour obtenir le meilleur PC - Répond à la question 10
    bestPCName=""
    bestPCConfig={
        "RAM":0,
        "Taille du Stockage":0,
        "Type de Stockage":"",
    }
    for key,value in dico.items():
        bestPCScore=0
        newPCScore=0
        if value["RAM"] < bestPCConfig["RAM"]:
            bestPCConfig+=1
        elif value["RAM"] > bestPCConfig["RAM"]:
            newPCScore+=1
        if value["Taille du Stockage"] < bestPCConfig["Taille du Stockage"]:
            bestPCConfig+=1
        elif value["Taille du Stockage"] > bestPCConfig["Taille du Stockage"]:
            newPCScore+=1
        if value["Type de Stockage"] == "SSD" and bestPCConfig["Type de Stockage"] == "HDD":
            bestPCConfig+=1
        elif value["Type de Stockage"] == "HDD" and bestPCConfig["Type de Stockage"] == "SSD":
            newPCScore+=1
        if newPCScore > bestPCScore:
            bestPCScore=newPCScore
            bestPCName=key
            bestPCConfig["RAM"]=value["RAM"]
            bestPCConfig["Taille du Stockage"]=value["Taille du Stockage"]
            bestPCConfig["Type de Stockage"]=value["Type de Stockage"]

    return bestPCName

# Programme principal

My_PC={} #Initialisation du dictionnaire

print("1. Ajouter un PC")
print("2. Modifier un PC")
print("3. Supprimer un PC")
print("4. Afficher la liste des PC")
print("5. Tri par taille de stockage")
print("6. Tri par RAM")
print("7. Echanger deux PC")
print("8. Meilleur PC")
print("9. Quitter")
choix=int(input("Sélectionner une option : ")) #Sélection de l'option
print("")

while choix!=10:
    if choix==1:
        createPC(My_PC)
    elif choix==2:
        modifyPC(My_PC)
    elif choix==3:
        nom=input("Nom du PC à supprimer : ")
        if nom in My_PC:
            del My_PC[nom]
        else:
            print("Le PC n'existe pas")
    elif choix==4:
        for key,value in My_PC.items():
            print("-",key)
    elif choix==5:
        orderByStorageSize(My_PC)
    elif choix==6:
        orderByRAM(My_PC)
    elif choix==7:
        exchangePC(My_PC)
    elif choix==8:
        bestPC=getBestPC(My_PC)
        print("Le meilleur PC est",bestPC)
    else:
        print("Option invalide")
    
    print("")
    print("1. Ajouter un PC")
    print("2. Modifier un PC")
    print("3. Supprimer un PC")
    print("4. Afficher la liste des PC")
    print("5. Tri par taille de stockage")
    print("6. Tri par RAM")
    print("7. Echanger deux PC")
    print("8. Meilleur PC")
    print("9. Quitter")
    choix=int(input("Sélectionner une option : "))
