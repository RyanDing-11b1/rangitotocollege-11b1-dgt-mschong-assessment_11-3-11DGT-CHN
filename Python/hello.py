import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

root = tk.Tk()
root.title("GAMES COMPENDIUM")
root.geometry("1000x800") #setting window size for menu (unchangeable)
root.resizable(False, False)
root.configure(bg='#1F3B4D') #setting background color for menu

#Creating the Title of the main menu
Title = tk.Label(root, text="GAMES COMPENDIUM", font=("fixedsys 40 bold"), bg="#FAF0CA", fg="#1F3B4D", padx=40, pady=20,)
Title.grid(row=0, column=0, columnspan=3, pady=30, padx=200)

#Create Tic Tac Toe game as function
def TicTacToe():
    TicTacToe = tk.Toplevel(root)
    TicTacToe.title('TIC TAC TOE')
    
    #X starts so true
    clicked = True
    count = 0



    #disable all buttons function
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

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X": #checking if winner is present (repeated for both X and O)
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

    #button clicked function (showing either X or O)
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
            messagebox.showerror("TIC TAC TOE", "Box already selected\nPick another box") #if box already selected, error message shows)


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
    my_menu = Menu(TicTacToe)
    TicTacToe.config(menu=my_menu)

    #creating the options
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Restart", command=restart)

    restart()

    #Made using youtube tutorial by Codemy.com

#Creating the button to open Tic Tac Toe
TicTacToebutton = tk.Button(
    root, 
    text= "TIC TAC TOE",
    font="fixedsys 25 bold",
    bg="#FAF0CA",
    fg="#1F3B4D",
    borderwidth=0,
    padx=35,
    pady=50,
    command=TicTacToe #opens Tic Tac Toe game
    )

TicTacToebutton.grid(row=1, column=0, rowspan=2, pady=0, padx=10) #positioning the button


#SNAKE GAME
def Snake():
    Snake = tk.Toplevel(root)
    Snake.title('Snake Game')
    Snake.resizable(False, False)

    ROWS = 20
    COLS = 20
    TILE_SIZE = 20

    WINDOW_WIDTH = TILE_SIZE * ROWS
    WINDOW_HEIGHT = TILE_SIZE * COLS

    class Tile:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    #Creating + customizing the window
    canvas = tk.Canvas(Snake, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
    canvas.pack()
    Snake.update()

    #Code to center the window
    window_width = Snake.winfo_width()
    window_height = Snake.winfo_height()
    screen_width = Snake.winfo_screenwidth()
    screen_height = Snake.winfo_screenheight()

    window_x = int((screen_width/2) - (window_width/2))
    window_y = int((screen_height/2) - (window_height/2))

    Snake.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    #creating the game
    snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #The snake's head (one tile)
    food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
    snake_body = [] #multiple snake tiles
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0

    def change_direction(e): #e for event
        #print(e)
        #print(e.keysym)
        nonlocal velocityX, velocityY, game_over
        if (game_over):
            return

        if (e.keysym == "Up" and velocityY != 1):
            velocityX = 0
            velocityY = -1
        elif (e.keysym == "Down" and velocityY != -1):
            velocityX = 0
            velocityY = 1
        elif (e.keysym == "Left" and velocityX != 1):
            velocityX = -1
            velocityY = 0
        elif (e.keysym == "Right" and velocityX != -1):
            velocityX = 1
            velocityY = 0

    def move():
        nonlocal snake, food, snake_body, game_over, score
        if (game_over):
            return
        
        if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
            game_over = True
            return
        
        for tile in snake_body:
            if (snake.x == tile.x and snake.y == tile.y):
                game_over = True
                return

        #Snake head touching food
        if (snake.x == food.x and snake.y == food.y):
            snake_body.append(Tile(food.x, food.y))
            food.x = random.randint(0, COLS-1) * TILE_SIZE
            food.y = random.randint(0, ROWS-1) * TILE_SIZE
            score += 1

        #changing the snake body
        for i in range(len(snake_body)-1, -1, -1):
            tile = snake_body[i]
            if (i == 0):
                tile.x = snake.x
                tile.y = snake.y
            else:
                prev_tile = snake_body[i-1]
                tile.x = prev_tile.x
                tile.y = prev_tile.y

        snake.x += velocityX * TILE_SIZE
        snake.y += velocityY * TILE_SIZE
    
    def draw():
        nonlocal snake, food, snake_body, game_over, score
        move()

        canvas.delete("all")

        #drawing the food
        canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")
        
        #drawing the snake
        canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "green")

        for tile in snake_body:
            canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "green")

        if (game_over):
            canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "fixedsys 30 bold", text = f"GAME OVER: {score}", fill = "white")
        else:
            canvas.create_text(30, 20, font = "fixedsys 15", text = f"Score: {score}", fill = "white")

        Snake.after(100, draw) #redraw every 100ms (0.1 seconds)

    draw()

    Snake.bind("<KeyRelease>", change_direction)



Snakebutton = tk.Button(
    root, 
    text= "SNAKE GAME",
    font="fixedsys 25 bold",
    bg="#FAF0CA",
    fg="#1F3B4D",
    borderwidth=0,
    padx=47,
    pady=50,
    command=Snake #opens Snake game
    )

Snakebutton.grid(row=3, column=0, rowspan=2, pady=30, padx=10)

BLACKJACKbutton = tk.Button(
    root, 
    text= "BLACKJACK GAME",
    font="fixedsys 25 bold",
    bg="#FAF0CA",
    fg="#1F3B4D",
    borderwidth=0,
    padx=10,
    pady=50, #opens Blackjack game
    )

BLACKJACKbutton.grid(row=1, column=1, rowspan=2, pady=30, padx=10)

SETTINGSbutton = tk.Button(
    root, 
    text= "SETTINGS",
    font="fixedsys 25 bold",
    bg="#FAF0CA",
    fg="#1F3B4D",
    borderwidth=0,
    padx=85,
    pady=50, #opens Blackjack game
    )

SETTINGSbutton.grid(row=3, column=1, rowspan=2, pady=30, padx=10)

root.mainloop()