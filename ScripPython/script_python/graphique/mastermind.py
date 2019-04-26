from tkinter import *
from random import *

numCanvas=0


def changeButtonColor(canvas,color):
    global combinaisonBool
    # print(numCanvas)
    i =0
    while(combinaisonBool[i]):
        print(i)
        i+=1
    canvas[i].create_rectangle(0,0,90,60,fill=color)
    combinaisonBool[i]=True
    # numCanvas+=1




Mafenetre=Tk()
Mafenetre.geometry("1200x800")
Mafenetre.title('MASTERMIND!')


newGameButton = Button(Mafenetre,text="Nouvelle partie",bg="ghost white")
newGameButton.pack(side=LEFT, padx=5,pady=5)
newGameButton.place(x=10,y=670)

quitterButton = Button(Mafenetre,text="Quitter",bg="orange red",command=Mafenetre.destroy)
quitterButton.pack(side=LEFT, padx=5,pady=5)
quitterButton.place(x=10,y=720)

validerButton = Button(Mafenetre,text="Valider",bg="spring green")
validerButton.pack(side=LEFT, padx=5, pady=5)
validerButton.place(x=1000, y=720)

annulerButton = Button(Mafenetre,text="Annuler",bg="orange red")
annulerButton.pack(side=LEFT, padx=5,pady=5)
annulerButton.place(x=1100,y=720)



# Combinaison 

combinaisonx=350
combinaisony=670

# choix1Canvas = Canvas(Mafenetre,bg="snow", height=60,width=90)
# choix1Canvas.pack(side=LEFT, padx=5,pady=5)
# choix1Canvas.place(x=combinaisonx,y=combinaisony)

# choix2Canvas = Canvas(Mafenetre,bg="snow", height=60,width=90)
# choix2Canvas.pack(side=LEFT, padx=5,pady=5)
# choix2Canvas.place(x=combinaisonx+100,y=combinaisony)

# choix3Canvas = Canvas(Mafenetre,bg="snow", height=60,width=90)
# choix3Canvas.pack(side=LEFT, padx=5,pady=5)
# choix3Canvas.place(x=combinaisonx+200,y=combinaisony)

# choix4Canvas = Canvas(Mafenetre,bg="snow", height=60,width=90)
# choix4Canvas.pack(side=LEFT, padx=5,pady=5)
# choix4Canvas.place(x=combinaisonx+300,y=combinaisony)

combinaisonBool=[True for i in range(0,4,1)]
combinaison=[Canvas(Mafenetre,bg="snow", height=60,width=90) for i in range(0,4,1)]
for i in range(0,4,1):
    combinaison[i].pack(side=LEFT,padx=5,pady=5)
    combinaison[i].place(x=combinaisonx+i*100,y=combinaisony)



palettex=1000
palettey=250

colors=["medium blue","lime green","firebrick1","orange","dark orchid","yellow"]

colorButton=[Button(Mafenetre,bg=colors[i], height=3,width=7,activebackground=colors[i],command= lambda: changeButtonColor(combinaison,colors[i])) for i in range(0,6,1)]
for i in range(0,6,2):
    colorButton[i].pack(side=LEFT, padx=5,pady=5)
    colorButton[i].place(x=palettex,y=palettey+i/2*80)

    colorButton[i+1].pack(side=LEFT, padx=5,pady=5)
    colorButton[i+1].place(x=palettex+100,y=palettey+i/2*80)

# blueButton = Button(Mafenetre,bg="medium blue", height=3,width=7,activebackground="medium blue", command= lambda: changeButtonColor(choix1Canvas,"medium blue"))
# blueButton.pack(side=LEFT, padx=5,pady=5)
# blueButton.place(x=palettex,y=palettey)

# greenButton = Button(Mafenetre,bg="lime green", height=3,width=7,activebackground="lime green")
# greenButton.pack(side=LEFT, padx=5,pady=5)
# greenButton.place(x=palettex+100,y=palettey)

# redButton = Button(Mafenetre,bg="firebrick1", height=3,width=7,activebackground="firebrick1")
# redButton.pack(side=LEFT, padx=5,pady=5)
# redButton.place(x=palettex,y=palettey+80)

# orangeButton = Button(Mafenetre,bg="orange", height=3,width=7,activebackground="orange")
# orangeButton.pack(side=LEFT, padx=5,pady=5)
# orangeButton.place(x=palettex+100,y=palettey+80)

# violetButton = Button(Mafenetre,bg="dark orchid", height=3,width=7,activebackground="dark orchid")
# violetButton.pack(side=LEFT, padx=5,pady=5)
# violetButton.place(x=palettex,y=palettey+160)

# jauneButton = Button(Mafenetre,bg="yellow", height=3,width=7,activebackground="yellow")
# jauneButton.pack(side=LEFT, padx=5,pady=5)
# jauneButton.place(x=palettex+100,y=palettey+160)





Mafenetre.mainloop()
