import os, sys, csv, time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from webbrowser import BackgroundBrowser


if not __name__ == '__main__':
    from . import ticket
    from . import server




class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=1200, borderwidth=4, relief='flat')
        self.root = root

        # setting scroll ver
        self.canvas = tk.Canvas(self.root)
        self.mainframe = ttk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)      # 縦スクロールバーをrootに作成
        self.hsb = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.canvas.xview)    # 横スクロールバーをrootに作成
        self.canvas.configure(yscrollcommand=self.vsb.set)  # 縦スクロールバーの動作をCanvasに設定
        self.canvas.configure(xscrollcommand=self.hsb.set)  # 横スクロールバーの動作をCanvasに設定
        # pack スクロールバーは先にpackする
        self.hsb.pack(side="bottom", fill="x")
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        # canvasにウィジェットを配置
        self.canvas.create_window((0,0), window=self.mainframe, anchor="nw")

        self.create_frame_widgets()
        self.create_home_widgets()
    
    def loop(self):
        self.destroy_home_widgets()
        self.create_frame_widgets()
        self.create_home_widgets()
        


    def destroy_home_widgets(self):
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        self.frame6.destroy()
        
    def create_frame_widgets(self):
        # Make Frame0
        self.frame0 = ttk.Frame(self.mainframe)
        self.frame0.pack(fill=tk.X)
        # Make Frame1
        self.frame1 = ttk.Frame(self.mainframe)
        self.frame1.pack(fill=tk.X)
        # Make Frame2
        self.frame2 = ttk.Frame(self.mainframe)
        self.frame2.pack(fill=tk.X)
        # Make Frame3
        self.frame3 = ttk.Frame(self.mainframe)
        self.frame3.pack(fill=tk.X)
        # Make Frame4
        self.frame4 = ttk.Frame(self.mainframe)
        self.frame4.pack(fill=tk.X)
        # Make Frame5
        self.frame5 = ttk.Frame(self.mainframe)
        self.frame5.pack(fill=tk.X)
        # Make Frame6
        self.frame6 = ttk.Frame(self.mainframe)
        self.frame6.pack(fill=tk.X)

        # Frame0 Constitution
        self.bakedTimeImg = tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))\
            + os.sep +'Img' + os.sep + 'bakedTime.png')
        self.small_bakedTimeImg = self.bakedTimeImg.subsample(8, 10)
        bakedTimeLabel1 = ttk.Label(self.frame0, text='9:30', font=('Meiryo UI',20), image=self.small_bakedTimeImg, compound='center')
        bakedTimeLabel1.pack(anchor=tk.W, side=tk.LEFT)
        TitleLabel = ttk.Label(self.frame0, text='ResManagement_ver1.0.0 produced by RikutoKoike    tell:090-6823-0709', font=('Meiryo UI',15))
        TitleLabel.pack()
        # Frame2 Constitution
        bakedTimeLabel2 = ttk.Label(self.frame2, text='11:00', font=('Meiryo UI',20), image=self.small_bakedTimeImg, compound='center')
        bakedTimeLabel2.pack(anchor=tk.W, side=tk.LEFT)
        # Frame4 Constitution
        bakedTimeLabel3 = ttk.Label(self.frame4, text='12:30', font=('Meiryo UI',20), image=self.small_bakedTimeImg, compound='center')
        bakedTimeLabel3.pack(anchor=tk.W, side=tk.LEFT)
        # Frame6 Constitution
        bakedTimeLabel4 = ttk.Label(self.frame6, text='14:00', font=('Meiryo UI',20), image=self.small_bakedTimeImg, compound='center')
        bakedTimeLabel4.pack(anchor=tk.W, side=tk.LEFT)

        

    def create_home_widgets(self):
        def sepainf(rmDatabase, time1, time2, time3, time4):
            now = int(time.time())
            pass









        with open(os.getcwd() + os.sep + 'rm' + os.sep + 'rmDatabase.csv', encoding='shift-jis') as f:           #scan to method_index
            csvreader = csv.reader(f)
            rmDatabase = [row for row in csvreader]

        # Frame1
        Ticket = []
        for i in range(len(rmDatabase)):
            temp_instance = ticket.ticket()
            temp_instance.makeTicket(self.frame1, rmDatabase[i], i%6, i//6)
            Ticket.append(temp_instance)
            
        
        # Frame2
        
        

        # Frame3
        


        # Frame4
        

        # Frame5


        # Frame6
        
        # Frameの大きさを確定してCanvasにスクロール範囲を設定
        self.mainframe.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))



if __name__ == '__main__':
    import ticket
    import server

    root = tk.Tk()
    root.title('RM_test')
    root.geometry('800x1200')
    app = Application(root=root)
    app.mainloop()