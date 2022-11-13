from tkinter import *
root=Tk()
root.title("simple caluculator")
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def clicked(num):
    if(num=="="):
        s1=str(e.get())
        e.delete(0,END)
        for i in s1:
            if not i.isdigit():
                s2=i
        if s2=="+":
            a=s1.index('+')
            b=s1[:a]
            c=s1[a+1:]
            sum=int(b)+int(c)
            e.insert(0,sum)
        elif s2=="-":
            a=s1.index('-')
            b=s1[:a]
            c=s1[a+1:]
            sum=int(b)-int(c)
            e.insert(0,sum)
        elif s2=='*':
            a=s1.index('*')
            b=s1[:a]
            c=s1[a+1:]
            sum=int(b)*int(c)
            e.insert(0,sum)
        elif s2=='/':
            a=s1.index('/')
            b=s1[:a]
            c=s1[a+1:]
            sum=int(b)/int(c)
            e.insert(0,sum)
        else:
            pass

            
    else:
        s=str(e.get())+str(num)
        e.delete(0,END)
        e.insert(0,s)
def clear():
    e.delete(0,END)
    

but_1=Button(root,text="1",padx=30,pady=10,command=lambda: clicked(1))
but_2=Button(root,text="2",padx=30,pady=10,command=lambda: clicked(2))
but_3=Button(root,text="3",padx=30,pady=10,command=lambda: clicked(3))
but_4=Button(root,text="4",padx=30,pady=10,command=lambda: clicked(4))
but_5=Button(root,text="5",padx=30,pady=10,command=lambda: clicked(5))
but_6=Button(root,text="6",padx=30,pady=10,command=lambda: clicked(6))
but_7=Button(root,text="7",padx=30,pady=10,command=lambda: clicked(7))
but_8=Button(root,text="8",padx=30,pady=10,command=lambda: clicked(8))
but_9=Button(root,text="9",padx=30,pady=10,command=lambda: clicked(9))
but_0=Button(root,text="0",padx=30,pady=10,command=lambda: clicked(0))
but_clear=Button(root,text="clear",padx=60,pady=10,command=clear)
but_add=Button(root,text="+",padx=30,pady=10,command=lambda: clicked("+"))
but_sub=Button(root,text="-",padx=30,pady=10,command=lambda: clicked("-"))
but_mul=Button(root,text="*",padx=30,pady=10,command=lambda: clicked("*"))
but_div=Button(root,text="/",padx=30,pady=10,command=lambda: clicked("/"))
but_equal=Button(root,text="=",padx=60,pady=10,command=lambda: clicked("="))
but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)

but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)

but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)

but_0.grid(row=4,column=0)
but_clear.grid(row=4,column=1,columnspan=2)
but_add.grid(row=5,column=0)
but_sub.grid(row=5,column=1)
but_mul.grid(row=5,column=2)
but_div.grid(row=6,column=0)
but_equal.grid(row=6,column=1,columnspan=2)
root.mainloop()