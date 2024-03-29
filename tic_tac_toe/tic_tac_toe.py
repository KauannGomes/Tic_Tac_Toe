from tkinter import * #type: ignore
from time import sleep


#Window-------------------------------------------
window = Tk()
window.title('Login')
window.configure(bg='#222831')
frame_info = Frame(window,bg='#FFFFFF',)
frame_btn = Frame(window,bg='#222831')
defeats = 0
wins = 0
#Func----------------------------------------------
def check_winner():
    for i in range(3):
        if btn[i][0]['text'] == btn[i][1]['text'] == btn[i][2]['text'] != '':
            return btn[i][0]['text']
        if btn[0][i]['text'] == btn[1][i]['text'] == btn[2][i]['text'] != '':
            return btn[0][i]['text']
    if btn[0][0]['text'] == btn[1][1]['text'] == btn[2][2]['text'] != '':
        return btn[0][0]['text']
    if btn[0][2]['text'] == btn[1][1]['text'] == btn[2][0]['text'] != '':
        return btn[0][2]['text']
    return None  
current_play = 'X'
def btn_exec(btn):
    
    #update play
    global current_play
    global wins
    global defeats
    if btn['text'] == '':
        btn['text'] = current_play
        current_play = "O" if current_play == "X" else "X"

    #checks victory or defeat
    win = check_winner()
    if win:
        print(f'Player {win} as win!!')
       
# Creating WidGets
btn1 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn1))
btn2 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn2))
btn3 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn3))
btn4 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn4))
btn5 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn5))
btn6 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn6))
btn7 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn7))
btn8 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn8))
btn9 = Button(frame_btn,text='',padx=50,pady=50,command=lambda: btn_exec(btn9))

btn = [[btn1, btn2, btn3],
       [btn4, btn5, btn6],
       [btn7, btn8, btn9]]

#Scoreboard
text_win = Label(frame_info,text=f'Victories: {wins}')
text_defeat = Label(frame_info,text=f'Defeats: {defeats}')


# Placing widgets on the screen
frame_btn.grid(row=0,column=0)
frame_info.grid(row=0,column=1,pady=10)

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)


text_win.grid(row=0,column=0)
text_defeat.grid(row=1,column=0)


window.mainloop()