import pickle
global usernameDirectory
usernameDirectory = []
file = open('objectDirectory.txt', 'a')
file.close()

class User:
    '''
      A class that creates users and has manageability features

      Attributes
      ----------
      password : string
          The user's password that corresponds to their username

      Methods
      -------
      logIn(passwordAttempt: string)
          Log in attempt corresponding to a username
      logOut()
          Logs out of the active user account
      passwordChange(oldPassword: string, newPassword: string)
          Changes the user's password if they correctly enter the previous password
      storeImageLibrary(imageRGB : list, imageName : string)
          Stores RGB of an image in the user's image library under a name for the image
      accessImage(imageName)
      Searches the user's library for an image name and accesses the pircture's RGB
      '''

    def __init__(self, password):
        self.password = password
        self.imageLibrary = {}

    def logIn(self, passwordAttempt):
        '''
            Attempts to log in to user's account

            Checks the attempted password with the set password and ensure they are equal before logging in

            Parameters
            ----------
            passwordAttempt : str
                The password entered by the user to log in

            Returns
            -------
            Boolean

            Raises
            ------
            None

            '''
        if passwordAttempt == self.password:
            return True
        else:
            print("Incorrect password")
            return False

    def logOut(self):
        '''
            Log's out of the user's account

            ..warning:: The rest of the documentation will be here at some point

            '''
        logOut()

    def passwordChange(self, oldPassword, newPassword):
        '''
            Changes a password

            Changes the password of associated with a username if the old password is correctly entered

            Parameters
            ----------
            oldPassword : str
                The previous password entered by the user

        newPassword: str
          The new password entered by the user

            Returns
            -------
            String

            Raises
            ------
            None

            '''

        if self.password == oldPassword:
            if len(newPassword) >= 7:
                self.password = newPassword
            else:
                return ("Password must be at least 7 characters in length")
        else:
            return("Incorrect previous password")

    def storeImageLibrary(self, imageRGB, imageName):
        '''
            Saves an image's RGB

            Takes in a name of the image and the image's RGB and saves it to a dictionary for further use

            Parameters
            ----------
            imageRGB : list
                The RGB of each pixel in the image

        imageName: str
          The name under which the image should be saved

            Returns
            -------
            None

            Raises
            ------
            None

            '''
        if imageName not in self.imageLibrary:
            self.imageLibrary[imageName] = imageRGB
        else:
            overwrite = input("This file already exists, would you like to overwrite the file?")
            if overwrite.lower() == ("yes"):
                self.imageLibrary[imageName] = imageRGB
            else:
                return("Cancelling overwrite")

    def accessImage(self, imageName):
        '''
            Access the RGB of an image

            Searches throught the user's image library for the image name provided and the image is then further used

            Parameters
            ----------
            imageName : str
                The name of the image the user wants to use

            Returns
            -------
            String

            Raises
            ------
            None

            '''
        if imageName in self.imageLibrary:
            return(self.imageLibrary[imageName])
        else:
            return("Image not found")


def objectCreator(inputName,inputPassword,inputPassword2):
    '''
          Creates a new user account

          .. warning:: The rest of the documentation will be here at some point (Front end implementation unfinished).

          '''

    updateObjectDirectory()
    if inputName == '' or inputPassword == '' or inputPassword2 == '':
        print("Don't leave any sections blank")
    elif inputName in usernameDirectory:
        print("Username already exists")
    elif inputPassword != inputPassword2:
        print("Passwords don't match")
    elif len(inputPassword) >= 7:
        globals()[inputName] = User(inputPassword)
        file = open('objectDirectory.txt', 'a')
        if len(usernameDirectory) != 0:
            file.write('\n')
            file.write(inputName)
        else:
            file.write(inputName)
        file.close()
        updateObjectDirectory()
        print("reached the end")
        appOpen()
        return True
    else:
        return("Password must be at least 7 characters in length")


def appOpen():
    updateObjectDirectory()
    print("reached here")
    try:
        for i in usernameDirectory:
            picklefile = open('userObjects', 'rb')
            globals()[i] = pickle.load(picklefile)
            picklefile.close()
    except:
        pass

def logOut():
    '''
          Logs out of the user's account

          .. warning:: The rest of the documentation will be here at some point.
    '''

    picklefile = open('userObjects', 'wb')
    for i in usernameDirectory:
        pickle.dump(globals()[i], picklefile)
    picklefile.close()

def updateObjectDirectory():
    file = open('objectDirectory.txt', 'r')
    text = file.readlines()
    file.close()
    global usernameDirectory
    usernameDirectory = []
    counter = 1
    for i in text:
        if len(text) != counter:
            newLine = i.strip("\n")
            usernameDirectory.append(newLine)
        else:
            usernameDirectory.append(i)
        counter+=1

def signInPortal(username,passwordAttempt):
    return(globals()[username].logIn(passwordAttempt))


print("really?")

