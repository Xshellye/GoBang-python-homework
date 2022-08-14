import createboard
import search
from tkinter import *
from PIL import Image, ImageTk
import fightbot
import online

def quit():
    mainroot.destroy()

def combine1(): #创建双人对战棋盘
    quit()
    pvp = createboard.PVP()
    pvp.createboard()
    mymainwindow()
    del pvp
    
def combine2(): #创建单人对战棋盘
    quit()
    fightbot.createboard()
    mymainwindow()

    
def combine3(): #创建战绩查询菜单
    quit()
    search.readin()
    mymainwindow()

def combine4(): #创建在线对战棋盘
    quit()
    online.onlinewindow()
    mymainwindow()

def mymainwindow():
    global mainroot
    img = Image.open("b1.png")
    size = 200,200
    img.thumbnail(size)
    mainroot = Tk()
    mainroot.title("五子棋")
    w = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "双人对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine1)  
    w2 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "人机对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine2)            
    w3 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "战绩查询",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine3)            
    w4 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "退出游戏",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = quit,
            width=17)   
    w5 = Button(mainroot,activebackground="black",
            bg = "navajowhite",      #按钮背景颜色
            text = "在线对战",
            font = ("宋体", 16, "bold"),
            bd = "5",                #按钮大小
            fg = "black",
            command = combine4)         
    w.grid(row=0,column=0)
    w2.grid(row=0,column=1)
    w3.grid(row=1,column=0)
    w5.grid(row=1,column=1)
    w4.grid(row=6,column=0,columnspan=2)
    img_png = ImageTk.PhotoImage(img)
    label_img = Label(mainroot, image = img_png)
    label_img.grid(row=2,column=0,rowspan=4,columnspan=2)
    mainroot.mainloop()

if __name__ == "__main__":
    mymainwindow()