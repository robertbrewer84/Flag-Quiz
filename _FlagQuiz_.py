
# Robert Brewer (SCN: 070983109)
# The Glasgow Academy
# Advanced Higher Computing Project

# Flag Quiz is, not surprisingly, a flag quiz where users may select a difficulty level and progress
# through 8 questions, gaining points for each question they answer correctly. Once they have completed
# the quiz they will enter their name and their score will be added to a high scores table.

# I believe this program satsfies the requirements for an advanced higher project
# and have therefore included in the commentary where this has been achieved.

import pygame
import copy
import csv
import random
import sys

# Imports the required python modules



def load_screen0 ():
    
    screen = pygame.display.set_mode([1920,1080])
    pygame.display.set_caption("Flag Quiz")
    pygame.mouse.set_visible(True)
    return screen

# Procedure to create the screen where the game will be played



def load_screen1 (screen):

    level = 0
    
    while level == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit() 
                pygame.quit()
                sys.exit()
                quit()
        # Allows the user to quit the program

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Stores the mouse position and any clicks in variables
        
        screen.fill(blue)
        
        TextSurf, TextRect = text_objects("Welcome to my flag quiz!", fontTitle)
        TextRect = (50,50)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Please select a level:", fontText)
        TextRect = (50,150)
        screen.blit(TextSurf, TextRect) # Prints text prompting the user to select a level

        pygame.draw.rect(screen, white,(50,250,800,80)) # Creates a white rectangle which is the outline of the button

        TextSurf, TextRect = text_objects("Level 1", fontText)
        TextRect = (75,275)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Easy", fontText)
        TextRect = (625,275)
        screen.blit(TextSurf, TextRect) # Prints the level number and difficlty which will be selected when this button is clicked
        
        if 50+800 > mouse[0] > 50 and 250+80 > mouse[1] > 250 and click[0] == 1 :
            level = 1 # If the mouse is over the button and a click is stored, the value of level chosen is stored

        pygame.draw.rect(screen, white,(50,400,800,80)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects("Level 2", fontText)
        TextRect = (75,425)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Moderate", fontText)
        TextRect = (625,425)
        screen.blit(TextSurf, TextRect) # Prints the level number and difficlty which will be selected when this button is clicked
        
        if 50+800 > mouse[0] > 50 and 400+80 > mouse[1] > 400 and click[0] == 1 :
            level = 2 # If the mouse is over the button and a click is stored, the value of level chosen is stored

        pygame.draw.rect(screen, white,(50,550,800,80)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects("Level 3", fontText)
        TextRect = (75,575)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Difficult", fontText)
        TextRect = (625,575)
        screen.blit(TextSurf, TextRect) # Prints the level number and difficlty which will be selected when this button is clicked
        
        if 50+800 > mouse[0] > 50 and 550+80 > mouse[1] > 550 and click[0] == 1 :
            level = 3 # If the mouse is over the button and a click is stored, the value of level chosen is stored

        pygame.draw.rect(screen, white,(50,700,800,80) # Creates a white rectangle which is the outline of the button
                         )
        TextSurf, TextRect = text_objects("Level 4", fontText)
        TextRect = (75,725)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Expert", fontText)
        TextRect = (625,725)
        screen.blit(TextSurf, TextRect) # Prints the level number and difficlty which will be selected when this button is clicked
        
        if 50+800 > mouse[0] > 50 and 700+80 > mouse[1] > 700 and click[0] == 1 :
            level = 4 # If the mouse is over the button and a click is stored, the value of level chosen is stored
# Allows the user to quit the program
        pygame.draw.rect(screen, white,(50,850,800,80)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects("Level 5", fontText)
        TextRect = (75,875)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Master", fontText)
        TextRect = (625,875)
        screen.blit(TextSurf, TextRect) # Prints the level number and difficlty which will be selected when this button is clicked
        
        if 50+800 > mouse[0] > 50 and 850+80 > mouse[1] > 850 and click[0] == 1 :
            level = 5 # If the mouse is over the button and a click is stored, the value of level chosen is stored
        
        pygame.display.update()
        clock.tick(24)
        # Repeats this loop at 24 frames per second

    return level

    # Procedure to create a level selection screen and store the level selected by the user




def load_screen2 (screen,level,score):

    question = random.randint(0,19)
    if level == 2 :
        question = question + 20
    elif level == 3 :
        question = question + 40
    elif level == 4 :
        question = question + 60
    elif level == 5 :
        question = question + 80
    # Generates a random question of the difficulty level selected by the user

    answered = False
    time = 0
    helpclick = False
    
    while answered == False and time < 360 :

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Stores the mouse position and any clicks in variables
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit() 
                pygame.quit()
                sys.exit()
                quit()
            # Allows the user to quit the program
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if 200+250 > mouse[0] > 200 and 600+100 > mouse[1] > 600 :
                    answered = True # If the mouse is over the button and a click is stored, the loop is broken
                    if flagdata[question].correctoption == 1:
                        score = score + 10 # If the user answer is correct, they gain 10 points

                elif 500+250 > mouse[0] > 500 and 600+100 > mouse[1] > 600 :
                    answered = True # If the mouse is over the button and a click is stored, the loop is broken
                    if flagdata[question].correctoption == 2:
                        score = score + 10 # If the user answer is correct, they gain 10 points

                elif 200+250 > mouse[0] > 200 and 750+100 > mouse[1] > 750 :
                    answered = True # If the mouse is over the button and a click is stored, the loop is broken
                    if flagdata[question].correctoption == 3:
                        score = score + 10 # If the user answer is correct, they gain 10 points

                elif 500+250 > mouse[0] > 500 and 750+100 > mouse[1] > 750 :
                    answered = True # If the mouse is over the button and a click is stored, the loop is broken
                    if flagdata[question].correctoption == 4:
                        score = score + 10 # If the user answer is correct, they gain 10 points
                # VALIDATES ALL INPUTS AS REQUIRED
                
                elif 1000+250 > mouse[0] > 1000 and 600+250 > mouse[1] > 600 :
                    helpclick = True # Causes help text to be displayed if the text button is clicked
        
        screen.fill(blue)

        flag = pygame.image.load(flagdata[question].image)
        screen.blit(flag,(200,100))

        pygame.draw.rect(screen, white,(200,600,250,100)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects((flagdata[question].option1), fontOptions)
        TextRect.center = (325,650)
        screen.blit(TextSurf, TextRect) # Prints option1 for this question
        
        pygame.draw.rect(screen, white,(500,600,250,100)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects((flagdata[question].option2), fontOptions)
        TextRect.center = (625,650)
        screen.blit(TextSurf, TextRect) # Prints option2 for this question
    
        pygame.draw.rect(screen, white,(200,750,250,100)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects((flagdata[question].option3), fontOptions)
        TextRect.center = (325,800)
        screen.blit(TextSurf, TextRect) # Prints option3 for this question

        pygame.draw.rect(screen, white,(500,750,250,100)) # Creates a white rectangle which is the outline of the button
        
        TextSurf, TextRect = text_objects((flagdata[question].option4), fontOptions)
        TextRect.center = (625,800)
        screen.blit(TextSurf, TextRect) # Prints option4 for this question

        TextSurf, TextRect = text_objects("Level:", fontText)
        TextRect = (1000,150)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(level), fontText)
        TextRect = (1000,220)
        screen.blit(TextSurf, TextRect)
        # Prints the level that the user is attempting

        TextSurf, TextRect = text_objects("Score:", fontText)
        TextRect = (1000,290)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(score) + " points", fontText)
        TextRect = (1000,360)
        screen.blit(TextSurf, TextRect)
        # Prints the user's current score

        TextSurf, TextRect = text_objects("Time:", fontText)
        TextRect = (1000,430)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(int((360-time)/24)), fontText)
        TextRect = (1000,500)
        screen.blit(TextSurf, TextRect)
        # Prints the number of seconds the user has remaining on the current question

        pygame.draw.rect(screen, white,(1000,600,250,250))
        if helpclick == False :
            TextSurf, TextRect = text_objects("HELP", fontTitle)
            TextRect.center = (1125,650)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("?", fontTitle)
            TextRect.center = (1125,750)
            screen.blit(TextSurf, TextRect)
            # Prints a help button for if the user is stuck
        else :
            TextSurf, TextRect = text_objects("You can answer the", fontOptions)
            TextRect.center = (1125,620)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("question by clicking", fontOptions)
            TextRect.center = (1125,660)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("any of the 4 options", fontOptions)
            TextRect.center = (1125,700)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("before time runs out", fontOptions)
            TextRect.center = (1125,740)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects("<--", fontTitle)
            TextRect.center = (1125,790)
            screen.blit(TextSurf, TextRect)
            # Prints help text if the help button has been clicked

        time = time + 1

        pygame.display.update()
        clock.tick(24)
        # Repeats this loop at 24 frames per second

    return score

    # Procedure to display the current question and receive the user's answer



def load_screen3 (screen):

    entered = False
    invalid = False
    username = ""

    while entered == False : 
                    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        # Stores the mouse position and any clicks or key presses in variables
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit() 
                pygame.quit()
                sys.exit()
                quit()
            # Allows the user to quit the program
            elif event.type == pygame.KEYDOWN:
                if ("a" <= event.unicode <= "z" or "0" <= event.unicode <= "9" or "A" <= event.unicode <= "Z") :
                    character = event.unicode
                    username = username + character
                # If the user types a character or number it is stores as part of their username
                if event.unicode == "\b" :
                    username = username[0:len(username)-1]
                # If the user types a backspace the last entered number or character is removed from username

                # VALIDATES ALL INPUTS AS REQUIRED

        screen.fill(blue)

        if invalid == True :
            TextSurf, TextRect = text_objects("Please enter a valid name", fontText)
            TextRect = (760,240)
            screen.blit(TextSurf, TextRect)
        # If the user has entered a name that is 0 or over 20 characters, an error message is displayed
    
        TextSurf, TextRect = text_objects("Please enter your name:", fontText)
        TextRect = (760,440)
        screen.blit(TextSurf, TextRect)
        # Text to prompt the user to input their name
        
        pygame.draw.rect(screen, white,(760,490,400,100)) # Creates a white rectangle which is the outline of the text input box
        TextSurf, TextRect = text_objects(username, fontText)
        TextRect = (760,520)
        screen.blit(TextSurf, TextRect) # Displays the username currently entered by the user

        pygame.draw.rect(screen, white,(1200,490,100,100)) # Creates a white rectangle which is the outline of the button
        TextSurf, TextRect = text_objects("GO!", fontOptions)
        TextRect.center = (1250,540)
        screen.blit(TextSurf, TextRect) # Prints text to imply that this button submits their username
        
        if 1200+100 > mouse[0] > 1200 and 490+100 > mouse[1] > 490 and click[0] == 1 : # If the mouse is over the button...
            if 0 < len(username) < 21 :
                entered = True
            # If the username is valid, the loop is broken
            else :
                invalid = True
                username = ""
            # If the username is not valid, it is reset and invalid is changed so an error message will be displayed
    
        pygame.display.update()
        clock.tick(24)
        # Repeats this loop at 24 frames per second

    return username

    # Procedure to receive the user's name

    

def load_screen4 (screen, topten, userscore, level):

    active = True
    
    while active == True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.unicode == "q" or event.unicode == "Q")):
                active = False
         # Allows the user to quit the program
        
        screen.fill(blue)

        TextSurf, TextRect = text_objects("Level " + str(level) + " High Scores", fontTitle)
        TextRect = (50,50)
        screen.blit(TextSurf, TextRect)
        # Prints a title for the page

        TextSurf, TextRect = text_objects("Nickname", fontText)
        TextRect = (50,150)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Answers Correct", fontText)
        TextRect = (450,150)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Answers Incorrect", fontText)
        TextRect = (800,150)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Percent Correct", fontText)
        TextRect = (1150,150)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Score", fontText)
        TextRect = (1500,150)
        screen.blit(TextSurf, TextRect)
        # Prints headings for each column of the high scores table
    
        y = 250
    
        for index in range (10):
            TextSurf, TextRect = text_objects(topten[index].nickname, fontText)
            TextRect = (50,y)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects(str(topten[index].acorrect), fontText)
            TextRect = (450,y)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects(str(topten[index].aincorrect), fontText)
            TextRect = (800,y)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects((str(topten[index].pcorrect) + "%"), fontText)
            TextRect = (1150,y)
            screen.blit(TextSurf, TextRect)
            TextSurf, TextRect = text_objects(str(topten[index].score), fontText)
            TextRect = (1500,y)
            screen.blit(TextSurf, TextRect)
            y = y + 50
        # Loops 10 times to print the details for each of the top 10 scores

        TextSurf, TextRect = text_objects("________________________________________________________________________________________", fontText)
        TextRect = (50,750)
        screen.blit(TextSurf, TextRect)
        # Draws a long line
    
        TextSurf, TextRect = text_objects(userscore.nickname, fontText)
        TextRect = (50,850)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(userscore.acorrect), fontText)
        TextRect = (450,850)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(userscore.aincorrect), fontText)
        TextRect = (800,850)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects((str(userscore.pcorrect) + "%"), fontText)
        TextRect = (1150,850)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects(str(userscore.score), fontText)
        TextRect = (1500,850)
        screen.blit(TextSurf, TextRect)
        # Prints the details for the current user's attempt

        pygame.display.update()

    #Procedure to display the top 10 scores and the current user's score

        
    
def text_objects(text, font):
    
    textSurface = font.render(text, True, black)
    
    return textSurface, textSurface.get_rect()

# Procedure to convert text to displayable format given the text to be displayed and font

    

class question:
    
    def __init__(self,image,option1,option2,option3,option4,correctoption):
            
        self.image = image
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctoption = correctoption

# Creates a record structure to store the question details

    
                    
def loadflags():

    image = []
    option1 = []
    option2 = []
    option3 = []
    option4  = []
    correctoption = []
    # Creates empty arrays for data to be stored
    
    progfile = open("data/Questions.csv","r")
    reader = csv.reader(progfile)
    # Opens the file containing the questions
    
    for row in reader:
        image.append("data/flags/" + row[0])
        option1.append(row[1])
        option2.append(row[2])
        option3.append(row[3])
        option4.append(row[4])
        correctoption.append(int(row[5]))
        # Stores the details from each row in the questions file
        
    progfile.close()
    # Closes the file
    
    flagdata = []    
    for index in range (100) :
        indexquestion = question(image[index],option1[index],option2[index],option3[index],option4[index],correctoption[index])
        flagdata.append(indexquestion)
    # Combines the arrays to store the question details as an array of records
        
    return flagdata

# Procedure to import the questions data into an array of records
# INTERFACES WITH STORED DATA
# ARRAY OF RECORDS



class scoredata:
    
    def __init__(self,nickname,acorrect,aincorrect,pcorrect,score):
        
            self.nickname = nickname
            self.acorrect = acorrect
            self.aincorrect = aincorrect
            self.pcorrect = pcorrect
            self.score = score

# Creates a record structure to store the details of each score

    

def loadhighscores():

    nickname = []
    acorrect = []
    aincorrect = []
    pcorrect = []
    score  = []
    # Creates empty arrays for data to be stored
    
    progfile = open("data/highscores.txt","r")
    reader = csv.reader(progfile)
    # Opens the file containing the scores
     
    for row in reader:
        nickname.append(row[0])
        acorrect.append(int(row[1]))
        aincorrect.append(int(row[2]))
        pcorrect.append(int(row[3]))
        score.append(int(row[4]))
        # Stores the details from each row in the highscores file
        
    progfile.close()
    # Closes the file
    
    highscores = []
    for index in range(len(nickname)):
        indexscore = scoredata(nickname[index],acorrect[index],aincorrect[index],pcorrect[index],score[index])
        highscores.append(indexscore)
    # Combines the arrays to store the score details as an array of records
        
    return highscores

# Procedure to import the scores data into an array of records
# INTERFACES WITH STORED DATA
# ARRAY OF RECORDS



def arraysort(highscores):
    
    topten = []
    # Creates an empty array to store the top ten scores
    
    for outer in range (10):
        
        maximum = highscores[0].score
        position = 0
        # Sets the maximum score to the value of the first index of the array
        
        for inner in range (1,len(highscores)):
            if highscores[inner].score > maximum :
                maximum = highscores[inner].score
                position = inner
            elif highscores[inner].score == maximum :
                if highscores[inner].nickname < highscores[position].nickname :
                    position = inner
            # Finds the position of the highest value of score in the array
                    
        topten.append(copy.copy(highscores[position]))
        # Appends the details for the highest score to the topten array
        
        highscores[position].nickname = ""
        highscores[position].acorrect = 0
        highscores[position].aincorrect = 0
        highscores[position].pcorrect = 0
        highscores[position].score = 0
        # Replaces the values where the maximum was with dummy values so it is not found again
        
    return topten

# Procedure to find the 10 highest scores and store them in an array called topteN
# SORT ALGORITHM
# ARRAY OF RECORDS

    

# Main Program



pygame.init()
# Initialises pygame

black = (0,0,0)
white = (255,255,255)
blue = (127, 172, 244)
fontTitle = pygame.font.Font(None, 100)
fontText = pygame.font.Font(None, 48)
fontOptions = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
# Defines the colours, fonts and timer used by the game

flagdata = loadflags()
# Runs the procedure to load the questions from an external file

screen = load_screen0()
# Runs the procedure to create the screen where the game will be played

level = load_screen1(screen)
# Runs the procedure to receive the user's choice of level

score = 0

for index in range (8):
    score = load_screen2(screen,level,score)
    pygame.time.wait(250)
# Runs the procedure that displays a question 8 times

username = load_screen3(screen)
# Runs the procedure which receives the user's name

highscores = loadhighscores()
# Runs the procedure to load the scores from an external file

acorrect = int(score/10)
aincorrect = int((80-score)/10)
pcorrect = int((score/80)*100 + 0.5)
# Calculates the other details for the current user's score

progfile = open("highscores.txt","a")
progfile.write("\n" + username + "," + str(acorrect) + "," + str(aincorrect) + "," + str(pcorrect) + "," + str(score))
progfile.close()
# Opens the scores file, writes the current user's score to it, then closes it

userscore = scoredata(username,acorrect,aincorrect,pcorrect,score)
# Stores the current user's details in a record

highscores.append(copy.copy(userscore))
# Adds the current user's score to the highscores array

topten = arraysort(highscores)
# Runs the procedure to find the ten highest scores

load_screen4(screen,topten,userscore,level)
# Runs the procedure to display the high scores table

pygame.display.quit() 
pygame.quit()
sys.exit()
quit()
# Quits the program
