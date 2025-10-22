import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("GAMES COMPENDIUM")
root.geometry("1000x800")
root.resizable(False, False)
root.configure(bg='#1F3B4D')

Title = tk.Label(root, text="GAMES COMPENDIUM", font=("fixedsys 40 bold"), bg="#FAF0CA", fg="#1F3B4D", padx=40, pady=20,)
Title.grid(row=0, column=0, columnspan=3, pady=30, padx=200)

def TicTacToe():
    TicTacToe = tk.Toplevel(root)
    TicTacToe.title('TIC TAC TOE')
    
    #X starts so true
    clicked = True
    count = 0



    #disable all buttons
    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    #checking if winner is present
    def checkwinner():
        global winner
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="lightgreen")
            b2.config(bg="lightgreen")
            b3.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b6.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="lightgreen")
            b8.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="lightgreen")
            b4.config(bg="lightgreen")
            b7.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b8.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="lightgreen")
            b6.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b7.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "X wins!")
            disable_all_buttons()

        #### X DONE, CHECKING FOR O
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="lightgreen")
            b2.config(bg="lightgreen")
            b3.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b6.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="lightgreen")
            b8.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="lightgreen")
            b4.config(bg="lightgreen")
            b7.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b8.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="lightgreen")
            b6.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b9.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="lightgreen")
            b5.config(bg="lightgreen")
            b7.config(bg="lightgreen")
            winner = True
            messagebox.showinfo("TIC TAC TOE", "O wins!")
            disable_all_buttons()

    #button clicked function
    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkwinner()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkwinner()
        else:
            messagebox.showerror("TIC TAC TOE", "Box already selected\nPick another box")


    #restarting game function
    def restart():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count
        clicked = True
        count = 0

        #creating buttons + customizing them
        b1 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
        b2 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
        b3 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

        b4 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
        b5 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
        b6 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

        b7 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
        b8 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
        b9 = Button(TicTacToe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

        #making grid for buttons
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)


    #create menu for start/reset button
    my_menu = Menu(root)
    root.config(menu=my_menu)

    #creating the options
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Restart", command=restart)

    restart()

    #Made using youtube tutorial by Codemy.com

TicTacToebutton = tk.Button(
    root, 
    text= "TIC TAC TOE",
    font="fixedsys 25 bold",
    bg="#FAF0CA",
    fg="#1F3B4D",
    borderwidth=0,
    padx=35,
    pady=50,
    command=TicTacToe
    )

TicTacToebutton.grid(row=1, column=0, rowspan=2, pady=0, padx=10)

root.mainloop()