#!/usr/bin/env python
#-*-coding:utf-8-*-

import Tkinter, threading, socket

class Client(Tkinter.Tk): # héritage de la classe Tkinter.Tk -> fenêtre python

    def __init__(self):
        Tkinter.Tk.__init__(self) # constructeur de la classe mère
        self.width, self.height = str(self.winfo_screenwidth()//2), str(self.winfo_screenheight()//2) #résolution écran (// division entière par 2 pour avoir la moitié de l'écran)
        self.title("Tchat - Client") #titre de la fenêtre
        self.geometry(self.width + "x" + self.height) #taille de la fenêtre
        self.resizable(width = False, height = False) # redimensionnement de la fenêtre interdit

        self.panel_top = Tkinter.Frame(self) #conteneur de widget haut
        self.panel_top.pack(side = Tkinter.TOP, fill = Tkinter.BOTH, expand = Tkinter.YES) #remplissage (fill) sur toute la largeur, étirement (expand) sur toute la hauteur 

        self.chat_box = Tkinter.Text(self.panel_top, state = Tkinter.DISABLED, font = ("Helvetica", 12))
        self.chat_box.pack(fill = Tkinter.BOTH, expand = Tkinter.YES) #.BOTH prend toute la largeur du widget parent (conteneur),.pack() permet ajouter un widget à son parent (conteneur)

        self.scrollbar = Tkinter.Scrollbar(self.chat_box)
        self.scrollbar.pack(side = Tkinter.RIGHT, fill = Tkinter.Y) #.Y prend la hauteur du widget parent (chat_box)

        self.chat_box.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.chat_box.yview)

        self.panel_bottom = Tkinter.Frame(self)
        self.panel_bottom.pack(side = Tkinter.BOTTOM, fill = Tkinter.BOTH)

        self.text_var = Tkinter.StringVar()
        self.text_tmp = ''
        
        self.input_text = Tkinter.Entry(self.panel_bottom, textvariable = self.text_var)
        self.input_text.pack(fill = Tkinter.BOTH)

        self.todo = True
        self.flag = True
        self.host = '127.0.0.1'
        self.port = 15555
        
        try:
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_client.connect((self.host, self.port))

            self.threadReceive = threading.Thread(target = self.receive)
            self.threadSend = threading.Thread(target = self.send)
            self.threadReceive.start()
            self.threadSend.start()
        except:
            pass

        self.input_text.bind("<Return>", self.display_message)
        self.mainloop()

        try:
            self.socket_client.close()
            self.todo = False
        except:
            pass
        
    def display_message(self, event):
        if self.flag: # si c'est le tour du client de parler on affiche son message
            message = self.text_var.get()
            if message != '':
                self.chat_box.config(state = Tkinter.NORMAL) #revenir à la valeur par défaut avant de pouvoir éditer "chat_box"
                self.chat_box.insert(Tkinter.END, 'You > ' + message + '\n') # insertion du texte à la fin
                self.chat_box.config(state = Tkinter.DISABLED)

                self.text_var.set('')
                self.text_tmp = message

    def send(self):
        while self.todo:
            if self.flag:
               if self.text_tmp != '':
                    self.socket_client.send('Stranger > ' + self.text_tmp)
                    self.text_tmp = ''
                    self.flag = False
                

    def receive(self):
        while self.todo:
            message = self.socket_client.recv(1024)
            if message:
                self.chat_box.config(state = Tkinter.NORMAL) #revenir à la valeur par défaut avant de pouvoir éditer "chat_box"
                self.chat_box.insert(Tkinter.END, message + '\n') # insertion du texte à la fin
                self.chat_box.config(state = Tkinter.DISABLED)

                self.flag = True

Client()
