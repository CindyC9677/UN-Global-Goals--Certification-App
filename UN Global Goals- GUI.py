from guizero import *

def CheckName():
    '''creating window to check for valid name'''
    # creating infographic window, colour of background is indian red
    window=App(width= 300, height= 100, bg= "indian red")
    # text widget
    textbox1=TextBox(window)
    # password enter button
    nameButton= PushButton(window, text="Please enter your full name", command=name, args=[textbox1, window])    
    # displays window
    window.display()
    
def name(textbox1, window):
    ''' Function to check name'''
    # using if statement to determine whether name is valid
    if nameCheck(textbox1):
        # hides windows
        window.hide()
      # opens up passwordWindow
        passwordWindow(window, textbox1)
    else:
        # opens up error page
        window.error(title="ERROR", text="Your name is INVALID!")
      # clearing textbox if error so user can retry
        textbox1.clear()
        
def nameCheck(text0):
    ''' Function check if name is valid'''
    text0=text0.value 
    # using if statement to check to see if the first letter in each word is a capital
    if text0.istitle():
        #using for loop to determine if there is a space and characters from the alphabet in name  
        for x in text0:
            if x.isspace() or x.isalpha():
                return True
            return False        
    
    
    
def passwordWindow(window, name):
    '''Function for password window'''
    # initializing error variable
    error = 0
    # creating window for password checker, colour of background is deep sky blue
    window2=Window(window, width=800, height= 600, bg="deep sky blue")
    # importing welcome picture
    Blank= Picture (window2, image= "Welcome.gif")
    # creating a textbox in window2
    tb=TextBox(window2)
     # password enter button
    passwordButton= PushButton(window2, text="Please enter your password.", command=password, args=[error, window, tb, window2, name])    
    
# password pattern- password must meet these requirements
# 1) password is 7 characters long
# 2) first character is a capital letter
# 3) second and third character is a number
# 4) fourth character is any character
# 5) fifth character is a capital letter
# 6) sixth character is a number
# 7) last character is a exclamation mark

def character1uppercase(word):
    ''' Function that determines if characters are uppercase, returning True or False accordingly'''
    # if statement to check if first character is a capital
    if word[0].isupper():
        # if statement to check if fifth character is a capital
        if word[4].isupper():
            return True
    return False
  
def characterIsDigit(word):
    '''Function that determines if characters are digits, returning True or False accordingly'''
    # if statement to check if character 2 is a digit
    if word[1].isdigit():
        # if statement to check if character 3 is a digit
        if word[2].isdigit():
            #if statement to check if character 6 is a digit
            if word[5].isdigit():
                return True
    return False
      
def exPoint(word):
    '''Function to check if any character is !'''
    # for loop to check if any character= !:
    for character in word:
    # if statement to check if character !, returning True or False accordingly
        if character== "!":    
            return True
    return False
 
def lengthOfWord(word):
    '''Function to check if number of characters in password is right'''
    if len(word) == 7:
        return True
    return False

def passCheck(word):
    '''Function to see if password meets requrements'''
    # using if statement, if all are true, return True, if any is False, return False
    if character1uppercase(word) and characterIsDigit(word) and exPoint(word) and lengthOfWord(word):
        return True
    return False

def passwordAttempt(error, window, tbox, window2, name):
    ''' Function that allows user to attempt password 3 times, and opens up infographic 1 window if password input is right'''
    error += 1
    # if statement to determine if password is right
    if passCheck(tbox.value):
        #hides window2
        window2.hide()
        # opens up infographic 1 window
        info1(window, name)
    # user gets 3 attempts to input correct password
    elif error == 3:
        # error window, displays you have entered password too many times
        window.error(title="ERROR", text="You have entered the password wrong too many times! GOODBYE !") 
        # destroys window
        window.destroy()
    else:
        # if password is wrong, window opens saying error message
        window.error(title="ERROR", text="Your password is WRONG!") 
        passAttemptRepeat(error, window, tbox, window2, name)

def password(error, window, tbox, window2, name):
    '''This function determines if the password is valid'''
    if passCheck(tbox.value):
        # hide window2
        window2.hide()
        # opens up infographic 1
        info1(window, name)
    else: 
        # runs passwordAttempt function
        passwordAttempt(error, window, tbox, window2, name)
        # hides window2
        window2.hide()

def passAttemptRepeat(error, window, tbox, window1, name):
    ''' This function creates the password window '''
    # hide window1
    window1.hide()
    # creating window2 for password window
    window2=Window(window, width=800, height= 600)
    #widgets for welcome/ password page
    #importing welcome picture
    Blank= Picture (window2, image= "Welcome.gif")
    # creating a textbox
    tb=TextBox(window2)
    #password enter button
    passwordButton= PushButton(window2, text="Please enter your password.", command=password, args=[error, window, tb, window2, name])  



#creating function for infographic 1-LifeBelowWater
def info1(window, name):
    '''This function creates the first infographic window'''
    # initializing variable/ score
    score = 0
    # creating window3 to show infographic 1, background colour is DodgerBlue2
    window3=Window(window, width= 600, height= 650, bg="DodgerBlue2")
    # widgets for info1
    # importing picture- LifeBelowWater.gif
    LifeBelowWater= Picture(window3, image="LifeBelowWater.gif")
    # text widget displaying question for infographic 1/ worth 1 point
    text3= Text(window3, text= "How much has ocean acidity increased by since pre-industrial times?")
    # textbox for user to type answer into
    text35= TextBox(window3)
    info1button= PushButton (window3, text= "Submit", command=button3, args= [text35, window, window3, score, name])

def button3(text, window, window3, score, name):
    '''  This function checks the value of the text for the correct answer'''
    # checking to see if text value is the same as the correct answer using an if statement
    if text.value=="26%" or text.value=="26":
        # calculating the score  
        score +=1
        # opening up infographic2 
        info2(window, score, name) 
    else:
        # opening up infographic2
        info2(window, score, name)
    # hides window3, first infographic window
    window3.hide()  
            
            
            
def info2(window, score, name):
    '''This function is for the second infographic window'''
    # creating second infographic window, background colour is turquoise
    window4= Window(window, width= 600, height= 650, bg="turquoise")
    # widgets for info2
    # importing LifeBelowWater2.gif image
    BelowWater= Picture (window4, image="LifeBelowWater2.gif")
    # text displaying second infographic question/ worth 1 point
    text4= Text(window4, text= "Over how many people depend on marine and coastal biodiversity for their livelihood?")
    # textbox for user to type answer into
    text45= TextBox(window4)
    info2button= PushButton (window4, text= "Submit", command=button4, args=[text45, window, window4, score, name])

def button4(text, window, window4, score, name):
    '''  This function checks the value of the text for the correct answer'''
    # checking to see if text value is the same as the correct answer using an if statement
    if text.value=="3 Billion People" or text.value=="3 Billion" or text.value=="3" or text.value=="Three" or text.value=="3 billion" or text.value=="three":
        # calculating the score
        score +=1
        # opens up infographic 3
        info3(window, score, name)
    else:
        # opens up infographic 3
        info3(window, score, name) 
    # hides window4, second infographic window
    window4.hide()   
    
    
    
def info3(window, score, name):
    '''This function is for the third infographic window'''
    # creating the third infographic window, background colour is deep sky blue
    window5= Window(window, width= 700, height= 600, bg="deep sky blue")
    # widgets for info 3
    # importing LifeBelowWater3.gif image
    Water= Picture (window5, image="LifeBelowWater3.gif")
    # text asking third infographic questio/ worth 1 point
    text5= Text(window5, text= "Fill in the blank- The ocean produces over----of the world's oxygen.")
    # textbox user inputs answer in 
    text55=TextBox(window5)
    info3button= PushButton (window5, text= "Submit", command=button5, args=[text55, window, window5, score, name])

def button5(text, window, window5, score, name):
    '''This function checks the value of text for the correct answer'''
     # checking to see if text value is the same as the correct answer using an if statement
    if text.value=="half" or text.value=="50%" or text.value=="1/2" or text.value=="Half" or text.value=="HALF":
        # calculating the score
        score+=1
        # opens up certificate window 
        certificate(text, window, score, name)
        # hides window5
        window5.hide()
    else:
        # opens up certificate window
        certificate(text, window, score, name)
        # hiding window 5, third infographic window
        window5.hide()
    
    
    
def certificate (text, window, score, name):
    '''Function that determines whether person passed or not and issues certificate accordingly'''
    # using if statement to check the score to see if it is higher than 1, issuing a certificate accordingly
    if score>1:
        # widgets for certificate
        # creating the certificate window, background colour is NavajoWhite2
        window6= Window(window, width= 900, height= 525, bg= "NavajoWhite2")
        # importing certificate image.gif
        cert= Picture (window6, image="Certificate.gif")
        # text for if user is certified 
        text6= Text(window6, text="Congratulations " + name.value + "! You are now certified!")
        text7= Text(window6, text=score.value)
         #if score is not higher than 1, text outputs       
    else:
        # widgets for the no pass 
        # creating the no pass window
        window6= Window(window, width= 500, height= 200)
        # text for if the user did not pass
        text65= Text(window6, text=name.value + " you did not pass. Better luck next time!")
        
# calling CheckName function to check for if name is valid to start program
CheckName()

# sample password 
# G90jK3!
