from tkinter import *
import joblib
import numpy as np
from PIL import ImageTk, Image


def ButtonDesigner(frame,index):
    bname='Buttons/'+str(index)+'.png'
    bimage.append(ImageTk.PhotoImage(Image.open(bname)))
    butt=Button(frame, image=bimage[index],command=lambda: ScreenWiper(bval[index]),bg=bgcolor,border=0)
    Buttons.append(butt)

def LabelDesigner(frame,index):
    lname='Labels/l'+str(index)+'.png'
    limage.append(ImageTk.PhotoImage(Image.open(lname)))
    labe = Label(frame, image=limage[index],bg = "#D0E1F9")
    Labels.append(labe)

def ScreenWiper(val):
    global flag
    for i in val:
        flag.append(i)
    ScreenManager('n')
    
def ScreenManager(check):
    global Iter
    Labels[Iter].place_forget()
    for i in list(buttinfo[Iter].keys()):
        Buttons[i].place_forget()
    if check=='n':
        Iter+=1
    else:
        Iter-=1
    Labels[Iter].place(x=0,y=0)
    for i in list(buttinfo[Iter].keys()):
        Buttons[i].place(x=buttinfo[Iter][i][0],y=buttinfo[Iter][i][1])

def Undo():
    global flag,Iter
    if Iter in [12,23]:
        pass
    elif Iter in [24,25,26]:
        flag=flag[:-8]
    else:
        flag.pop()
    ScreenManager('u')
    
def Predict(frame):
    global nimage,nlabe,pimage,plabe,flag,Iter
    flag.pop(-14)
    pflag=np.array(flag).reshape(1,-1)
    result=Model.predict(pflag)[0]
    Labels[Iter].place_forget()
    for i in list(buttinfo[Iter].keys()):
        Buttons[i].place_forget()
    Iter+=1
    pname='FlagData/'+result+'.jpg'
    pimage=ImageTk.PhotoImage(Image.open(pname))
    plabe = Label(frame, image=pimage,bg = "#D0E1F9")
    plabe.place(x=100,y=20)
    nname='FlagData/'+result+'.png'
    nimage=ImageTk.PhotoImage(Image.open(nname))
    nlabe = Label(frame, image=nimage,bg = "#D0E1F9")
    nlabe.place(x=120,y=380)
    Buttons[32].place(x=0,y=530)
    Buttons[33].place(x=520,y=530)
    
def Restart():
    global Iter,flag,plabe,nlabe
    plabe.place_forget()
    nlabe.place_forget()
    Buttons[32].place_forget()
    Buttons[33].place_forget()
    flag=[]
    Iter=0
    Labels[0].place(x=0,y=0)
    Buttons[28].place(x=520,y=530)


if __name__=='__main__':
    bgcolor="#D0E1F9"
    Iter=0
    Buttons,bimage,Labels,limage,flag=[],[],[],[],[]
    pimage,plabe,nimage,nlabe=None,None,None,None
    Model=joblib.load('Model.pkl')
    buttinfo=[{28:(520,530)},{0:(100,200),1:(100,300),2:(400,200),3:(400,300),5:(250,400)},{0:(0,120),1:(0,220),2:(0,320),3:(0,420),4:(260,120),5:(260,220),6:(260,320),7:(260,420),9:(520,120),11:(520,220),13:(520,320),14:(520,420),30:(0,530)},
          {1:(100,130),2:(100,230),3:(100,330),4:(100,430),5:(400,130),6:(400,230),7:(400,330),8:(400,430),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},
          {18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{29:(250,300),30:(0,530)},{0:(100,250),1:(100,350),2:(400,250),4:(400,350),30:(0,530)},{0:(250,150),1:(250,250),2:(250,350),30:(0,530)},{0:(250,200),1:(250,320),30:(0,530)},
          {0:(250,150),1:(250,250),4:(250,350),30:(0,530)},{0:(0,120),1:(0,210),2:(0,300),3:(0,390),4:(260,120),5:(260,210),6:(260,300),7:(260,390),9:(520,120),10:(520,210),14:(520,300),15:(520,390),16:(100,480),17:(400,480),30:(0,550)},
          {18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{18:(250,210),19:(250,340),30:(0,530)},{29:(250,300),30:(0,530)},{20:(0,250),21:(520,250),22:(260,250),23:(260,350),24:(0,350),25:(400,450),26:(100,450),27:(520,350),30:(0,530)},
          {20:(100,160),21:(400,160),22:(260,460),23:(400,260),24:(100,260),25:(400,360),26:(100,360),30:(0,530)},{20:(0,250),21:(520,250),22:(260,250),23:(260,350),24:(0,350),25:(400,450),26:(100,450),27:(520,350),30:(0,530)},{31:(250,300),30:(0,530)}]
    bval=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[22],[50],[1],[0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0]]
    
    app=Tk()
    app.geometry("1530x840")
    app.title('Flag Predictor')

    BgImage=ImageTk.PhotoImage(Image.open("back.jpg"))
    BgLabel = Label(app, image = BgImage)
    BgLabel.place(x = 0,y = 0)

    frame1 = Frame(app, bg = "#D0E1F9",width=800,height=900)
    frame1.place(x=400,y=200)

    for i in range(28):
        ButtonDesigner(frame1,i)
    for i in range(27):
        LabelDesigner(frame1,i)
    
    bimage.append(ImageTk.PhotoImage(Image.open('Buttons/proceed.png')))
    Buttons.append(Button(frame1, image=bimage[28],command=lambda: ScreenManager("n"),bg=bgcolor,border=0))
    bimage.append(ImageTk.PhotoImage(Image.open('Buttons/predict.png')))
    Buttons.append(Button(frame1, image=bimage[29],command=lambda: ScreenManager("n"),bg=bgcolor,border=0))
    bimage.append(ImageTk.PhotoImage(Image.open('Buttons/undo.png')))
    Buttons.append(Button(frame1, image=bimage[30],command=Undo,bg=bgcolor,border=0))
    Buttons.append(Button(frame1, image=bimage[29],command=lambda: Predict(frame1),bg=bgcolor,border=0))
    bimage.append(ImageTk.PhotoImage(Image.open('Buttons/restart.png')))
    Buttons.append(Button(frame1, image=bimage[31],command=Restart,bg=bgcolor,border=0))
    bimage.append(ImageTk.PhotoImage(Image.open('Buttons/exit.png')))
    Buttons.append(Button(frame1, image=bimage[32],command=app.destroy,bg=bgcolor,border=0))
    
    Labels[0].place(x=0,y=0)
    Buttons[28].place(x=520,y=530)
    app.mainloop()