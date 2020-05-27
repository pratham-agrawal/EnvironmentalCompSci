import pickle
global usernameDirectory
usernameDirectory = []
file = open('objectDirectory.txt', 'a')
file.close()

class User:
    def __init__(self, password):
        '''
            Constructor to build a user object

            Parameters
            ----------
            password : str
                The password required to access the user's account

            '''

        self.password = password
        self.imageLibrary = {}

    def logIn(self, passwordAttempt):
        if passwordAttempt == self.password:
            logIn(self)
        else:
            print("Incorrect password")

    def logOut(self):
        logOut(self)

    def check(self):
        print("THE OBJECT WORKS!!!!!!!!!")

def objectCreator():
    updateObjectDirectory()
    inputName = input("Enter a username: ")
    inputPassword = input("Enter a password: ")
    if inputName in usernameDirectory:
        print("Username already exists")
    else:
        if len(inputPassword) >= 7:
            globals()[inputName] = User(inputPassword)
            file = open('objectDirectory.txt', 'a')
            if len(usernameDirectory) != 0:
                file.write('\n')
                file.write(inputName)
            else:
                file.write(inputName)
            file.close()
            updateObjectDirectory()
            logIn(inputName)
        else:
            print("Password must be at least 7 characters in length")


def logIn(username):
    '''
    try:
        picklefile = open('userObjects', 'rb')
        userObjects = pickle.load(picklefile)
        picklefile.close()
        print(userObjects)
        print("legit")
        counter = 0
        for i in userObjects:
            if str(i) == username:
                globals()[username] = userObjects[counter]
                print(globals()[username])
            counter+=1
    except:
        print("First User")'''
    updateObjectDirectory()
    try:
        for i in usernameDirectory:
            picklefile = open('userObjects', 'rb')
            globals()[i] = pickle.load(picklefile)
            picklefile.close()
    except:
        print("skipped")

def logOut(username):
    '''
    counter = 0
    new = False
    for i in userObjects:
        if str(i) == username:
            userObjects[counter] = globals()[username]
            new = True
        counter +=1
    if new == False:
        userObjects.append(globals()[username])
    print (userObjects)
    picklefile = open('userObjects', 'wb')
    pickle.dump(userObjects, picklefile)
    picklefile.close()'''

    picklefile = open('userObjects', 'wb')
    for i in usernameDirectory:
        print("dumped")
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

