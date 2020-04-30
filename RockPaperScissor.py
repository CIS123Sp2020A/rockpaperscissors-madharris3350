#Madison Harris

#Complete an algorithm for the Rock Paper Scissors GUI.
#Be sure to detail inputs, outputs, widgets used, and any calculations needed

#import tkinter

#import random

#create radio button labeled rock, paper, and scissors

#create play and quit buttons

#computer selects rock(0) paper(1) or scissors(2) 
#display with user selection(message box)

#create if/else statement around if the plaer wins or nnot attach the
#text to tell their moves (message box)

#rock beats scissors
#paper beats rock
#scissors beat paper

import tkinter
import tkinter.messagebox as box

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the intVar object to 1.
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable=self.radioVar, value='Scissors')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        

        # Set up buttons
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    def showOption(self):
        import random
        computer = random.randint(0,2)
        if computer == 0:
            computerOption = "Rock"
        if computer == 1:
            computerOption = "Paper"
        if computer == 2:
            computerOption = "Scissors"
            
        box.showinfo('Selection', 'You selected ' + self.radioVar.get() +
                                    '\nComputer selected ' + computerOption)
        

#I couldnt figure out the second part
##    def showWinner(self):
##        winner = "none"
##        if computerOption == "Rock" and self.radioVar == "Scissors":
##        if computerOption == "Paper" and self.radioVar == "Rock":
##        if computerOption == "Scissors" and self.radioVar == "Paper":
##            
##
##        if computerOption == "Scissors" and self.radioVar == "Rock":
##        if computerOption == "Rock" and self.radioVar == "Paper":
##        if computerOption == "Paper" and self.radioVar == "Scissors":
##
##        if computerOption == "Rock" and self.radioVar == "Rock":
##        if computerOption == "Paper" and self.radioVar == "Paper":
##        if computerOption == "Scissors" and self.radioVar == "Scissors":
            
        
            



    #self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        
       # if computerOption == "Rock" and self.radioVar == "Paper":
            

        

demoGUI = MyGUI()
