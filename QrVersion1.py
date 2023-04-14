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
    
    t  = turtle.Turtle()
    ts = turtle.Screen()
    
    t.pensize(1)
    m=math
    t.penup()
    t.hideturtle()
    t.setx(-750)
    t.sety(250)
    t.speed(0)
    t.right(90)
    t.pendown()
    
    compteur = 0
    longueur = len(tab)
    
    if (len(tab)<50):
        
        t.begin_fill()
        t.forward(235)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(240)
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
        t.forward(415)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(485)
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
        
        for j in range(0,4):
            
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
        
        
        for j in range(4,8):
            
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
        t.forward(225)
        t.right(180)
        t.pendown()
        
        compteur += 1 ;
        
        
        if (longueur > 50):
            
            if (compteur== m.ceil(longueur/2)) :
                t.penup()
                t.forward(245)
                t.right(90)
                t.forward(m.ceil(longueur/2)*15)
                t.left(90)
                t.pendown() 
                compteur = 0
                
    if (longueur%2!=0) and (longueur >= 50):
        
        t.penup()
        t.forward(235)
        t.pendown()
        
        
        t.color("black")
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(240)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(240)
        t.penup()
   
    ts.mainloop()
    ts.exitonclick()
    
# FONCTION PRINCIPALE 

tabMessage = []
message = input("Saisissez un message :")

tabMessage = tabASCII(message, tabMessage) 
tabMessage = cryptage(tabMessage)
tabMessage = binaire(tabMessage)

DessinQR(tabMessage)


    
    