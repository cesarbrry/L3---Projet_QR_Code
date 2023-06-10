import turtle
import sys
import math
import random

# FONCTION ASCII 
# ENTREE : Une chaine de char et une liste vide 
# SORTIE : Une liste remplie des valeurs ASCII de chaque char +
#          Val ASCII 0 qui correspond a NULL (fin du message)

def tabUnicode (chaine,tab):
    print("\nMESSAGE DE BASE\n")
    for i in chaine:
        tab.append(ord(i))    
    print(tab)
    return tab

# FONCTION CRYPTE
# ENTREE : Une chaine de charactere 
# SORTIE : Une chaine de charactere cryptée avec le code de César

def cryptage(tab,clef):
    print("\nMESSAGE CRYPTE\n")
    for i in range(len(tab)):
        tab[i] += (math.ceil((len(tab))/clef))
    print(tab)
    return tab

# FONCTION BINAIRE // Prends en argument une liste d'entier
# ENTREE : Une liste d'entier en base 10
# SORTIE : Une liste de listes de taille 8 consituées de 0 et de 1 
#          correspondantes aux characteres saisis

def binaire (tab):
    
    print("\nMESSAGE EN BINAIRE\n")
    tampon = 0
    
    for i in range(len(tab)):
        
        tab[i] = bin(tab[i])
        tampon = tab[i]
        
        tab[i] = []
        
        for j in tampon :
            tab[i].append(j)
    
        del tab[i][0:2]
    
    for i in range(len(tab)):
        while (len(tab[i])<8):
            tab[i].insert(0,'0')
            
        print(tab[i])
    print("\n")
    return tab;

# FONCTION AJOUTE BIT DE CONTROLE :
# ENTREE : Une liste de listes de taille 8 consituées de 0 et de 1 
#          correspondantes aux characteres saisis
# SORTIE : Une liste de listes de taille 11 consituées de 0 et de 1 
#          correspondantes aux characteres saisis + 3 bits de parité differents 
#          permettant de controler le message et detecter les erreurs

def CtrlBit(tab):
    
    print("BITS DE CONTROLE \n")
    
    valeurBit = 0
    PariteCroiseeDeb  = 0 ;
    PariteCroiseeFull = 0 ;
    PariteCroiseeFin  = 0 ;
    PariteEntrelaDeb  = 0 ;
    PariteEntrelaFin  = 0 ; 
    
    for i in range(len(tab)):
        
        for j in range(4,8):
            valeurBit += int(tab[i][j])
            valeurBit = valeurBit%2
        
        tab[i].insert(0,str(valeurBit))
        PariteCroiseeFin += valeurBit
        valeurBit = 0
        
        for j in range(1,5):
            valeurBit += int(tab[i][j])
            valeurBit = valeurBit%2
        
        tab[i].insert(0,str(valeurBit))
        PariteCroiseeDeb += valeurBit
        valeurBit = 0
        
        for j in range(2,10):
            valeurBit += int(tab[i][j])
            valeurBit = valeurBit%2
        
        tab[i].insert(0,str(valeurBit))
        PariteCroiseeFull += valeurBit
        valeurBit = 0
        
        for j in range(4,11,2):
            valeurBit += int(tab[i][j])
            valeurBit = valeurBit%2
            
        tab[i].insert(0,str(valeurBit))
        PariteEntrelaFin += valeurBit
        valeurBit = 0
        
        for j in range(4,12,2):
            valeurBit += int(tab[i][j])
            valeurBit = valeurBit%2
            
        tab[i].insert(0,str(valeurBit))
        PariteEntrelaDeb += valeurBit
        valeurBit = 0
        
        print(tab[i])
        
    tab.append([str(PariteEntrelaDeb%2),str(PariteEntrelaFin%2),str(PariteCroiseeFull%2),str(PariteCroiseeDeb%2),str(PariteCroiseeFin%2)])
    print(tab[len(tab)-1])
    print("\n")
        
    return tab;

#FONCTION CREATION MESSAGE TRANSMIS
# Le but de cette fonction est uniquement d'introduire aleatoirement des erreurs dans la message envoyé 
# afin de voir si on peut detecter les lettres mal transmises et savoir le nombre d'erreur du message

def TransmMess(tab):
    
    print("INSERTION DES ERREURS\n")
    
    tabMessRecus = []
    tabMessRecus = tab

    NbErreurs = random.randint(0,10)
    TamponIndex    = []
    TamponIndexBool = []
    
    for i in range(NbErreurs):
        j = random.randint(0,len(tab)-2)
        k = random.randint(0,12)
        
        if (tab[j][k]=='0'):
            tab[j][k]='1'
        else : 
            tab[j][k]='0'
        
        if (( k>4 ) and (j not in TamponIndexBool)) : 
            TamponIndex.append(j)
        
        if (( k<=4 ) and (j not in TamponIndexBool)) : 
            TamponIndexBool.append(j)
            
    for i in range(len(tab)):
        print(tab[i])   

    print("\nNombre total d'erreur(s) inseree(s) : " + str(NbErreurs))
    print("\nCharacteres du message errones [ "+str(len(TamponIndex))+" ] :")
    print(sorted(TamponIndex))
    print("\nBits de controle du message errones [ "+str(len(TamponIndexBool))+" ] :")
    print(sorted(TamponIndexBool))
    print("\n")
    
    return tabMessRecus    

#FONCTION VERIFICATION D'ERREURS
# Le but de cette fonction est d'utilisé les bits de parité créés et d'essayer de trouver le nombre 
# d'erreurs générés dans notre message et d'afficher en console le message qui est recu

def VerifErreur(tab,clefdecryptage) :
    
    print("DETECTION D'ERREUR \n")
    
    valBitCtrlFull  = 0 
    valBitCtrlDroit = 0 
    valBitCtrlGauch = 0
    valBitEntrDroit = 0
    valBitEntrGauch = 0
    
    CompteurErreur         = 0
    CompteurErreurTotal    = 0
    CompteurErreurBool     = 0
    
    VerifBitCtrlFull   = 0 
    VerifBitCtrlDroit  = 0 
    VerifBitCtrlGauch  = 0 
    VerifBitEntrDroit  = 0
    VerifBitEntrGauch  = 0
    
    BoolVerifGauche = False 
    BoolVerifDroit  = False 
    BoolVerifFull   = False 
    BoolEntrDroit   = False
    BoolEntrGauch   = False
    
    tableauIndex    = []
    
    # VERIFICATION SI LA PARITE CROISEE EST RESPECTEE

    for i in range(len(tab)-1):
        
        VerifBitEntrGauch += int(tab[i][0])
        VerifBitEntrDroit += int(tab[i][1])
        VerifBitCtrlFull  += int(tab[i][2])
        VerifBitCtrlGauch += int(tab[i][3])
        VerifBitCtrlDroit += int(tab[i][4])
    
    VerifBitEntrGauch  = VerifBitEntrGauch%2
    VerifBitEntrDroit  = VerifBitEntrDroit%2
    VerifBitCtrlFull  = VerifBitCtrlFull%2
    VerifBitCtrlGauch = VerifBitCtrlGauch%2
    VerifBitCtrlDroit = VerifBitCtrlDroit%2
    
    # BOOLEEN POUR DEFINIR SI LES BITS DE CONTROLE SONT UTILISES OU NON 
        
    if (VerifBitEntrGauch == int(tab[len(tab)-1][0])) : 
        VerifBitEntrGauch = True
        print("Bit de controle Entrelace Debut   VRAI")
    else : 
        CompteurErreurBool += 1
        print("Bit de controle Entrelace Debut   FAUX")
        
    if (VerifBitEntrDroit == int(tab[len(tab)-1][1])) : 
        VerifBitEntrDroit = True
        print("Bit de controle Entrelace Fin     VRAI")
    else : 
        CompteurErreurBool += 1
        print("Bit de controle Entrelace Fin     FAUX")
        
    if (VerifBitCtrlFull == int(tab[len(tab)-1][2])) : 
        BoolVerifFull = True
        print("Bit de controle Full              VRAI")
    else : 
        CompteurErreurBool += 1
        print("Bit de controle Full              FAUX")
        
    if (VerifBitCtrlGauch == int(tab[len(tab)-1][3])) : 
        BoolVerifGauche = True
        print("Bit de controle Gauche            VRAI")  
    else : 
        CompteurErreurBool += 1
        print("Bit de controle Gauche            FAUX")
        
    if (VerifBitCtrlDroit == int(tab[len(tab)-1][4])) : 
        BoolVerifDroit = True
        print("Bit de controle Droite            VRAI")
    else : 
        CompteurErreurBool += 1
        print("Bit de controle Droite            FAUX")
    
    print("\n")
    
    # ON CALCULE POUR CAQUE LIGNE LA VALEUR DES 3 BITS DE CONTROLE 

    for i in range(len(tab)-1):
        for j in range(9,13):
            valBitCtrlDroit += int(tab[i][j])
        for j in range(5,9):
            valBitCtrlGauch += int(tab[i][j])
        for j in range(5,13):
            valBitCtrlFull  += int(tab[i][j])
        for j in range(5,13,2):
            valBitEntrGauch += int(tab[i][j])
        for j in range(6,13,2):
            valBitEntrGauch += int(tab[i][j])
            
        valBitEntrGauch = valBitEntrGauch%2
        valBitEntrDroit = valBitEntrDroit%2
        valBitCtrlFull  = valBitCtrlFull%2
        valBitCtrlGauch = valBitCtrlGauch%2
        valBitCtrlDroit = valBitCtrlDroit%2
        
        
    # VERIFICATION DES BITS POUR CHAQUE POSSIBILITE

# print("bit n° "+ str(i) +" bien transmis")

        if (BoolVerifFull == True):
            if (BoolEntrGauch == True):
                if (BoolEntrDroit == True):
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3]:
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif (BoolVerifGauche == False) :
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]") 
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2]:
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                elif (BoolEntrDroit == False):
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlFull)!=tab[i][2] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
            elif (BoolEntrGauch == False):
                if (BoolEntrDroit == True):
                    
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlFull)!=tab[i][2] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                elif (BoolEntrDroit == False):
                    
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlGauch)!=tab[i][3] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitCtrlFull)!=tab[i][2] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitCtrlFull) != tab[i][2] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                            
        elif (BoolVerifFull == False):
            if (BoolEntrGauch == True):
                if (BoolEntrDroit == True):
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlGauch)!=tab[i][3]:
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif (BoolVerifGauche == False) :
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitEntrDroit)!=tab[i][1] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                elif (BoolEntrDroit == False):
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlGauch)!=tab[i][3] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrGauch)!=tab[i][0] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrGauch)!=tab[i][0] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
            elif (BoolEntrGauch == False):
                if (BoolEntrDroit == True):
                    
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlGauch)!=tab[i][3] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitEntrDroit)!=tab[i][1] or str(valBitCtrlDroit)!=tab[i][4] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitEntrDroit)!=tab[i][1] :
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                elif (BoolEntrDroit == False):
                    
                    if(BoolVerifGauche == True):
                        if(BoolVerifDroit == True):
                            if str(valBitCtrlGauch)!=tab[i][3] or str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            if str(valBitCtrlGauch)!=tab[i][3] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                    elif(BoolVerifGauche == False):
                        if(BoolVerifDroit == True):
                            if str(valBitCtrlDroit)!=tab[i][4] : 
                                print("ERREUR BIT [ " + str(i) + " ]")
                                CompteurErreur += 1
                                if i not in tableauIndex : 
                                    tableauIndex.append(i)
                                
                        elif(BoolVerifDroit==False):
                            print("ERREUR POSSIBLE BIT [ " + str(i) + " ]")
                            CompteurErreurTotal += 1
                            if i not in tableauIndex : 
                                tableauIndex.append(i)
                            
        
        valBitEntrDroit = 0
        valBitEntrGauch = 0
        valBitCtrlDroit = 0
        valBitCtrlFull  = 0
        valBitCtrlGauch = 0 
            
    CompteurErreurMess = CompteurErreur + CompteurErreurTotal
    CompteurErreurTotal += (CompteurErreur + CompteurErreurBool)
    
    print("\nAu total on detecte "+ str(CompteurErreurTotal) + " erreurs de transmission dans le message dont : \n[ "+str(CompteurErreurMess)+" ] erreurs dans le message \n[ "+str(CompteurErreurBool)+" ] erreurs dans les bits de controle.\n\nOn a les characteres suivant du message de base detectes comme faux :")
    print(sorted(tableauIndex))
    
    messagerecu = []
    concatene = ''
    
    for i in range (len(tab)-1):
        if i not in (tableauIndex) : 
            for j in range(5,13):
                concatene += tab[i][j]
        else : 
            concatene += '*'
        messagerecu.append(concatene)
        concatene=''
    
    for i in range(len(messagerecu)):
        if messagerecu[i] != '*':
            messagerecu[i] = int(messagerecu[i],2)
            
            if clefdecryptage != 0 : 
                messagerecu[i] -= (math.ceil((len(tab)-1)/clefdecryptage))
            
            messagerecu[i] = chr(messagerecu[i])
        concatene += messagerecu[i]
    
    print("\nmessage recu : "+concatene+"\n[Quand le charactere est errone, il est remplace par le charactere '*']")
        
                
            
    return(tableauIndex)
             
        
# DESSINER LE QRCODE :
# ENTREE : Une double liste de correspondant au message en binaire
# SORTIE : Un graphique coddant le message de base

def DessinQR(tab):
    
    t  = turtle.Turtle()
    ts = turtle.Screen()
    
    t.pensize(1)
    m=math
    t.penup()
    t.hideturtle()
    t.setx(-750)
    t.sety(0)
    t.speed(0)
    t.right(90)
    t.pendown()
    
    t.pensize(3)
    t.circle(50,360)
    
    if (len(tab)<80):
        t.penup()
        t.forward(50)
        t.left(90)
        t.forward(110)
        t.left(90)
        t.forward(50+(315/2))
        t.right(180)
        t.pendown()
    
    else :
        t.penup()
        t.pensize(10)
        t.forward(50)
        t.left(90)
        t.forward(110)
        t.left(90)
        t.forward(50+(635/2))
        t.right(180)
        t.pendown()
    
    t.pensize(1)
    compteur = 0
    longueur = len(tab)
    
    if (len(tab)<80):
        
        t.begin_fill()
        t.forward(315)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(315)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(5)
        t.end_fill()
        
        t.penup()
        t.left(90)
        t.forward(15)
        t.right(90)
        t.pendown()
        
    else :
        
        t.begin_fill()
        t.forward(635)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(635)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(5)
        t.end_fill()
        
        t.penup()
        t.left(90)
        t.forward(15)
        t.right(90)
        t.pendown()
    
    for i in range(len(tab)):
        
        t.fillcolor('black')
        
        for j in range(0,5):
            
            if tab[i][j] == '1' : 
                
                t.begin_fill()
                t.circle(5,360)
                t.end_fill()
                
                t.penup()
                t.forward(15)
                t.pendown()
            
            elif tab[i][j] == '0' : 
                
                t.circle(5,360)
                t.penup()
                t.forward(15)
                t.pendown()
        
        if i != (len(tab)-1):
            
            t.begin_fill()
            t.forward(45)
            t.left(90)
            t.forward(10)
            t.left(90)
            t.forward(45)
            t.circle(5,180)
            t.end_fill()
            
            t.penup()
            t.forward(50)
            t.pendown()
            
            t.begin_fill()
            t.forward(45)
            t.circle(5,180)
            t.forward(45)
            t.left(90)
            t.forward(10)
            t.left(90)
            t.end_fill()
            
            t.penup()
            t.forward(60)
            t.pendown()
        
        
            for j in range(5,13):
                
                if tab[i][j] == '1' : 
                    
                    t.begin_fill()
                    t.circle(5,360)
                    t.end_fill()
                    
                    t.penup()
                    t.forward(15)
                    t.pendown()
                
                elif tab[i][j] == '0' : 
                    
                    t.circle(5,360)
                    t.penup()
                    t.forward(15)
                    t.pendown()
            
                
            t.penup()
            t.backward(5)
            t.pendown()        
            
            t.begin_fill()
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.end_fill()
                
            t.penup()
            t.left(180)
            t.forward(15)
            t.left(90)
            t.forward(300)
            t.right(180)
            t.pendown()
                
            compteur += 1 ;
        
        
        if (longueur > 80):
            
            if (compteur== m.ceil(longueur/2)) :
                t.penup()
                t.forward(320)
                t.right(90)
                t.forward(m.ceil(longueur/2)*15)
                t.left(90)
                t.pendown() 
                compteur = 0
  
    ts.mainloop()
    ts.exitonclick()
    
# FONCTION PRINCIPALE 

tabMessage      = []
tabIndexErreurs = []
message = input("Saisissez un message :")
clefdecryptage = 0

if len(message) <= 180:
    tabMessage  = tabUnicode(message, tabMessage)
    
    BoolCryptage = int(input("Souhaitez vous crypter votre message ? (0) NON / (1) OUI \nSaisissez votre choix : "))
    if BoolCryptage != 0 :
        clefdecryptage= int(input("Saisissez votre clef de chiffrage ( Doit etre inferieure a la longueur du message) : "))
        if clefdecryptage >= len(tabMessage) :
            print("\n")
            sys.exit("ERREUR : CLEF DE CHIFFRAGE TROP ELEVEE")
        tabMessage = cryptage(tabMessage, clefdecryptage)
    tabMessage  = binaire(tabMessage)
    CtrlBit(tabMessage)
    tabMessTransmis = TransmMess(tabMessage)
    tabIndexErreurs = VerifErreur(tabMessTransmis,clefdecryptage)
    DessinQR(tabMessTransmis) 

else : 
    print("\n")
    sys.exit("ERREUR : MESSAGE TROP LONG")
