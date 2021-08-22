from tkinter import *

def calc(x):
    global t1
    global t2
    global op
    if x in  ['0','1','2','3','4','5','6','7','8','9']:
        en.insert(END,x)
    elif x=='+':
        t1=int(en.get())
        op='+'
        en.delete(0,END)
    elif x=='-':
        t1=int(en.get())
        op='-'
        en.delete(0,END)    
    elif x=='=' and op=='+':
        t2=int(en.get())
        en.delete(0,END)
        r=t1+t2
        en.insert(END,r)
    elif x=='=' and op=='-':
        t2=int(en.get())
        en.delete(0,END)
        r=t1-t2
        en.insert(END,r)
    elif x=='C':
        en.delete(0,END)
    elif x=='*':
        t1=int(en.get())
        op='*'
        en.delete(0,END)
    elif x=='/':
        t1=int(en.get())
        op='/'
        en.delete(0,END)    
    elif x=='=' and op=='*':
        t2=int(en.get())
        en.delete(0,END)
        r=t1*t2
        en.insert(END,r)
    elif x=='=' and op=='/':
        t2=int(en.get())
        if t2==0:
            r='На ноль делить нельзя! '
            en.delete(0,END)
            en.insert(END,r)
        else:
            en.delete(0,END)
            r=t1/t2
            en.insert(END,r)
    elif x=='C':
        en.delete(0,END)



                
root=Tk()
root.config(bg='#363636')
root.title('Calculator')
root.resizable(0,0)

en=Entry(root,width=28,font=('Time',20),bg='#FFFFFF',justify=RIGHT)
en.grid(row=0,column=0,columnspan=10,padx=5,pady=5)

bt1=Button(root,width=8,font=('Time',15),text='1',bg='#A9A9A9',fg='#000000', command=lambda x='1': calc(x))
bt1.grid(row=3,column=1,padx=5,pady=5,sticky=W)

bt2=Button(root,width=8,font=('Time',15),text='2',bg='#A9A9A9',fg='#000000', command=lambda x='2': calc(x))
bt2.grid(row=3,column=2,padx=5,pady=5)

bt3=Button(root,width=8,font=('Time',15),text='3',bg='#A9A9A9',fg='#000000', command=lambda x='3': calc(x))
bt3.grid(row=3,column=3,padx=5,pady=5)

bt4=Button(root,width=8,font=('Time',15),text='4',bg='#A9A9A9',fg='#000000', command=lambda x='4': calc(x))
bt4.grid(row=2,column=1,padx=5,pady=5,sticky=W)

bt5=Button(root,width=8,font=('Time',15),text='5',bg='#A9A9A9',fg='#000000', command=lambda x='5': calc(x))
bt5.grid(row=2,column=2,padx=5,pady=5)

bt6=Button(root,width=8,font=('Time',15),text='6',bg='#A9A9A9',fg='#000000', command=lambda x='6': calc(x))
bt6.grid(row=2,column=3,padx=5,pady=5)

bt7=Button(root,width=8,font=('Time',15),text='7',bg='#A9A9A9',fg='#000000', command=lambda x='7': calc(x))
bt7.grid(row=1,column=1,padx=5,pady=5,sticky=W)

bt8=Button(root,width=8,font=('Time',15),text='8',bg='#A9A9A9',fg='#000000', command=lambda x='8': calc(x))
bt8.grid(row=1,column=2,padx=5,pady=5,sticky=N)

bt9=Button(root,width=8,font=('Time',15),text='9',bg='#A9A9A9',fg='#000000', command=lambda x='9': calc(x))
bt9.grid(row=1,column=3,padx=5,pady=5,sticky=N)

bt13=Button(root,width=8,font=('Time',15),text='C',bg='#FF4500',fg='#000000', command=lambda x='C': calc(x))
bt13.grid(row=4,column=1,padx=5,pady=5,sticky=W)

bt10=Button(root,width=8,font=('Time',15),text='0',bg='#A9A9A9',fg='#000000', command=lambda x='0': calc(x))
bt10.grid(row=4,column=2,padx=5,pady=5,sticky=S)

bt11=Button(root,width=8,font=('Time',15),text='=',bg='#FF4500',fg='#000000', command=lambda x='=': calc(x))
bt11.grid(row=4,column=3,padx=5,pady=5,sticky=S)

bt12=Button(root,width=8,font=('Time',15),text='+',bg='#A9A9A9',fg='#000000', command=lambda x='+': calc(x))
bt12.grid(row=1,column=4,padx=5,pady=5,sticky=E)

bt14=Button(root,width=8,font=('Time',15),text='-',bg='#A9A9A9',fg='#000000', command=lambda x='-': calc(x))
bt14.grid(row=2,column=4,padx=5,pady=5,sticky=E)

bt15=Button(root,width=8,font=('Time',15),text='*',bg='#A9A9A9',fg='#000000', command=lambda x='*': calc(x))
bt15.grid(row=3,column=4,padx=5,pady=5,sticky=E)

bt16=Button(root,width=8,font=('Time',15),text='/',bg='#A9A9A9',fg='#000000', command=lambda x='/': calc(x))
bt16.grid(row=4,column=4,padx=5,pady=5,sticky=E)



root.mainloop()
