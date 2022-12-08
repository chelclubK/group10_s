from tkinter import *
from random import randint
from tkinter import messagebox as mb
N=26#строка
M=26#ряд
S=30
k=0
dx=[1,0,-1,0]
dy=[0,-1,0,1]
pole=list()
for i in range(N):
    row=list()
    for j in range(M):
        cell={'lw':1,'tw':1}
        row.append(cell)
    cell={'lw':1,'tw':0}
    row.append(cell)
    pole.append(row)
row=list()
for j in range(M):
    cell={'lw':0,'tw':1}
    row.append(cell)
cell={'lw':0,'tw':0}
row.append(cell)
pole.append(row)

def paintMaze():
    xolst.delete('line')
    #newMaze()
    for i in range(N+1):
        for j in range(M+1):
            x=j
            y=i
            if pole[i][j]['lw']==1:
                xolst.create_line(x*S+5,y*S+5,
                                  x*S+5,y*S+S+5,
                                  fill='black',width=2, tag='line')
            if pole[i][j]['tw']==1:
                xolst.create_line(x*S+5,y*S+5,
                                  x*S+S+5,y*S+5,
                                  fill='black',width=2,tag='line')
def movehero(event):
    global hx, hy, my, mx, k
    if event.keysym=='Right':
        if pole[hy][hx+1]['lw']==0:
            xolst.move(hero,S,0)
            hx+=1
    if event.keysym=='Left':
        if pole[hy][hx]['lw']==0:
            xolst.move(hero,-S,0)
            hx-=1
    if event.keysym=='Up':
        if pole[hy][hx]['tw']==0:
            xolst.move(hero,0,-S)
            hy-=1
    if event.keysym=='Down':
        if pole[hy+1][hx]['tw']==0:
            xolst.move(hero,0,S)
            hy+=1
    if event.keysym=='space':
        NewMaze()
    if hx==mx and hy==my:
        mx=randint(1,M-1)
        my=randint(1,M-1)
        xolst.delete('goal')
        xolst.create_image(mx*S+20,my*S+20,image=mine, tag='goal')
        k+=1
        stet['text']='СЧЕТ '+str(k)
def NewMaze():
    for i in range(1,N):
        for j in range(1,M):
            pole[i][j]['lw']=randint(0,1)
            pole[i][j]['tw']=randint(0,1)
    pole[0][1]['lw']=0
    pole[1][0]['tw']=0
    paintMaze()
def createMaze():
    #формируем матрицу 
    Attribute=[]
    for i in range(N):
        Row=[]
        for j in range(M):
            Row.append('outside')
        Attribute.append(Row)
    #start
    a=randint(1,N-1)
    b=randint(1,M-1)
    Attribute[a][b]='inside'
    counter=0
    for i in range(4):
        xc=b+dx[i]
        yc=a+dy[i]
        if xc>=0 and yc>=0 and xc<M and yc<N:
            Attribute[yc][xc]='border'
            counter+=1
    while counter>0:
        c=randint(1,counter)
        for i in range(N):
            for j in range(M):
                if Attribute[i][j]=='border':
                    c-=1
                    if c==0:
                        xloc=j
                        yloc=i
        Attribute[yloc][xloc]='inside'
        c=0
        for i in range(4):
            xc=xloc+dx[i]
            yc=yloc+dy[i]
            if xc>=0 and yc>=0 and xc<M and yc<N:
                if Attribute[yc][xc]=='inside':
                    c+=1
                elif Attribute[yc][xc]=='outside':
                    Attribute[yc][xc]='border'
        c=randint(1,c)
        for i in range(4):  
            xc=xloc+dx[i]
            yc=yloc+dy[i]
            if xc>=0 and yc>=0 and xc<M and yc<N:
                if Attribute[yc][xc]=='inside':
                    c-=1
                    if c==0:
                        if dx[i]==-1:
                            pole[yloc][xloc]['lw']=0
                        elif dx[i]==1:
                            pole[yloc][xloc+1]['lw']=0
                        elif dy[i]==-1:
                            pole[yloc][xloc]['tw']=0
                        elif dy[i]==1:
                            pole[yloc+1][xloc]['tw']=0
        counter=0
        for i in range(N):
            for j in range(M):
                if Attribute[i][j]=='border':
                    counter+=1
    paintMaze()
def timerzlo():
    global hy, hx, zx, zy, dz,q,k
    xolst.move(zloy,0,dz*S)
    zy+=dz
    if zy==-1:
        dz=1
        zx=randint(1,M-1)
        xolst.coords(zloy,zx*S+20,zy*S+20)
    elif zy==N:
        dz=-1
        zx=randint(1,M-1)
        xolst.coords(zloy,zx*S+20,zy*S+20)
    if hx==zx and hy==zy:
        q+=1
        zxc['text']='СПАЛИЛИ '+str(q)+'/3'
        print('kapec')
    if q==3:
        if k>10:
            mb.showinfo('Запись в дневнике', 'молодец, но РОДИТЕЛЕЙ В ШКОЛУ')
            q=0
        if k<10:
            mb.showinfo('Запись в дневнике', 'ахаха бот! РОДИТЕЛЕЙ В ШКОЛУ')
            #q=0
            ok.destroy()
    if k==20:
        mb.showinfo('фаталити','ну молодец молодец, умеешь уворачиваться, но это тебя не спасет, училка то бессмертная в отличае от тебя хахаха мучайся дальше хахаха')
        k=0
    ok.after(50,timerzlo)
hx=0
hy=0
zx=0
zy=3
dz=1
q=0
mx=randint(1,25)
my=randint(1,25)
ok=Tk()
ok.title('ЛАБИРИНТ')
ok.resizable(False, False)
ok.geometry('1000x1000')
ok['bg']='lightgreen'
mine=PhotoImage(file='майнкрафт.png')
lox=PhotoImage(file='школьник.png')
ychilka=PhotoImage(file='училка.png')
resh=Button(ok, text='Решить лабиринт')
craft=Button(ok, text='Создать')
xolst=Canvas(ok, width=800,height=790)
zxc1=Label(ok, text='ДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР ШКОЛЬНИКА')
zxc1.pack()
stet=Label(ok, text='СЧЕТ-'+str(k))
stet.pack()
zxc=Label(ok, text='СПАЛИЛИ '+str(q)+'/3')
zxc.pack()
xolst.pack(side='top')
createMaze()
hero=xolst.create_image(20,20,image=lox)
xolst.create_image(mx*S+20,my*S+20,image=mine,tag='goal')
zloy=xolst.create_image(zx*S+20,zy*S+20, image=ychilka)
resh.pack()
craft.pack()
zxc1=Label(ok, text='P.s. Если нажать на пробел то поменяется лабиринт, используйте это когда вы в тупике. Удачи вам в тренировки пальцев.')
zxc1.pack()
zxc11=Label(ok, text='"Решить лабиринт" и "Создать" не работает.')
zxc11.pack()
ok.bind('<KeyPress>',movehero)
timerzlo()
ok.mainloop()
