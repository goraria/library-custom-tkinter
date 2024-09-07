from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from CTkListbox import *
import pymysql
import os

import AddBook
import AddMember

set_appearance_mode("System")
set_default_color_theme("blue")

main_color = '#62e2ff'
hover_color = '#74f0ff'

myPassword = 'Jiang@99@03$0820'
myDatabase = 'se_proj'

myConnect = pymysql.connect(host='localhost', user='root', password=myPassword, database=myDatabase)
myCursor = myConnect.cursor()

class App(CTk):
    def __init__(self):
        super().__init__()
        appIconConst = PhotoImage(file='./icons/dup.png')
        self.title('Return Book')
        self.minsize(width=1280, height=720)
        self.resizable(False, False)
        self.geometry('1280x720')
        self.iconbitmap('./icons/bitmap.ico')
        self.iconphoto(True, appIconConst, appIconConst)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ####

        self.logoImage = CTkImage(Image.open('./icons/logo_modified.png'), size=(50, 50))
        self.largeTestImage = CTkImage(Image.open('./icons/cmd.png'), size=(200, 200))
        self.iconImage = CTkImage(Image.open('./icons/cmd.png'), size=(20, 20))
        self.homeImage = CTkImage(Image.open('./icons/homes.png'), size=(40, 40))
        self.bookImage = CTkImage(Image.open('./icons/dup.png'), size=(40, 40))
        self.addUserImage = CTkImage(Image.open('./icons/user.png'), size=(40, 40))

        ####

        self.navigationFrame = CTkFrame(self)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")
        self.navigationFrame.grid_rowconfigure(4, weight=1)

        self.navigationFrameLabel = CTkLabel(self.navigationFrame, text='  Gorth Inc.', image=self.logoImage, compound='left', font=CTkFont('Arial', size=20, weight='bold'))
        self.navigationFrameLabel.grid(row=0, column=0, padx=20, pady=20)

        self.bookButton = CTkButton(self.navigationFrame, height=50, text="Book", image=self.bookImage,
                                     fg_color='transparent', text_color=('black', 'white'), hover_color=('gray75', 'gray25'), anchor='w',
                                     font=CTkFont('Arial', size=14, weight='normal'))
        self.bookButton.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="ew")

        self.appearanceModeMenu = CTkOptionMenu(self.navigationFrame, values=['System', 'Light', 'Dark'], command=self.ChangeAppearanceModeEvent)
        self.appearanceModeMenu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        ####

        self.contentFrame = CTkFrame(self, fg_color=('#AAAAAA', '#555555'))
        self.contentFrame.grid(row=0, column=1, sticky="nsew")
        self.contentFrame.grid_rowconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)

        ####

        self.bookFrame = CTkFrame(self.contentFrame, fg_color='transparent')
        self.bookFrame.grid(row=0, column=1, sticky='nsew')
        self.bookFrame.grid_columnconfigure(0, weight=1)
        self.bookFrame.grid_rowconfigure(0, weight=0)
        self.bookFrame.grid_rowconfigure(1, weight=1)
        self.bookFrame.grid_rowconfigure(2, weight=0)

        ####

        self.bookTopFrame = CTkFrame(self.bookFrame, fg_color='transparent')
        self.bookTopFrame.grid(row=0, column=0, sticky='nsew')
        self.bookTopFrame.grid_columnconfigure(0, weight=1)
        self.bookTopFrame.grid_rowconfigure(0, weight=1)

        self.bookCenterFrame = CTkFrame(self.bookFrame, fg_color='transparent')
        self.bookCenterFrame.grid(row=1, column=0, sticky='nsew')
        self.bookCenterFrame.grid_columnconfigure(0, weight=1)
        self.bookCenterFrame.grid_rowconfigure(0, weight=1)

        self.bookMainCenterFrame = CTkFrame(self.bookCenterFrame, fg_color='transparent')
        self.bookMainCenterFrame.grid(row=0, column=0, padx=5, sticky='nsew')
        self.bookMainCenterFrame.grid_columnconfigure(0, weight=1)
        self.bookMainCenterFrame.grid_rowconfigure(0, weight=1)

        self.bookBottomFrame = CTkFrame(self.bookFrame, fg_color='transparent')
        self.bookBottomFrame.grid(row=2, column=0, sticky='nsew')
        self.bookBottomFrame.columnconfigure(0, weight=1)

        ##

        self.iconRtnBook = CTkImage(Image.open('./icons/rtn.png'), size=(50, 50))
        self.buttonRtnBook = CTkButton(self.bookTopFrame, text='Return', image=self.iconRtnBook, anchor="w", width=150,
                                       height=50, border_width=0, compound='left', font=('Arial Bold', 16), state='disabled')
        self.buttonRtnBook.pack(side='left', padx=(5, 0), pady=5)

        self.iconGiveBook = CTkImage(Image.open('./icons/launch.png'), size=(50, 50))
        self.buttonGiveBook = CTkButton(self.bookBottomFrame, text='Give Book', image=self.iconGiveBook, anchor="w", width=150, height=50,
                                    border_width=0, compound='left', font=('Arial Bold', 16), state='disabled')
        self.buttonGiveBook.pack(side='left', padx=(5, 0), pady=5)

        ####

        self.bgImage = CTkImage(Image.open('./icons/theme.png'))
        self.bgImageLabel = CTkLabel(self.bookMainCenterFrame, image=self.bgImage, text=None)
        self.bgImageLabel.grid(row=0, column=0, ipadx=5, ipady=5)

        #### # Return Form

        self.rtnFrame = CTkFrame(self.bookMainCenterFrame, width=600, height=600, fg_color=('#DBDBDB', '#2B2B2B'))
        self.rtnFrame.grid(row=0, column=0, sticky='nsew')
        self.rtnFrame.grid_columnconfigure(0, weight=1)
        self.rtnFrame.grid_rowconfigure(8, weight=1)
        self.rtnLabel = CTkLabel(self.rtnFrame, text="Return Book", font=CTkFont(family='Arial', size=20, weight="bold"))
        self.rtnLabel.grid(row=0, column=0, padx=30, pady=30)
        self.rtnNameEntry = CTkEntry(self.rtnFrame, width=320, placeholder_text="name book", font=CTkFont(family='Arial', size=14))
        self.rtnNameEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.rtnNameEntry = CTkEntry(self.rtnFrame, width=320, placeholder_text="id person", font=CTkFont(family='Arial', size=14))
        self.rtnNameEntry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.rtnFormButton = CTkButton(self.rtnFrame, text="Return", width=160)
        self.rtnFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))

        #### 

    def ChangeAppearanceModeEvent(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)

    ####


if __name__ == '__main__':
    app = App()
    app.mainloop()


