import imp
import os, sys, csv
from re import M
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

if not __name__ == '__main__':
    from . import server


class ticket():
    def __init__(self):
        pass

    def makeTicket(self, baseframe, inf, x, y):
        def trash():
            name = self.entry_name.get()
            tel = self.entry_tel.get()
            unix_time = self.entry_unix_time.get()
            server.trash(name, tel, unix_time)
        
        self.Ticket = ttk.Frame(baseframe, width=120, height=180, padding=(5,10), relief='flat')
        #self.Ticket.grid_propagate(False)
        self.Ticket.grid(column=x, row=y)
        self.Ticket_top = ttk.Frame(self.Ticket, width=120, height=180, padding=(5,10), relief='flat')
        #self.Ticket_top.grid_propagate(False)
        self.Ticket_top.pack()
        self.unix_time = datetime.fromtimestamp(int(inf[2][:-2]))
        text =\
             '氏名：'+inf[0]+'\n'\
            +'電話：'+inf[1]+'\n'\
            +'日付：'+f'{self.unix_time:%m/%d %H:%M}'+'\n'\
            +'食パン：'+str(inf[3])+'本'+str(inf[4])+'斤'+'\n'\
            +'予約：'+inf[5].replace('nn', '\n　　　')+'\n'\
            +'その他：'+inf[6]+'\n'
        self.fusenImg = tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))\
            + os.sep +'Img' + os.sep + 'fusen.png')
        self.small_fusenImg = self.fusenImg.subsample(4, 3)
        self.free = ttk.Label(self.Ticket_top, text=text, font=('Meiryo UI',12), image=self.small_fusenImg, compound='center')
        self.free.pack()

        self.trashboxImg = tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))\
            + os.sep +'Img' + os.sep + 'Trashbox.png')
        self.small_trashboxImg = self.trashboxImg.subsample(10, 10)
        style=ttk.Style()
        style.theme_use('default')
        style.configure('B.TButton', relief="flat")
        self.trashboxImgButton = ttk.Button(self.Ticket_top, image=self.small_trashboxImg, compound='none', style='B.TButton', command=trash)
        self.trashboxImgButton.pack(anchor=tk.E)

        self.entry_name = tk.StringVar()
        self.entry_name.set(inf[0])
        self.entry_tel = tk.StringVar()
        self.entry_tel.set(inf[1])
        self.entry_unix_time = tk.StringVar()
        self.entry_unix_time.set(inf[2])


if __name__ == '__main__':
    import server