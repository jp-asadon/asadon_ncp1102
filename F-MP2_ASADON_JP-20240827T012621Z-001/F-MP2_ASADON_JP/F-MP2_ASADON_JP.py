from tkinter import *
import random
from PIL import ImageTk, Image
import customtkinter
from tkinter import messagebox

window = Tk()

rock_show = ImageTk.PhotoImage(Image.open("rock.png").resize((70, 70), Image.Resampling.LANCZOS))
paper_show = ImageTk.PhotoImage(Image.open("paper.png").resize((70, 70), Image.Resampling.LANCZOS))
scissor_show = ImageTk.PhotoImage(Image.open("scissor.png").resize((70, 70), Image.Resampling.LANCZOS))
title = ImageTk.PhotoImage(Image.open("title.png").resize((260, 55), Image.Resampling.LANCZOS))
computer = ImageTk.PhotoImage(Image.open("computer.png").resize((70, 70), Image.Resampling.LANCZOS))
congrats = ImageTk.PhotoImage(Image.open("congrats.png").resize((250, 60), Image.Resampling.LANCZOS))
lost = ImageTk.PhotoImage(Image.open("lost.png").resize((250, 60), Image.Resampling.LANCZOS))
draw = ImageTk.PhotoImage(Image.open("draw.png").resize((250, 60), Image.Resampling.LANCZOS))
guess = ImageTk.PhotoImage(Image.open("guess.png").resize((70, 70), Image.Resampling.LANCZOS))

frame = Frame(window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

background = ImageTk.PhotoImage(Image.open("background.jpg").resize((450, 460), Image.Resampling.LANCZOS))

label = Label(frame, image=background)
label.pack()


lbl_computer_img = Label(window, image=computer)
lbl_computer_img.place(x=77, y=80)

lbl_guess = Label(window, image=guess)
lbl_guess.place(x=253, y=80)

lbl_title = Label(window, image=title)
lbl_title.place(x=60, y=8)

number = random.randint(1, 3)

def restart_game():
    frame = Frame(window, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(frame, image=background)
    label.pack()

    lbl_computer_img = Label(window, image=computer)
    lbl_computer_img.place(x=77, y=80)

    lbl_guess = Label(window, image=guess)
    lbl_guess.place(x=253, y=80)

    lbl_title = Label(window, image=title)
    lbl_title.place(x=60, y=8)


    rock_show = ImageTk.PhotoImage(Image.open("rock.png").resize((70, 70), Image.Resampling.LANCZOS))
    paper_show = ImageTk.PhotoImage(Image.open("paper.png").resize((70, 70), Image.Resampling.LANCZOS))
    scissor_show = ImageTk.PhotoImage(Image.open("scissor.png").resize((70, 70), Image.Resampling.LANCZOS))

    number = random.randint(1,3)

    lbl_game = Label(window, text=number, font=("Arial", 20))
    lbl_game.place(x=30, y=250)

    def show_rock():
        lbl_rock_show = Label(window, image=rock_show)
        lbl_rock_show.place(x=253, y=80)
        if number == 3:
            lbl_computer_img["image"] = scissor_show
            lbl_result = Label(window, image=congrats)
            lbl_result.place(x=73, y=392)
        elif number == 2:
            lbl_computer_img["image"] = paper_show
            lbl_result = Label(window, image=lost)
            lbl_result.place(x=73, y=392)
        else:
            lbl_computer_img["image"] = rock_show
            lbl_result = Label(window, image=draw)
            lbl_result.place(x=73, y=392)

    def show_paper():
        lbl_paper_show = Label(window, image=paper_show)
        lbl_paper_show.place(x=253, y=80)
        if number == 1:
            lbl_computer_img["image"] = rock_show
            lbl_result = Label(window, image=congrats)
            lbl_result.place(x=73, y=392)
        elif number == 3:
            lbl_computer_img["image"] = scissor_show
            lbl_result = Label(window, image=lost)
            lbl_result.place(x=73, y=392)
        else:
            lbl_computer_img["image"] = paper_show
            lbl_result = Label(window, image=draw)
            lbl_result.place(x=73, y=392)

    def show_scissor():
        lbl_scissor_show = Label(window, image=scissor_show)
        lbl_scissor_show.place(x=253, y=80)
        if number == 2:
            lbl_computer_img["image"] = paper_show
            lbl_result = Label(window, image=congrats)
            lbl_result.place(x=73, y=392)
        elif number == 1:
            lbl_computer_img["image"] = rock_show
            lbl_result = Label(window, image=lost)
            lbl_result.place(x=73, y=392)
        else:
            lbl_computer_img["image"] = scissor_show
            lbl_result = Label(window, image=draw)
            lbl_result.place(x=73, y=392)

    def exit_game():
        messagebox.showinfo("Quit?", "Are you sure you want to exit?")
        window.quit()

    lbl_computer = Label(window, text="Computer", font=("Tahoma", 14))
    lbl_computer.place(x=70, y=160)
    lbl_player = Label(window, text=" Player ", font=("Tahoma", 14))
    lbl_player.place(x=258, y=160)

    rock = ImageTk.PhotoImage(Image.open("rock.png").resize((30, 30), Image.Resampling.LANCZOS))
    paper = ImageTk.PhotoImage(Image.open("paper.png").resize((30, 30), Image.Resampling.LANCZOS))
    scissor = ImageTk.PhotoImage(Image.open("scissor.png").resize((30, 30), Image.Resampling.LANCZOS))

    btn_rock = customtkinter.CTkButton(master=window, image=rock, text="ROCK     ", command=show_rock, width=190,
                                       height=40, compound="right")
    btn_rock.pack(pady=5, padx=20)
    btn_rock.place(x=100, y=200)

    btn_paper = customtkinter.CTkButton(master=window, image=paper, text="PAPER    ", command=show_paper, width=190,
                                        height=40, compound="right", fg_color="#C77C78", hover_color="#D35B58")
    btn_paper.pack(pady=5, padx=20)
    btn_paper.place(x=100, y=250)

    btn_scissor = customtkinter.CTkButton(master=window, image=scissor, text="SCISSOR", command=show_scissor, width=190,
                                          height=40, compound="right", fg_color="#b1995f", hover_color="#76663f")
    btn_scissor.pack(pady=5, padx=20)
    btn_scissor.place(x=100, y=300)

    btn_new_game = Button(window, bg="#4CBB17", command=restart_game, text="NEW GAME", fg="white", font=("Centaur", 12), width=15)
    btn_new_game.place(x=50, y=352)

    btn_exit = Button(window, bg="#EE4B2B", command=exit_game, text="EXIT", fg="white", font=("Centaur", 12), width=15)
    btn_exit.place(x=210, y=352)


lbl_game = Label(window, text=number, font=("Arial", 20))
lbl_game.place(x=30, y=250)

def show_rock():
    lbl_rock_show = Label(window, image=rock_show)
    lbl_rock_show.place(x=253, y=80)
    if number == 3:
        lbl_computer_img["image"] = scissor_show
        lbl_result = Label(window, image=congrats)
        lbl_result.place(x=73, y=392)
    elif number == 2:
        lbl_computer_img["image"] = paper_show
        lbl_result = Label(window, image=lost)
        lbl_result.place(x=73, y=392)
    else:
        lbl_computer_img["image"] = rock_show
        lbl_result = Label(window, image=draw)
        lbl_result.place(x=73, y=392)


def show_paper():
    lbl_paper_show = Label(window, image=paper_show)
    lbl_paper_show.place(x=253, y=80)
    if number == 1:
        lbl_computer_img["image"] = rock_show
        lbl_result = Label(window, image=congrats)
        lbl_result.place(x=73, y=392)
    elif number == 3:
        lbl_computer_img["image"] = scissor_show
        lbl_result = Label(window, image=lost)
        lbl_result.place(x=73, y=392)
    else:
        lbl_computer_img["image"] = paper_show
        lbl_result = Label(window, image=draw)
        lbl_result.place(x=73, y=392)


def show_scissor():
    lbl_scissor_show = Label(window, image=scissor_show)
    lbl_scissor_show.place(x=253, y=80)
    if number == 2:
        lbl_computer_img["image"] = paper_show
        lbl_result = Label(window, image=congrats)
        lbl_result.place(x=73, y=392)
    elif number == 1:
        lbl_computer_img["image"] = rock_show
        lbl_result = Label(window, image=lost)
        lbl_result.place(x=73, y=392)
    else:
        lbl_computer_img["image"] = scissor_show
        lbl_result = Label(window, image=draw)
        lbl_result.place(x=73, y=392)


def exit_game():
    messagebox.showinfo("Quit?", "Are you sure you want to exit?")
    window.quit()

lbl_computer = Label(window, text="Computer", font=("Tahoma", 14))
lbl_computer.place(x=70, y=160)

lbl_player = Label(window, text=" Player ", font=("Tahoma", 14))
lbl_player.place(x=258, y=160)


rock = ImageTk.PhotoImage(Image.open("rock.png").resize((30, 30), Image.Resampling.LANCZOS))
paper = ImageTk.PhotoImage(Image.open("paper.png").resize((30, 30), Image.Resampling.LANCZOS))
scissor = ImageTk.PhotoImage(Image.open("scissor.png").resize((30, 30), Image.Resampling.LANCZOS))

btn_rock = customtkinter.CTkButton(master=window, image=rock, text="ROCK     ", command=show_rock, width=190, height=40, compound="right")
btn_rock.pack(pady=5, padx=20)
btn_rock.place(x=100, y=200)

btn_paper = customtkinter.CTkButton(master=window, image=paper, text="PAPER    ", command=show_paper, width=190,
                                    height=40, compound="right", fg_color="#C77C78", hover_color="#D35B58")
btn_paper.pack(pady=5, padx=20)
btn_paper.place(x=100, y=250)

btn_scissor = customtkinter.CTkButton(master=window, image=scissor, text="SCISSOR", command=show_scissor, width=190,
                                      height=40, compound="right", fg_color="#b1995f", hover_color="#76663f")
btn_scissor.pack(pady=5, padx=20)
btn_scissor.place(x=100, y=300)

btn_new_game = Button(window, bg="#4CBB17", command=restart_game, text="NEW GAME", fg="white", font=("Centaur", 12),
                      width=15)
btn_new_game.place(x=50, y=352)

btn_exit = Button(window, bg="#EE4B2B", command=exit_game, text="EXIT", fg="white", font=("Centaur", 12), width=15)
btn_exit.place(x=210, y=352)

icont = ImageTk.PhotoImage(file="icon.png")
window.iconphoto(False, icont)
window.title("Jack en Poy")
window.geometry("400x465")
window.resizable(0,0)
window.mainloop()
