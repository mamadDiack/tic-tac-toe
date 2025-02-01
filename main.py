from tkinter import *

# Variables globales
buttons = []
game_over = False
current_player = "X"
frame = None  # Déclarer frame comme variable globale

# Afficher le gagnant
def print_winner():
    global game_over
    if not game_over:
        game_over = True
        print(f"Le joueur {current_player} a gagné")
        stat = 0
        restart(stat)

# Faire une nouvelle partie ou quitter
def restart(stat):
    global frame  # Utiliser la variable globale frame
    frame = Frame(root, background="blue")
    champ = Entry(frame, background="blue")
    champ.grid(row=0, column=0, columnspan=2)  # Spanning two columns
    champ.delete(0, END)
    if stat == 0:
        champ.insert(END, f"Le joueur {current_player} a gagné")
    else:
        champ.insert(END, "Match nul")

    button_restart = Button(frame, text="Nouvelle Partie", bg="green", command=relancer_code)
    button_quit = Button(frame, text="Quitter", bg="red", command=root.quit)
    button_restart.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
    frame.grid(row=1, column=0, columnspan=3)  # Spanning three columns

# Redémarrer le jeu
def relancer_code():
    global game_over, current_player, buttons, frame
    game_over = False
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="")
    if frame:  # Masquer la frame si elle existe
        frame.grid_forget()

# Vérifier s'il y a match nul
def check_nul():
    if not game_over:
        count = 0
        for row in range(3):
            for column in range(3):
                current_button = buttons[row][column]
                if current_button['text'] == "X" or current_button['text'] == "O":
                    count += 1

        if count == 9:
            print("Match nul")
            stat = 1
            restart(stat)

# Changer de joueur
def switch_players():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Détection de victoire
def check_win(clicked_row, clicked_col):
    # Vérification des lignes et colonnes
    if all(buttons[clicked_row][i]['text'] == current_player for i in range(3)) or \
       all(buttons[i][clicked_col]['text'] == current_player for i in range(3)):
        print_winner()
    # Vérification des diagonales
    if clicked_row == clicked_col and all(buttons[i][i]['text'] == current_player for i in range(3)):
        print_winner()
    if clicked_row + clicked_col == 2 and all(buttons[i][2 - i]['text'] == current_player for i in range(3)):
        print_winner()

# Placer les symboles
def place_symbol(row, column):
    clicked_button = buttons[row][column]
    if clicked_button['text'] == "" and not game_over:
        clicked_button.config(text=current_player)
        check_win(row, column)
        check_nul()
        switch_players()

# Création du tableau de grille
def draw_grid():
    for row in range(3):
        button_in_cols = []
        for column in range(3):
            button = Button(
                root, font=("Arial", "19"), text="",
                width=15, height=5,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            button_in_cols.append(button)
        buttons.append(button_in_cols)

# Création de la fenêtre
root = Tk()
root.title("Tic Tac Toe")
root.minsize(500, 500)
draw_grid()
root.mainloop()