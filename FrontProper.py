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
MED_FONT = ("Verdana",10)
SMALL_FONT = ("Verdana",8)

def popupAlert(msg):
    '''
        Pop up message

        Pops up an alert when something goes wrong

        Parameters
        ----------
        msg: Str
            The message that needs to be popped up and displayed

        Returns
        -------
        None

        Raises
        ------
        None

        '''
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=MED_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

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
            popupAlert("Fill out all fields")
        else:
            userList = [line.rstrip('\n') for line in open('objectDirectory.txt')]
            if username not in userList:
                popupAlert("Invalid username")
            elif user.signInPortal(username,password) == True:
                global usersName
                usersName = username
                controller.show_frame(UserAccount)
            else:
                popupAlert("Wrong Password")

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
        result = user.objectCreator(userName,password1,password2)
        if result == True:
            global usersName
            usersName = userName
            controller.show_frame(UserAccount)
        else:
            popupAlert(result)

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
        button1alt = ttk.Button(self, text='Image Library', command=self.callBackOneAlt)
        button1alt.place(x=130, y=65)

        label3 = tk.Label(self,text = 'Select image two from:')
        label3.place(x=70, y=90)
        button2 = ttk.Button(self, text='File Explorer', command= self.callBackTwo)
        button2.place(x=50, y=115)
        button2alt = ttk.Button(self, text='Image Library', command=self.callBackTwoAlt)
        button2alt.place(x=130, y=115)

        button3 = ttk.Button(self, text='Compare Images!', command= self.displayLabel)
        button3.place(x=75, y=150)

        button4 = ttk.Button(self, text= 'Sign out', command = lambda: [controller.show_frame(StartPage), user.logOut()])
        button4.place(x=90, y=200)

    def popupmsg(self):
        '''
            Creates a popup message

            Pops up directory choices and allows them to interact with program

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

        popup = tk.Tk()

        def autoClose():
            '''
                Closes popup

                Destroys the popup automatically after something has been selected

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
            popup.destroy()

        popup.wm_title("!")
        label = ttk.Label(popup, text="Would you like to save image to directory", font=MED_FONT)
        label.pack(side="top", fill='x', pady=8, padx = 5)
        label1 = tk.Label(popup, text='Save under:')
        label1.pack(padx=10)
        saveName = tk.Entry(popup, width=40)
        saveName.pack(padx=10)
        B1 = ttk.Button(popup, text="Save", command=lambda: [self.save1ToDirectory(True, saveName.get()), autoClose()])
        B1.pack(pady=3)
        B2 = ttk.Button(popup, text="Don't Save", command=lambda: [self.save1ToDirectory(False, saveName.get()), autoClose()])
        B2.pack(pady=3)
        popup.mainloop()

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
        global file1
        file1 = imList1[1]
        print(file1)
        global imageOneSelected
        imageOneSelected = True
        global directory1
        directory1 = False
        self.popupmsg()

    def save1ToDirectory(self,save,saveName):
        '''
            Prepares variables to be saved to library

            Is called to save an image to library

            Parameters
            ----------
            save: bool
                Whether or not they want to save the image to library or not
            saveName: str
                The name to be saved under

            Returns
            -------
            None

            Raises
            ------
            None

            '''

        global save1
        save1 = save
        global saveName1
        if save == True:
            fileImageNames = usersName + "_image_names.txt"
            lineList = [line.rstrip('\n') for line in open(fileImageNames)]
            if saveName not in lineList:
                saveName1=saveName
            else:
                saveName1 = False
                popupAlert("That image name already exists")
        if save == False:
            saveName1 = False

    def callBackOneAlt(self):
        '''
            Prepares variables and image from library

            Prepares variable and triggers a pop up to collect image library information

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

        global file1
        file1 = False
        global imageOneSelected
        imageOneSelected = True
        global directory1
        directory1 = True
        global save1
        save1 = False
        self.popupmsgalt()

    def popupmsgalt(self):
        '''
            Creates a popup message

            Pops up directory choices and allows them to interact with program

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
        popup = tk.Tk()

        def autoClose():
            '''
                Closes popup

                Destroys the popup automatically after something has been selected

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
            popup.destroy()

        popup.wm_title("!")
        label = ttk.Label(popup, text="Enter the name you saved the image under", font=MED_FONT)
        label.pack(side="top", fill='x', pady=8, padx = 5)
        saveName = tk.Entry(popup, width=40)
        saveName.pack(padx=10)
        B1 = ttk.Button(popup, text="Enter", command=lambda: [self.directory1name(saveName.get()), autoClose()])
        B1.pack(pady=3)
        B2 = ttk.Button(popup, text="Cancel", command=autoClose)
        B2.pack(pady=3)
        popup.mainloop()

    def directory1name(self,name):
        '''
            Prepares variables

            Is called to create variables to use an image from the image library

            Parameters
            ----------
            name: str
                The name of the image that they saved to the library

            Returns
            -------
            None

            Raises
            ------
            None

            '''
        fileImageNames = usersName + "_image_names.txt"
        lineList = [line.rstrip('\n') for line in open(fileImageNames)]
        if name in lineList:
            global saveName1
            saveName1 = name
        else:
            saveName1=False
            popupAlert("That image doesn't exists")

    def popupmsg2(self):
        '''
            Creates a popup message

            Pops up directory choices and allows them to interact with program

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
        popup2 = tk.Tk()

        def autoClose():
            '''
                Closes popup

                Destroys the popup automatically after something has been selected

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
            popup2.destroy()

        popup2.wm_title("!")
        label = ttk.Label(popup2, text="Would you like to save image to directory", font=MED_FONT)
        label.pack(side="top", fill='x', pady=8, padx = 5)
        label1 = tk.Label(popup2, text='Save under:')
        label1.pack(padx=10)
        saveName = tk.Entry(popup2, width=40)
        saveName.pack(padx=10)
        B1 = ttk.Button(popup2, text="Save", command=lambda: [self.save2ToDirectory(True, saveName.get()), autoClose()])
        B1.pack(pady=3)
        B2 = ttk.Button(popup2, text="Don't Save", command=lambda: [self.save2ToDirectory(False, saveName.get()), autoClose()])
        B2.pack(pady=3)
        popup2.mainloop()

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
        global file2
        file2 = imList2[1]
        print(file2)
        global imageTwoSelected
        imageTwoSelected = True
        global directory2
        directory2 = False
        self.popupmsg2()

    def save2ToDirectory(self,save,saveName):
        '''
            Prepares variables to be saved to library

            Is called to save an image to library

            Parameters
            ----------
            save: bool
                Whether or not they want to save the image to library or not
            saveName: str
                The name to be saved under

            Returns
            -------
            None

            Raises
            ------
            None

            '''
        global save2
        save2 = save
        global saveName2
        if save == True:
            fileImageNames = usersName + "_image_names.txt"
            lineList = [line.rstrip('\n') for line in open(fileImageNames)]
            if saveName not in lineList:
                saveName2 = saveName
            else:
                saveName2 = False
                popupAlert("That image name already exists")
        if save == False:
            saveName2 = False

    def callBackTwoAlt(self):
        '''
            Prepares variables and image from library

            Prepares variable and triggers a pop up to collect image library information

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
        global file2
        file2 = False
        global imageTwoSelected
        imageTwoSelected = True
        global directory2
        directory2 = True
        global save2
        save2 = False
        self.popupmsgalt2()

    def popupmsgalt2(self):
        '''
            Creates a popup message

            Pops up directory choices and allows them to interact with program

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
        popup = tk.Tk()

        def autoClose():
            '''
                Closes popup

                Destroys the popup automatically after something has been selected

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
            popup.destroy()

        popup.wm_title("!")
        label = ttk.Label(popup, text="Enter the name you saved the image under", font=MED_FONT)
        label.pack(side="top", fill='x', pady=8, padx=5)
        saveName = tk.Entry(popup, width=40)
        saveName.pack(padx=10)
        B1 = ttk.Button(popup, text="Enter", command=lambda: [self.directory2name(saveName.get()), autoClose()])
        B1.pack(pady=3)
        B2 = ttk.Button(popup, text="Cancel", command=autoClose)
        B2.pack(pady=3)
        popup.mainloop()

    def directory2name(self, name):
        '''
            Prepares variables

            Is called to create variables to use an image from the image library

            Parameters
            ----------
            name: str
                The name of the image that they saved to the library

            Returns
            -------
            None

            Raises
            ------
            None

            '''
        fileImageNames = usersName + "_image_names.txt"
        lineList = [line.rstrip('\n') for line in open(fileImageNames)]
        if name in lineList:
            global saveName2
            saveName2 = name
        else:
            saveName2= False
            popupAlert("That image doesn't exists")

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
            fileName = usersName + "_image_directory.txt"
            text1 = tk.Label(self, text=str(bk.comparator(usersName,file1, file2, 4, directory1, directory2, save1, saveName1, save2, saveName2, fileName)))
            text1.place(x=1, y=175)
        else:
            popupAlert("Select both images")


app = Controller()
app.mainloop()
