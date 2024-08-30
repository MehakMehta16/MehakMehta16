from tkinter import *
from tkinter import messagebox

PlayerA = "X"
stop_game = False

states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

def clicked(r, c):
    global PlayerA, stop_game
    if states[r][c]==0 and not stop_game: 
        b[r][c].configure(text=PlayerA)
        states[r][c]=PlayerA
        PlayerA="O" if PlayerA=="X" else "X"
        check_if_win()

def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            stop_game=True
            messagebox.showinfo("Winner", states[i][0] + " won")
            return
        elif states[0][i]==states[1][i]==states[2][i] != 0:
            messagebox.showinfo("Winner", states[0][i] + " won")
            return
        
    if states[0][0]==states[1][1]==states[2][2]!=0:  
        stop_game=True
        messagebox.showinfo("Winner", states[0][0] + " won")
        return
    elif states[0][2]==states[1][1]==states[2][0]!=0:  
        stop_game=True
        messagebox.showinfo("Winner", states[0][2] + " won")
        return


    if all(states[i][j]!=0 for i in range(3) for j in range(3)):
        stop_game=True
        messagebox.showinfo("Draw", "It's a draw!")
        return

root = Tk()
root.title("TIC TAC TOE")
root.resizable(0, 0)

b=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(height=4, width=8, font=("Cambria", "20"), command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

root.mainloop()
