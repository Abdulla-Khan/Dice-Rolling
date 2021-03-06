from tkinter import *

die = {
    0: "🎲",
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: "⚃",
    5: '⚄',
    6: '⚅',
}
app = Tk()
app.title('Dice Rolling App')
dice = Label(app, text=die[0], font=('Times', 100), foreground='black',width=2)
dice.grid(row=0, column=0, padx=25, pady=5)


def roll():
    from random import randint
    i = randint(1, 6)
    msg = Label(app, text=die[i], font=('Times', 100), foreground='black')
    msg.grid(row=0, column=0, padx=25, pady=5)


rollB = Button(app, text='Roll', command=roll)
rollB.grid(row=1, column=1)
app.mainloop()
