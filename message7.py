#local variables using in the function

from tkinter import *
from threading import  *
import pyautogui as pag
import time

mw = Tk()
mw.title('auto messenger')
mw.iconbitmap('images/msg.ico')


class automessenger(Thread):                                 #class
    hmt_c = 5
    wt_c = 3
    msg_c = 'running'
    def run(self):                                            #method
        for x in range(self.hmt_c):
            time.sleep(self.wt_c)
            pag.typewrite(self.msg_c)
            pag.press('enter')


def messenger(hmt, wt, msg):
    print(hmt, 't imes')
    print(wt, 'seconds')
    print(msg)

    send = automessenger()                               #object of class
    send.daemon = True                         #to stop the sub thread automatically after the main thead
    send.start()                                         #calling of method


# creating widgets
hmt_label = Label(mw, text='How Many Times:', font=('Arial', 14))  # hmt=how many times
hmt_input = Entry(mw, width=5, font=('Arial', 18))
hmt_times = Label(mw, text='Times', font=('Arial', 12))

wt_input = Entry(mw, width=5, font=('Arial', 18))
wt_label = Label(mw, text='Waiting Time :', font=('Arial', 14))  # wt = waiting times
wt_sec = Label(mw, text='Seconds', font=('Arial', 12))

msg_label = Label(mw, text='Mesage:', font=('Arial', 14))  # msg= message
msg_input = Entry(mw, width=30, font=('Arial', 18))  # width=30, box will be bigger on x axis

send_btn = Button(mw, text='start sending!', font=('Arial', 14),
                  command=lambda: messenger(hmt_input.get(), wt_input.get(), msg_input.get()))

# showing widgets
hmt_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)  # sticky specify the location either east,west,north,south
hmt_input.grid(row=0, column=1, padx=10, pady=10, sticky=W)
hmt_times.grid(row=0, column=1, padx=95, pady=10, sticky=W)

wt_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
wt_input.grid(row=1, column=1, padx=10, pady=10, sticky=W)
wt_sec.grid(row=1, column=1, padx=95, pady=10, sticky=W)

msg_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)
msg_input.grid(row=2, column=1, padx=10, pady=10, sticky=W)

send_btn.grid(row=3, column=1, pady=25)

mw.mainloop()

