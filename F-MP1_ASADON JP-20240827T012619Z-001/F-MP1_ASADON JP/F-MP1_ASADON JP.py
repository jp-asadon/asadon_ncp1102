from tkinter import *
import random
from PIL import ImageTk, Image

window = Tk()

ONE_CORRECT = 500.00
TWO_CORRECT = 5000.00
THREE_CORRECT = 500000.00

random_one = random.randint(0, 9)
random_two = random.randint(0, 9)
random_three = random.randint(0, 9)

frame = Frame(window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

background = ImageTk.PhotoImage(Image.open("back.jpg"))

label = Label(frame, image=background)
label.pack()


def get_result():
    if (int(txt_guess_one.get()) == random_one) and (int(txt_guess_two.get()) == random_two) and (
            int(txt_guess_three.get()) == random_three):
        lbl_prize["text"] = "   Prize: P " + str(THREE_CORRECT) + "     "
        print(THREE_CORRECT)
        lbl_guess_one["text"] = random_one
        print(random_one)
        lbl_guess_two["text"] = random_two
        print(random_two)
        lbl_guess_three["text"] = random_three
        print(random_three)
    elif (int(txt_guess_one.get()) == random_one and int(txt_guess_two.get()) == random_two) or (
            int(txt_guess_two.get()) == random_two and int(txt_guess_three.get()) == random_three) or (
            int(txt_guess_one.get()) == random_one and int(txt_guess_three.get()) == random_three):
        lbl_prize["text"] = "   Prize: P " + str(TWO_CORRECT) + "       "
        print(TWO_CORRECT)
        lbl_guess_one["text"] = random_one
        print(random_one)
        lbl_guess_two["text"] = random_two
        print(random_two)
        lbl_guess_three["text"] = random_three
        print(random_three)
    elif int(txt_guess_one.get()) == random_one or int(txt_guess_two.get()) == random_two or int(
            txt_guess_three.get()) == random_three:
        lbl_prize["text"] = "   Prize: P " + str(ONE_CORRECT) + "       "
        print(THREE_CORRECT)
        lbl_guess_one["text"] = random_one
        print(random_one)
        lbl_guess_two["text"] = random_two
        print(random_two)
        lbl_guess_three["text"] = random_three
        print(random_three)
    else:
        lbl_guess_one["text"] = random_one
        print(random_one)
        lbl_guess_two["text"] = random_two
        print(random_two)
        lbl_guess_three["text"] = random_three
        print(random_three)


def restart_game():
    random_one = random.randint(0, 9)
    random_two = random.randint(0, 9)
    random_three = random.randint(0, 9)

    def get_result():
        if (int(txt_guess_one.get()) == random_one) and (int(txt_guess_two.get()) == random_two) and (int(txt_guess_three.get()) == random_three):
            lbl_prize["text"] = "   Prize: P " + str(THREE_CORRECT) + "     "
            print(THREE_CORRECT)
            lbl_guess_one["text"] = random_one
            print(random_one)
            lbl_guess_two["text"] = random_two
            print(random_two)
            lbl_guess_three["text"] = random_three
            print(random_three)
        elif (int(txt_guess_one.get()) == random_one and int(txt_guess_two.get()) == random_two) or (
            int(txt_guess_two.get()) == random_two and int(txt_guess_three.get()) == random_three) or (
            int(txt_guess_one.get()) == random_one and int(txt_guess_three.get()) == random_three):
            lbl_prize["text"] = "   Prize: P " + str(TWO_CORRECT) + "       "
            print(TWO_CORRECT)
            lbl_guess_one["text"] = random_one
            print(random_one)
            lbl_guess_two["text"] = random_two
            print(random_two)
            lbl_guess_three["text"] = random_three
            print(random_three)
        elif int(txt_guess_one.get()) == random_one or int(txt_guess_two.get()) == random_two or int(
            txt_guess_three.get()) == random_three:
            lbl_prize["text"] = "   Prize: P " + str(ONE_CORRECT) + "       "
            print(THREE_CORRECT)
            lbl_guess_one["text"] = random_one
            print(random_one)
            lbl_guess_two["text"] = random_two
            print(random_two)
            lbl_guess_three["text"] = random_three
            print(random_three)
        else:
            lbl_guess_one["text"] = random_one
            print(random_one)
            lbl_guess_two["text"] = random_two
            print(random_two)
            lbl_guess_three["text"] = random_three
            print(random_three)


    lbl_game = Label(window, text="Guessing Game", font=("Bankgothic md bt", 20,))
    lbl_game.place(x=90, y=33)

    lbl_guess_one = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
    lbl_guess_one.place(x=133, y=88)
    lbl_guess_two = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
    lbl_guess_two.place(x=183, y=88)
    lbl_guess_three = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
    lbl_guess_three.place(x=233, y=88)

    lbl_prize = Label(window, text="    Prize: P 000.00     ", font=("Century Gothic", 12))
    lbl_prize.place(x=123, y=222)

    txt_guess_one = Entry(window, bd=2, justify="center", font=("Arial", 18))
    txt_guess_one.configure(width=3)
    txt_guess_one.place(x=120, y=128)
    txt_guess_two = Entry(window, bd=2, justify="center", font=("Arial", 18))
    txt_guess_two.configure(width=3)
    txt_guess_two.place(x=170, y=128)
    txt_guess_three = Entry(window, bd=2, justify="center", font=("Arial", 18))
    txt_guess_three.configure(width=3)
    txt_guess_three.place(x=220, y=128)

    btn_reveal = Button(window, bg="#ffef00", command=get_result, text="REVEAL", fg="black", font=("Centaur", 12))
    btn_reveal.configure(width=28)
    btn_reveal.place(x=65, y=175)

    btn_restart = Button(window, bg="#ffef00", command=restart_game, text="NEW GAME", fg="black", font=("Centaur", 12))
    btn_restart.configure(width=28)
    btn_restart.place(x=65, y=266)

lbl_game = Label(window, text="Guessing Game", font=("Bankgothic md bt", 20,))
lbl_game.place(x=90, y=33)

lbl_guess_one = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
lbl_guess_one.place(x=133, y=88)
lbl_guess_two = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
lbl_guess_two.place(x=183, y=88)
lbl_guess_three = Label(window, text="?", justify="center", fg="red", font=("Arial", 18))
lbl_guess_three.place(x=233, y=88)

lbl_prize = Label(window, text="    Prize: P 000.00     ", font=("Century Gothic", 12))
lbl_prize.place(x=123, y=222)

txt_guess_one = Entry(window, bd=2, justify="center", font=("Arial", 18))
txt_guess_one.configure(width=3)
txt_guess_one.place(x=120, y=128)
txt_guess_two = Entry(window, bd=2, justify="center", font=("Arial", 18))
txt_guess_two.configure(width=3)
txt_guess_two.place(x=170, y=128)
txt_guess_three = Entry(window, bd=2, justify="center", font=("Arial", 18))
txt_guess_three.configure(width=3)
txt_guess_three.place(x=220, y=128)

btn_reveal = Button(window, bg="#ffef00", command=get_result, text="REVEAL", fg="black", font=("Centaur", 12))
btn_reveal.configure(width=28)
btn_reveal.place(x=65, y=175)

btn_restart = Button(window, bg="#ffef00", command=restart_game, text="NEW GAME", fg="black", font=("Centaur", 12))
btn_restart.configure(width=28)
btn_restart.place(x=65, y=266)

icont = ImageTk.PhotoImage(file="dice.png")
window.iconphoto(False, icont)
window.title("Guessing Game")
window.geometry("400x400")
window.configure(bg="#CFF5E7")
window.mainloop()
