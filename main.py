from tkinter import *
import NashEqMixte

root = Tk()
root.config(background="#181D31")
root.geometry("1080x600")
root.minsize(1080, 600)
root.title("Rock Paper Scissor Lizard Spock Game")

# Computer Value
computer_value = {"0": "Rock","1": "Paper","2": "Scissor","3": "Lizard","4": "Spock"}
score_ad = 0
score_j = 0
#------------------------------------------------------------------------------#




def update_score():
    global score_ad
    global score_j

    print("Player ", score_j)
    print("Computer ", score_ad)
    print()

    lp.config(text="Player Score - " + str(score_j) + "\t")
    lc.config(text="Computer Score - " + str(score_ad))



def reset_jeu():
    global score_ad
    global score_j
    l1.config(text="Player\t")
    l3.config(text="Computer")
    l4.config(text="")
    score_ad = 0
    score_j = 0

    lp.config(text="Player Score - " + str(score_j) + "\t")
    lc.config(text="Computer Score - " + str(score_ad))
def inc_score(c):
    global score_ad
    global score_j
    if c:
        score_ad = score_ad + 1
    else:
        score_j = score_j + 1


# Si le joueur choisit Pierre
def Rock():
    c_v = NashEqMixte.ChoixStrat()
    col = "black"
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Paper":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Lizard":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"

    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Rock\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Si le joueur choisit feuille
def Paper():
    c_v = NashEqMixte.ChoixStrat()
    col = "black"
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Rock":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Lizard":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    else:
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Paper\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Si le joueur choisit ciseaux
def Scissor():
    c_v = NashEqMixte.ChoixStrat()
    col = "black"
    if c_v == "Scissor":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Rock":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Lizard":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Scissor\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Si le joueur choisit lézard
def Lizard():
    c_v = NashEqMixte.ChoixStrat()
    col = "black"
    if c_v == "Lizard":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Rock":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Scissor":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    else:
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Lizard\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Si le joueur choisit spock
def Spock():
    c_v = NashEqMixte.ChoixStrat()
    col = "black"
    if c_v == "Spock":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Rock":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Scissor":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Spock\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Ajouter des labels et les boutons 
Label(root,
      text="Rock Paper Scissor Lizard Spock",
      font="normal 25 bold",
      fg="white", bg="#181D31").pack(pady=20)

frame = Frame(root, bg="#181D31")
frame.pack()

l1 = Label(frame,
           text="   Player\t", fg="#78ABC2",
           font="normal 25 bold", bg="#181D31")

l2 = Label(frame,
           text="  VS     ",
           font="normal 20 bold", bg="#181D31")

l3 = Label(frame, text="Computer", fg="#4B718E", font="normal 25 bold", bg="#181D31")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="#181D31",
           width=15,
           borderwidth=0,
           relief="solid")
l4.pack(pady=20)

frame1 = Frame(root, bg="#181D31")
frame1.pack()

ro = PhotoImage(file="images/rock.png")
ro = ro.subsample(3, 3)

pa = PhotoImage(file="images/paper.png")
pa = pa.subsample(3, 3)

sc = PhotoImage(file="images/scissor.png")
sc = sc.subsample(3, 3)

li = PhotoImage(file="images/lizard.png")
li = li.subsample(3, 3)

sp = PhotoImage(file="images/spock.png")
sp = sp.subsample(3, 3)

b1 = Button(frame1, text="Rock",fg="#78ABC2", image=ro, borderwidth= 0,
            font=10,
            command=Rock, compound=TOP, bg="#181D31")

b2 = Button(frame1, text="Paper ",fg="#78ABC2", image=pa,borderwidth= 0,
            font=10,
            command=Paper, compound=TOP, bg="#181D31")

b3 = Button(frame1, text="Scissor",fg="#78ABC2", image=sc,borderwidth= 0,
            font=10,
            command=Scissor, compound=TOP, bg="#181D31")

b4 = Button(frame1, text="Lizard",fg="#78ABC2", image=li,borderwidth= 0,
            font=10,
            command=Lizard, compound=TOP, bg="#181D31")

b5 = Button(frame1, text="Spock",fg="#78ABC2", image=sp,borderwidth= 0,
            font=10,
            command=Spock, compound=TOP, bg="#181D31")


b1.pack(side=LEFT, padx=10)

b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
b5.pack(padx=10)

Button(root, text="Reset Game",
       font=10, fg="white",
       bg="#78ABC2", command=reset_jeu).pack(pady=20)

frame2 = Frame(root)
frame2.pack()
lp = Label(frame2,
           text="Player Score - " + str(score_j) + "\t",
           font="normal 15 bold", fg="green", bg="#181D31")

lc = Label(frame2,
           text="Computer Score - " + str(score_ad),
           font="normal 15 bold", fg="red", bg="#181D31")
lp.pack(side=LEFT)
lc.pack(side=LEFT)
# Executer Tkinter
root.mainloop()
