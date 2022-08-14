import os
from tkinter import *
import tkinter
import tkinter.messagebox

def course():
    board= []
    files = Liebiaokuang.curselection()
    name = Liebiaokuang.get(files)
    with open("./Record/"+ name +".txt","r") as record:
            recordlist = record.readlines()
            result = recordlist[0].strip("\n")
            for i in range(1,len(recordlist)):
                tempboard = recordlist[i].strip("\n").split(" ")
                tempboard = [x for x in tempboard if x != '']
                board.append(tempboard)
    quit2()
    printboard(board,result)

def quit():  
    searchroot2.destroy()
    readin()
    
def quit2():  
    searchroot.destroy()
     
def printboard(board:list, result:str):
    global searchroot2
    searchroot2 = Tk()
    searchroot2.title("对局详情")                         
    can = Canvas(searchroot2, width=600,height=600,background='navajowhite')
    can.pack()
    for i in range(0, 15):
        can.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
        can.create_line(20, i * 40 + 20, 580, i * 40 + 20)
    can.create_oval(135, 135, 145, 145,fill='black')
    can.create_oval(135, 455, 145, 465,fill='black')
    can.create_oval(465, 135, 455, 145,fill='black')
    can.create_oval(455, 455, 465, 465,fill='black')
    can.create_oval(295, 295, 305, 305,fill='black')
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "null":
                pass
            if board[i][j][0] == "b":
                can.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='black')
                can.create_text(40*i+20, 40*j+20, text=board[i][j][1:], fill = 'white')
            if board[i][j][0] == "w":
                can.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='white')
                can.create_text(40*i+20, 40*j+20, text=board[i][j][1:], fill = 'black')
    butt = Button(searchroot2,text="退出",command = quit, bg = "Floralwhite", font = ("宋体", 16, "bold"))
    butt.pack(fill = X)
    tkinter.messagebox.showinfo("对局结果", result)
    searchroot2.mainloop()
    
                
    
def readin():
    global searchroot, Liebiaokuang
    sum =0
    black = 0
    white = 0
    searchroot = Tk()
    scorllbar=tkinter.Scrollbar(searchroot)
    scorllbar.pack(side = RIGHT, fill = Y)
    Liebiaokuang = Listbox(searchroot, yscrollcommand=scorllbar.set)
    dir = os.listdir("./Record")
    if len(dir) == 0:
        searchroot.withdraw()
        tkinter.messagebox.showinfo("提示", "没有对局记录！")
        searchroot.destroy()
    else:
        for files in os.listdir("./Record"):
            sum += 1
            Liebiaokuang.insert(tkinter.END, files[:-4])  
            with open("./Record/"+ files,"r") as record:
                recordlist = record.readlines()
                result = recordlist[0].strip("\n")
                if result[0] == "玩" or result[0] == "黑": black += 1
                else: white +=1
        label = Label(searchroot,text = "对局次数：{0}\n 黑方胜率：{1:.2f}%\n 白方胜率：{2:.2f}%".format(sum,(black/sum)*100,(white/sum)*100),font = ("宋体", 10, "bold"))  
        label.pack()      
        Liebiaokuang.pack()
        b = Button(searchroot, text="查询", command = course, bg = "navajowhite")
        b.pack(fill= X)
        b2 = Button(searchroot, text="退出", command = quit2, bg = "navajowhite")
        b2.pack(fill= X)
    searchroot.mainloop()
    
    