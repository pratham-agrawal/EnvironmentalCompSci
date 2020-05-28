import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
import User as user
import Back as bk

imageOneSelected = False
imageTwoSelected = False
user.appOpen()

LARGE_FONT = ("Verdana",12)

class Controller(tk.Tk): #tk.TK is inherited
    '''
      A class that manages frames of the program, inherited from tk.Tk

      Attributes
      ----------
      *args : arguments
          Optional
      *kwargs: key worded arguments
          Optional

      Methods
      -------
      show_frame(cont : class)
          Switches the visible frame to the class frame that is entered

      '''

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self,"CompEnv Client")

        container = tk.Frame(self)
        container.pack(side='top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,SignUpPage, UserAccount):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''
            Switches frames

            Takes in a frame class and moves it to the front, thus making it visable

            Parameters
            ----------
            cont : class
                The frame class that you want to display

            Returns
            -------
            None

            Raises
            ------
            None

            '''

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    '''
          A frame class, with properties inherited from tk.Frame

          Attributes
          ----------
          parent : Class
              The parent class of the program
          controller : object
              The main controller object that has the show_frames method

          Methods
          -------
          signInMethod(controller : object, username : string, password : string)
              Log's into account if account details are correct
          '''

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = 'Sign In', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = tk.Label(self,text = 'Username:')
        label1.pack()
        userName = tk.Entry(self, width=40)
        userName.pack(padx=10)
        label2 = tk.Label(self,text = 'Password:')
        label2.pack(padx=10)
        password1 = tk.Entry(self, width=40)
        password1.pack()

        button1 = ttk.Button(self, text='Sign In', command=lambda: self.signInMethod(controller, userName.get(),password1.get()))
        button1.pack(pady=5)

        button2 = ttk.Button(self, text= 'Create an account', command = lambda: controller.show_frame(SignUpPage))
        button2.pack(pady=5)

    def signInMethod(self,controller, username,password):
        '''
            Sign's into user's account

            Checks the attempted password with the set password and ensure they are equal before logging in and then changing the frame to the user's accoutn

            Parameters
            ----------
            controller : object
                The controller object so that the method can change frames
            username : string
                The username entered by the user to log in
            password : string
                The password entered by the user to log in

            Returns
            -------
            String

            Raises
            ------
            None

            '''

        if username == '' or password == '':
            return("Please fill out all fields")
        else:
            if user.signInPortal(username,password) == True:
                controller.show_frame(UserAccount)
            else:
                return("Get yeeted")

class SignUpPage(tk.Frame):
    '''
          A frame class, with properties inherited from tk.Frame

          Attributes
          ----------
          parent : Class
              The parent class of the program
          controller : object
              The main controller object that has the show_frames method

          Methods
          -------
          createObject(controller : object, userName : string, password1 : string, password2 : string)
              Creates a new user
          '''

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = 'Sign Up', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = tk.Label(self,text = 'Username:')
        label1.pack()
        userName = tk.Entry(self, width=40)
        userName.pack(padx=10)
        label2 = tk.Label(self,text = 'Password:')
        label2.pack(padx=10)
        password1 = tk.Entry(self, width=40)
        password1.pack()
        label3 = tk.Label(self,text = 'Confirm Password:')
        label3.pack(padx=10)
        password2 = tk.Entry(self, width=40)
        password2.pack()

        button1 = ttk.Button(self, text='Create your account', command=lambda: self.createObject(controller,userName.get(),password1.get(),password2.get()))
        button1.pack(pady=5)

        button2 = ttk.Button(self, text= 'Already have an account?', command = lambda: controller.show_frame(StartPage))
        button2.pack(pady=5)

    def createObject(self,controller,userName,password1,password2):
        '''
            Creates a new user

            If the input requirments are all correct it will create a new user object with the given inputs

            Parameters
            ----------
            controller : object
                The controller object so that the method can change frames
            userName : string
                The username entered by the user to sign up
            password1 : string
                The password entered by the user to sign up
            password2 : string
                The password entered by the user to sign up

            Returns
            -------
            Boolean

            Raises
            ------
            None

            '''
        if user.objectCreator(userName,password1,password2) == True:
            controller.show_frame(UserAccount)


class UserAccount(tk.Frame):
    '''
          A frame class, with properties inherited from tk.Frame

          Attributes
          ----------
          parent : Class
              The parent class of the program
          controller : object
              The main controller object that has the show_frames method

          Methods
          -------
          callBackOne() :
              Allows user to select image from computer
          callBackTwo():
              Allows user to select image from computer
          displayLabel():
              Runs comparison algorithm and displays a label with the results
          '''

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = 'Welcome', font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(self,text = 'Select image one from:')
        label2.place(x=70, y=40)
        button1 = ttk.Button(self, text='File Explorer', command= self.callBackOne)
        button1.place(x=50, y=65)
        button1alt = ttk.Button(self, text='Image Library', command=self.callBackOne)
        button1alt.place(x=130, y=65)

        label3 = tk.Label(self,text = 'Select image two from:')
        label3.place(x=70, y=90)
        button2 = ttk.Button(self, text='File Explorer', command= self.callBackTwo)
        button2.place(x=50, y=115)
        button2alt = ttk.Button(self, text='Image Library', command=self.callBackOne)
        button2alt.place(x=130, y=115)

        button3 = ttk.Button(self, text='Compare Images!', command= self.displayLabel)
        button3.place(x=75, y=150)

        button4 = ttk.Button(self, text= 'Sign out', command = lambda: [controller.show_frame(StartPage), user.logOut()])
        button4.place(x=90, y=200)

    def callBackOne(self):
        '''
            Selecting image

            Pops up finder and allows them to choose the image they want to compare

            Parameters
            ----------
            None

            Returns
            -------
            None

            Raises
            ------
            None

            '''

        imageOne = str(fd.askopenfile())
        imList1 = imageOne.split("'")
        global imOnePosition
        imOnePosition = imList1[1]
        print(imOnePosition)
        global imageOneSelected
        imageOneSelected = True

    def callBackTwo(self):
        '''
            Selecting image

            Pops up finder and allows them to choose the image they want to compare

            Parameters
            ----------
            None

            Returns
            -------
            None

            Raises
            ------
            None

            '''

        imageTwo = str(fd.askopenfile())
        imList2 = imageTwo.split("'")
        global imTwoPosition
        imTwoPosition = imList2[1]
        print(imTwoPosition)
        global imageTwoSelected
        imageTwoSelected = True

    def displayLabel(self):
        '''
            Displays comparison results

            Runs comparison algorithm and displays a label with the results

            Parameters
            ----------
            None

            Returns
            -------
            String

            Raises
            ------
            None

            '''

        if imageOneSelected == True and imageTwoSelected == True:
            text1 = tk.Label(self, text=str(bk.comparator(imOnePosition, imTwoPosition, 4)))
            text1.place(x=110, y=175)
        else:
            return("Image one not selected")


app = Controller()
app.mainloop()
