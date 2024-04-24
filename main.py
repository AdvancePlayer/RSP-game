import tkinter as tk
import random
from PIL import Image, ImageTk


bg_color = "#24272E"
fg_color = "white"

def comp_play():
    computer = random.randint(0,2)
    if computer == 0:
        comp_turn = "rock"
    elif computer == 1:
        comp_turn = "paper"
    elif computer == 2:
        comp_turn = "scissors"
    else:
        print("error in comp_play() function")
    return comp_turn

def check_winner(player_move, comp_move):
    if player_move == comp_move:
        return "It's a tie!"
    elif (player_move == "rock" and comp_move == "scissors") or (player_move == "paper" and comp_move == "rock") or (player_move == "scissors" and comp_move == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

player_sc = 0
comp_sc = 0
player_score_label = None 
comp_score_label = None
player_img_label = None
comp_img_label = None

def play(player_move):
    comp_move = comp_play()
    result = check_winner(player_move, comp_move)
    result_label.config(text=result)
    update_score(result)

    player_img_path = player_move + ".png"
    comp_img_path = comp_move + "comp" + ".png"
    player_img = Image.open("images/"+player_img_path)
    comp_img = Image.open("images/"+comp_img_path)

    player_img_tk = ImageTk.PhotoImage(player_img)
    comp_img_tk = ImageTk.PhotoImage(comp_img)

    player_img_label.config(image=player_img_tk)
    comp_img_label.config(image=comp_img_tk)

    player_img_label.image = player_img_tk
    comp_img_label.image = comp_img_tk


def update_score(result):
    global player_sc, comp_sc, player_score_label, comp_score_label

    if result == "You win!":
        player_sc += 1
    elif result == "Computer wins!":
        comp_sc += 1
    player_score_label.config(text="Player Score: " + str(player_sc))
    comp_score_label.config(text="Computer Score: " + str(comp_sc))


def offline_play():
    global player_score_label,comp_score_label,player_img_label, comp_img_label
    global result_label 


    name = name_entry.get()
    if name:
        play_window = tk.Toplevel(root)
        play_window.title("RPS Game")
        play_window.configure(bg=bg_color)
        play_window.geometry("900x600")
        play_window.iconbitmap("images/favicon.ico")
        play_window.minsize(900,600)
        
        tk.Label(play_window, text="You: "+name, font=("Helvetica", 20),fg=fg_color,bg=bg_color).place(relx=0.05,rely=0.1)
        tk.Label(play_window, text="Opponent: Computer", font=("Helvetica", 20),fg=fg_color,bg=bg_color).place(relx=0.95, rely=0.1, anchor='ne')
        player_score_label = tk.Label(play_window, text="Player Score: " + str(player_sc),fg=fg_color,bg=bg_color ,font=("Helvetica", 16))
        player_score_label.place(relx=0.05,rely=0.18)
        comp_score_label = tk.Label(play_window, text="Computer Score: " + str(comp_sc),fg=fg_color,bg=bg_color ,font=("Helvetica", 16))
        comp_score_label.place(relx=0.92, rely=0.18, anchor='ne')

        result_label = tk.Label(play_window, text="", font=("Helvetica", 16),fg=fg_color,bg=bg_color)
        result_label.place(relx=0.5, rely=0.5, anchor="center")

        player_img_label = tk.Label(play_window, bg=bg_color)
        player_img_label.place(relx=0.15, rely=0.46, anchor="center")

        comp_img_label = tk.Label(play_window, bg=bg_color)
        comp_img_label.place(relx=0.85, rely=0.46, anchor="center")


        tk.Button(play_window, font=16,text="Rock",width=15 ,bg="#FCBD6D",command=lambda: play("rock"),fg=fg_color).place(relx=0.2, rely=0.8)
        tk.Button(play_window, text="Paper", font=16,width=15,bg="#FCBD6D", command=lambda: play("paper"),fg=fg_color).place(relx=0.42,rely=0.8)
        tk.Button(play_window, text="Scissors", font=16,width=15,bg="#FCBD6D", command=lambda: play("scissors"),fg=fg_color).place(relx=0.65,rely=0.8)

        play_window.bind('<Escape>', lambda e, w=play_window: w.destroy())
        root.withdraw()
    else:
        error_label.config(text="Please enter your name", fg="red")


root = tk.Tk()
root.title("Start Game")
root.geometry('400x300')
root.resizable(False,False)
root.configure(bg=bg_color)
root.iconbitmap("images/favicon.ico")


title_label = tk.Label(root, text="Welcome to the Game!", font=("Helvetica", 24),bg=bg_color,fg=fg_color)
name_label = tk.Label(root, text="Enter your name:",font=20,bg=bg_color,fg=fg_color)
name_entry = tk.Entry(root,font=20)
name_entry.focus_set()
play_button_offline = tk.Button(root, text="Play",width=10,font=16,bg="#FCBD6D",fg=bg_color ,command=offline_play)
error_label = tk.Label(root, fg="red",bg=bg_color)

title_label.pack(padx=0,pady=10)
name_label.pack(padx=0,pady=15)
name_entry.pack(padx=0,pady=0)
play_button_offline.pack(padx=0,pady=20)
error_label.pack(padx=0,pady=0)

root.bind('<Escape>', lambda e, w=root: w.destroy())
root.bind('<Return>',lambda e: offline_play())
root.mainloop()