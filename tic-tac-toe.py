import tkinter as tk
from tkinter import messagebox, DISABLED

root = tk.Tk()
root.title('Tic-Tac-Toe')
root.iconbitmap()

# x starts so true
clicked = True
count = 0


# disable buttons


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

# check if someone won


def checkifwon():
    global winner
    winner = False

    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! X Wins!')
        disable_all_buttons()

    # CHECK IF O WON
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic-Tac-Toe', 'Congrats! O Wins!')
        disable_all_buttons()

    # check if tie
    if count == 9 and winner == False:
        messagebox.showinfo('Tic-Tac-Toe', 'You have tied!')
        disable_all_buttons()

# button click function


def b_click(b):
    global clicked, count

    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        checkifwon()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror(
            'Tic Tac Toe', 'Hey! That box has already been selected\nPick another box')

# reset


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    # buttons
    b1 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b1))
    b2 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b2))
    b3 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b3))
    b4 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b4))
    b5 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b5))
    b6 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b6))
    b7 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b7))
    b8 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b8))
    b9 = tk.Button(root, text=' ', font=('Helvetica', 20), height=3,
                   width=6, bg='SystemButtonFace', fg='black', command=lambda: b_click(b9))

    # grid buttons

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset Game', command=reset)

reset()

root.mainloop()
