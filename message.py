#sticky specify the location either east,west,north,south
#colummnspan: merge the columns into it

from tkinter import *

mw = Tk()

mw.title('auto messenger')
mw.iconbitmap('images/msg.ico')

# creating widgets
hmt_label = Label(mw, text='How Many Times:', font=('Arial',14))   #hmt=how many times
hmt_input = Entry(mw, width=5, font=('Arial',18))
hmt_times = Label(mw, text='Times', font=('Arial',12))

wt_input = Entry(mw, width=5, font=('Arial',18))
wt_label = Label(mw, text='Waiting Times:', font=('Arial',14))     #wt = waiting times
wt_sec = Label(mw, text='Seconds', font=('Arial',12))

msg_label = Label(mw, text='Mesage:', font=('Arial',14))           #msg= message
msg_input = Entry(mw, width=30, font=('Arial',18))

# showing widgets
hmt_label.grid(row=0,column=0,padx=10,pady=10,sticky=E)
hmt_input.grid(row=0,column=1,padx=10,pady=10,sticky=W)
hmt_times.grid(row=0,column=2,padx=10,pady=10,sticky=W)

wt_label.grid(row=1,column=0,padx=10,pady=10,sticky=E)
wt_input.grid(row=1,column=1,padx=10,pady=10,sticky=W)
wt_sec.grid(row=1,column=2,padx=10,pady=10,sticky=W)

msg_label.grid(row=2,column=0,padx=10,pady=10,sticky=E)
msg_input.grid(row=2,column=1,padx=10,pady=10,sticky=W,columnspan=2)


mw.mainloop()