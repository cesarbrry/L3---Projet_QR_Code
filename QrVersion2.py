import turtle
import math

# FONCTION CRYPTE
# ENTREE : Une chaine de charactere 
# SORTIE : Une chaine de charactere cryptée

def cryptage(tab):
    for i in range(len(tab)):
        tab[i] = tab[i] + ((len(tab)*8)%15)
    return tab
        
# FONCTION ASCII 
# ENTREE : Une chaine de char et une liste vide 
# SORTIE : Une liste remplie des valeurs ASCII de chaque char +
#          Val ASCII 0 qui correspond a NULL (fin du message)

def tabASCII (chaine,tab):
    for i in chaine:
        tab.append(ord(i))
    return tab


# FONCTION BINAIRE // Prends en argument une liste d'entier
# ENTREE : Une liste d'entier en base 10
# SORTIE : Une liste de listes de taille 8 consituées de 0 et de 1 correspondantes aux entier

def binaire (tab):
    
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
    print("\n\n")
    return tab;

# DESSINER LE QRCODE :
# ENTREE : Une double liste de correspondant au message en binaire
# SORTIE : Un graphique coddant le message de base

def DessinQR(tab):
    
    t=turtle.Turtle()
    
    t.penup()
    t.hideturtle()
    t.setx(-340)
    t.sety(300)
    t.speed("fastest")
    t.right(90)
    t.pendown()
    
    taillecase = ((400-30)/len(tab))
    
    t.width(8)
    t.forward(420)
    t.left(90)
    t.forward(420)
    t.left(90)
    t.forward(420)
    t.left(90)
    t.forward(420)
    t.left(180)
    t.penup()
    
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.pendown()
    
    t.width(1)
    
    for i in range(len(tab)):
        
        t.fillcolor('black')
        
        for j in range(0,8):
            
            if tab[i][j] == '1' : 
                
                t.color('black')
                t.begin_fill()
                t.forward(taillecase)
                t.left(90)
                t.forward(50)
                t.left(90)
                t.forward(taillecase)
                t.left(90)
                t.forward(50)
                t.end_fill()
                
                t.penup()
                t.left(180)
                t.forward(50)
                t.right(90)
                t.pendown()
            
            elif tab[i][j] == '0' : 
                
                t.color('white')
                t.forward(taillecase)
                t.left(90)
                t.forward(50)
                t.left(90)
                t.forward(taillecase)
                t.left(90)
                t.forward(50)
                
                t.penup()
                t.left(180)
                t.forward(50)
                t.right(90)
                t.pendown()
        
        t.color('black')
        t.penup()
        t.forward(taillecase)
        t.right(90)
        t.forward(400)
        t.left(90)
        t.pendown()
    
    t.penup()
    t.forward(30)
    t.left(90)
    t.pendown()
    
    for j in range(0,8):
        if (j%2==0):
        
            t.penup()
            t.forward(25)
            t.pendown()
            t.begin_fill()
            t.circle(10,360)
            t.end_fill()
            t.penup()
            t.forward(25)
        
        else : 
            
            t.penup()
            t.forward(50)
            t.pendown()
 
    turtle.done()
    
# FONCTION PRINCIPALE 

tabMessage = []
message = input("Saisissez un message :")

tabMessage = tabASCII(message, tabMessage) 
tabMessage = cryptage(tabMessage)
tabMessage = binaire(tabMessage)

DessinQR(tabMessage)


    
    