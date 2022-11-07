import tkinter as tk
import rm.HomeTk
import rm.server

def main():
    def serverloop():
        app.loop()
        root.after(1000, serverloop)
    
    root = tk.Tk()
    root.title('ResManagement_ver1.0.0')    
    root.geometry('800x1200')
    app = rm.HomeTk.Application(root=root)
    serverloop()
    root.mainloop()


if __name__ == '__main__':
    main()