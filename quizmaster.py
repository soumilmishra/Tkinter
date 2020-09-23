import tkinter
from tkinter import *
import random

questions =[
    "Where is Jantar Mantar Located ?",
    "Where is Charminar located ?",
    "Where is Qutub Minar located ?",
    "Where is India Gate Located ?",
    "What is the currency of Great Britain ?",
    "What is the the capital of Australia ?",
    "What is the capital of Kerala ?",
    "What is the capital of Assam ?",
    "What is the Capital of Rajasthan ?",
    "What is the capital of India ?",
]
answers_choice =[
    ["Rajasthan","Mumbai","Delhi","Agra"],
    ["Rajasthan","Mumbai","Delhi","Hyderabad"],
    ["Rajasthan","Mumbai","Delhi","Agra"],
    ["Rajasthan","Mumbai","Delhi","Agra"],
    ["Dinar", "Yen", "Rupee", "GBP"],
    ["Sydney", "Canberra", "Melbourne", "Downtown"],
    ["Mumbai", "Cochin", "Calcutta", "Jaipur"],
    ["Mumbai", "New Delhi", "Dibrugarh", "Jaipur"],
    ["Mumbai", "New Delhi", "Calcutta", "Jaipur"],
    ["Mumbai", "New Delhi", "Calcutta", "Jaipur"],
]

answers = [2,3,2,2,3,0,1,2,3,1]

user_answer=[]
indexes = []
ques=1

def showresult(score):
    lablequestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    lblimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    lblimage.pack()
    labelresulttext = Label(
        root,
        background ="#ffffff",
        font = ("Consolas", 24 , "bold"),
        justify = "center",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="hooray.png")
        lblimage.configure(image=img)
        lblimage.image =img
        labelresulttext.configure(text="You are Excellent !!! \n Your Score is " + str(score) + " out of 25")
    elif (score >=10 and score <20):
        img = PhotoImage(file="better1.png")
        lblimage.configure(image=img)
        lblimage.image = img
        labelresulttext.configure(text="You Can Do Better !!! \n Your score is " + str(score) + " out of 25")
    else:
        img = PhotoImage(file="better1.png")
        lblimage.configure(image=img)
        lblimage.image = img
        labelresulttext.configure(text="You Can Do Better !!! \n Your score is " + str(score) + " out of 25")

def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x = x + 1
    print(score)
    showresult(score)


def selected():
    global radiovar,user_answer,indexes
    global lablequestion,r1,r2,r3,r4
    x =radiovar.get()
    radiovar.set(-1)
    user_answer.append(x)
    global ques
    if ques < 5:
        lablequestion.config(text=questions[indexes[ques]])
        r1['text']=answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques = ques + 1
    else:
        print(indexes)
        print(user_answer)
        calc()

def gen():
    global indexes
    while(len(indexes)<5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)

def startQuiz():
    global lablequestion,r1,r2,r3,r4
    lablequestion =Label(
        root,
        text = questions[indexes[0]],
        justify = "center",
        width = 500,
        wraplength =400,
        font = ("Consolas",26,"bold"),
        background = "#ffffff",
    )
    lablequestion.pack(pady=(100,30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    global r1,r2,r3,r4
    r1 = tkinter.Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times",15),
        value = 0,
        variable= radiovar,
        command =selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)
    r2 = tkinter.Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 15),
        value=1,
        variable = radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)
    r3 = tkinter.Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 15),
        value=2,
        variable = radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)
    r4 = tkinter.Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 15),
        value=3,
        variable = radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)

def isPressed():
    lableruleset.destroy()
    labelrules.destroy()
    labeltext.destroy()
    labelimage.destroy()
    labelimagebtn.destroy()
    gen()
    startQuiz()


root = tkinter.Tk()

root.title("QuizMaster")
root.geometry("800x600")
root.config(background="#ffffff")
root.resizable(height=0 , width=0)

img1 = PhotoImage(file="gradecap1.png")


labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(0,40))

img2 = PhotoImage(file="startbutton.png")

labeltext = Label(
    text = "QuizMaster",
    font = ("Comic sans MD",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,20))
labelimagebtn = Button(
    root,
    image = img2,
    border =0,
    relief = FLAT,
    background = "#ffffff",
    command = isPressed,
)
labelimagebtn.pack()

labelrules =Label(
    root,
    text = "Read the Rules \n Once Ready Press Start Button",
    font = ("Comic sans MD",16,"bold"),
    background ="#ffffff",
    justify = "center",
)
labelrules.pack(pady = (10,0))

lableruleset = Label(
    root,
    text = "There will be 10 questions \n Each question will have one correct answer \n You will get 20 seconds to select the answer",
    justify = "center",
    background="#000000",
    font = ("Consolas",14,"bold"),
    foreground = "#ffffff",
    width = 800,
)
lableruleset.pack(pady=(75,0))



root.mainloop()



