
import socket
import tkinter
from tkinter import *
import tkinter.messagebox
import numpy as np
import datetime

def c():
    global pre,server
    ip = e.get()
    duankou = e2.get()
    server = socket.socket()
    server.bind((ip,int(duankou)))
    server.listen(3)
    tkinter.messagebox.showinfo("提示","等待连接中...")
    pre, addr = server.accept()
    tkinter.messagebox.showinfo("提示","连接成功！")
    createboard(1)
    onlineroot.destroy()

  
def c2():
    global client
    ip = e.get()
    duankou = e2.get()
    client = socket.socket() 
    client.connect((ip,int(duankou))) 
    tkinter.messagebox.showinfo("提示","连接成功！")
    createboard(0)
    onlineroot.destroy()

def winlose(i,j,pvproot,B):
    f = [[-1, 0], [-1, 1], [0, 1], [1, 1]]
    for z in range(0, 4):
        a, b = f[z][0], f[z][1]
        count1, count2 = 0, 0
        x, y = i, j
        while B[x][y][0] == B[i][j][0]:
            count1 += 1
            if x + a >= 0 and y + b >= 0 and x + a < 15 and y + b < 15 and B[x + a][y + b][0] == B[i][j][0]:
                [x, y] = np.array([x, y]) + np.array([a, b])
            else:
                x, y = i, j
                break
        while B[x][y][0] == B[i][j][0]:
            count2 += 1
            if x - a < 15 and y - b < 15 and x - a >= 0 and y - b >= 0 and B[x - a][y - b][0] == B[i][j][0]:
                [x, y] = np.array([x, y]) - np.array([a, b])
            else:
                break
        if count1 + count2 == 6:
            C = B.tolist()
            d = datetime.datetime.now()
            if B[i][j][0] == "b":   
                with open("./Record/{data}.txt".format(data = d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
                    txt.write("黑胜\n")
                    for items in C:
                        for item in items:
                            txt.write(item + " ")
                        txt.write("\n")
                tkinter.messagebox.showinfo('提示', '黑棋获胜')
                pvproot.destroy()
            else:
                with open("./Record/{data}.txt".format(data = d.strftime("%Y-%m-%d-%H-%M-%S")), "w") as txt:
                    txt.write("白胜\n")
                    for items in C:
                        for item in items:
                            txt.write(item + " ")
                        txt.write("\n")               
                tkinter.messagebox.showinfo('提示', '白棋获胜')
                pvproot.destroy()

def callback1(event):
    global num,down,i,j,sent
    if down == 0:
        return
    else:
        for j in range (0,15):
            for i in range (0,15):
                if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                    break
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2*20 ** 2:
                break
        if A[i][j] != 1:
            down = 0
            w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='black')
            w1.create_text(40*i+20, 40*j+20, text=num, fill ='white' )
            A[i][j] = 1
            t= "b" + str(num)
            B[i][j] = t
            
            num += 2
            send_data = str(i) +"," + str(j)
            pre.send(send_data.encode())
            winlose(i,j,pvproot,B)
            sent.set("现在轮到白方落子" )  
            pvproot.update()
            data = pre.recv(1024)
            down = 1
            data = data.decode()
            if "," in data:
                i,j = data.split(",")
                i = int(i)
                j = int(j)
                w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='white')
                w1.create_text(40*i+20, 40*j+20, text=num-1, fill ='black' )
                A[i][j] = 1
                t= "w" + str(num-1)
                B[i][j] = t
                winlose(i,j,pvproot,B)
                down = 1      
            else:
                quit()
            
            
def callback2(event):
    global num,down,i,j,sent
    if down == 0:
        return
    elif down==1:  
        for j in range (0,15):
            for i in range (0,15):
                if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2 * 20 ** 2:
                    break
            if (event.x - 20 - 40 * i) ** 2 + (event.y - 20 - 40 * j) ** 2 <= 2*20 ** 2:
                break
        if A[i][j] != 1:
            down = 0
            w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='white')
            w1.create_text(40*i+20, 40*j+20, text=num, fill = 'black')
            A[i][j] = 1
            t= "w" + str(num)
            B[i][j] = t
            num += 2
            winlose(i,j,pvproot,B)
            send_data = str(i) +"," + str(j)
            client.send(send_data.encode())
            sent.set("现在轮到黑方落子" )  
            pvproot.update()
            
        data = client.recv(1024)
        down = 1
        data = data.decode()
        if "," in data:
            i,j = data.split(",")
            i = int(i)
            j = int(j)
            w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='black')
            w1.create_text(40*i+20, 40*j+20, text=num-1, fill = 'white')
            A[i][j] = 1
            t= "b" + str(num-1)
            B[i][j] = t     
            winlose(i,j,pvproot,B)
        else:
            tkinter.messagebox.showinfo("提示","对方已退出") 
            quit()
    elif down== -1:  
        data = client.recv(1024)
        down = 1
        data = data.decode()
        if "," in data:
            i,j = data.split(",")
            i = int(i)
            j = int(j)
            w1.create_oval(40*i+5, 40*j+5, 40*i+35, 40*j+35,fill='black')
            w1.create_text(40*i+20, 40*j+20, text=num-1, fill = 'white')
            A[i][j] = 1
            t= "b" + str(num-1)
            B[i][j] = t     
            winlose(i,j,pvproot,B)
        else:
            tkinter.messagebox.showinfo("提示","对方已退出") 
            quit()
   
    

def quit():
    senddata = "quit"
    try:
        pre.send(senddata.encode())
        pre.close()
        server.close()
    except:
        client.send(senddata.encode())
        client.close()
    pvproot.destroy()

def createboard(info):  
    global down,pvproot,A,B,num,w1,sent
    sent = StringVar()
    sent.set("现在轮到黑方落子")
    num = 0
    A = np.full((15,15),0)
    B = np.full((15,15),"null")
    pvproot = Tk()#创建窗口
    pvproot.title("欢乐五子棋")                        
    l3 = Label(pvproot,textvariable=sent ,font=('楷体',15))
    l3.pack()
    w1 = Canvas(pvproot, width=600,height=600,background='navajowhite')
    w1.pack()
    for i in range(0, 15):
        w1.create_line(i * 40 + 20, 20, i * 40 + 20, 580)
        w1.create_line(20, i * 40 + 20, 580, i * 40 + 20)
    w1.create_oval(135, 135, 145, 145,fill='black')
    w1.create_oval(135, 455, 145, 465,fill='black')
    w1.create_oval(465, 135, 455, 145,fill='black')
    w1.create_oval(455, 455, 465, 465,fill='black')
    w1.create_oval(295, 295, 305, 305,fill='black')
    if info == 1: 
        tkinter.messagebox.showinfo("提示","你是黑方，先下")
        down = 1
        w1.bind("<Button -1>",callback1) 
        u=Button(pvproot,text="退出游戏",width=10,height=1,command= quit,font=('楷体',15), bg = "Floralwhite")
        u.pack(fill = X)
        mainloop()
    else:
        tkinter.messagebox.showinfo("提示","你是白方，请单击鼠标并等待黑方开局")
        down = -1
        num += 1
        w1.bind("<Button -1>",callback2) 
        u=Button(pvproot,text="退出游戏",width=10,height=1,command= quit,font=('楷体',15), bg = "Floralwhite")
        u.pack(fill = X)
        pvproot.mainloop()



def onlinewindow():
    global e,onlineroot,e2
    onlineroot =  Tk()
    l1 = Label(onlineroot,text= "ip地址")
    l1.grid(row=0,column=0)
    l1 = Label(onlineroot,text= "端口")
    l1.grid(row=1,column=0)
    e = Entry(onlineroot, font=('黑体', 12))
    e.insert(0,"127.0.0.1")
    e.grid(row=0,column=1)
    e2 = Entry(onlineroot, font=('黑体', 12))
    e2.insert(0,"9001")
    e2.grid(row=1,column=1)
    b = Button(onlineroot,command=c,text="创建游戏",bd = "5",width=28)
    b2 = Button(onlineroot,command=c2,text="加入游戏",bd = "5",width=28)
    b.grid(row=2,column=0,columnspan=2,)
    b2.grid(row=3,column=0,columnspan=2)
    onlineroot.mainloop()

#onlinewindow()