from guizero import *

#right click- press end to, compress
#def checkCapital (fullName):
  #'''This function checks to see if the first character is a capital'''
  #if name.isalpha() == True and name == name.capitalize():
    #return True
  #else:
    #return False    
  
#def checkName(fullName):
    #'''This function checks to see if all the characters are letters'''
    #if fullName.isalpha()==True:
        #return True
    #else:
        #return False
## creating function for checking name
#def name():
  #'''main function'''
  ##user inputs name
  #firstName= input("Please enter your name: ")
  #variable1 = checkName (fullName)
  #variable2= checkCapital (fullName)  
  
  #lastName= input("Please enter your last name: ")
  
  #if variable1==True and variable2==True:
    #print ("Nice! Your name is valid")
  #else:
    #print ("Invalid. Please try again.")

#name()    

#creating function for infographic 1-LifeBelowWater
def CheckName():
    '''creating window to check for valid name'''
    window=App(width= 300, height= 100)
    textbox1=TextBox(window)
    #password enter button
    nameButton= PushButton(window, text="Please enter your full name", command=name, args=[textbox1, window])    
    window.display()
    
def name(textbox1, window):
    ''' Function to check name'''
    # using if statement to determine whether value is valid
    # if nameCheck(textbox1):-might need    
    if nameCheck(textbox1):
      window.hide()
      passwordWindow(window, textbox1)
    else:
      window.error(title="ERROR", text="Your name is INVALID!")
        
    # making password pattern
def nameCheck(text0):
    text0=text0.value 
    if text0.istitle:
      for x in text0:
        if x.isspace() or x.isalpha():
          return True
        return False        
    
def passwordWindow(window, name):
    '''Function for password window'''
    window2=Window(window, width=800, height= 600)
    #importing welcome picture
    Blank= Picture (window2, image= "Welcome.gif")
    tb=TextBox(window2)
     #password enter button
    passwordButton= PushButton(window2, text="Please enter your password. Please minimize this page after entering password. Password is there for reference", command=password, args=[window, tb, name])    
    
#password pattern- password must meet these requirements
# password is 5 characters long
# first character is a capital letter
# second and third character is a number
# fourth character is any character
# last character is a capital letter

    # making password pattern
def passCheck(word):
    if word[0].isupper() and word[1].isdigit() and word[2].isdigit() and word[4].isupper():
      return True
    return False

def password(window, tbox, window2):
# to check for specific characters
    if passCheck(tbox.value):
      info1(window, name)
    else:        
      window.error(title="ERROR", text="Your password is WRONG!")
     


def info1(window, name):
    '''creating first infographic window'''
    score = 0
    window3=Window(window, width= 600, height= 1500)
    LifeBelowWater= Picture(window3, image="LifeBelowWater.gif")
    text3= Text(window3, text= "How much has ocean acidity increased by since pre-industrial times?")
    text35= TextBox(window3)
    info1button= PushButton (window3, text= "Submit", command=button3, args= [text35, window, window3, score, name])


def button3(text, window, window3, score, name):  
  if text.value=="26%" or text.value=="26":
    score +=1
    info2(window, score, name) 
  else:
    info2(window, score, name)
  window3.hide()  
            
   
def info2(window, score, name):
    '''creating second infographic window'''
    window4= Window(window, width= 600, height= 1500)
    BelowWater= Picture (window4, image="LifeBelowWater2.gif")
    text4= Text(window4, text= "Over how many people depend on marine and coastal biodiversity for their livelihood?")
    text45= TextBox(window4)
    info2button= PushButton (window4, text= "Submit", command=button4, args=[text45, window, window4, score, name])

def button4(text, window, window4, score, name):          
  if text.value=="3 Billion People" or text.value=="3 Billion" or text.value=="3" or text.value=="Three" or text.value=="3 billion" or text.value=="three":
    score +=1
    info3(window, score, name)
  else:
    info3(window, score, name) 
  window4.hide()   
 
    
def info3(window, score, name):
    '''creating third infographic window'''
    window5= Window(window, width= 600, height= 800)
    Water= Picture (window5, image="LifeBelowWater3.gif")
    text5= Text(window5, text= "Fill in the blank- The ocean produces over----of the world's oxygen.")
    text55=TextBox(window5)
    info3button= PushButton (window5, text= "Submit", command=button5, args=[text55, window, window5, score, name])

def button5(text, window, window5, score, name):
    '''check the value of textbox 4 for the correct answer'''
    if text.value=="half" or text.value=="50%" or text.value=="1/2" or text.value=="Half" or text.value=="HALF":
        score+=1
        certificate(text, window, score, name)
        window6.hide()
    else:
        certificate(text, window, score, name)
        window6.hide()
    
def certificate (text, window, window6, score, name):
    '''Function that determines whether person passed or not and issues certificate accordingly'''
    #check the score to see if higher than 1
    if score>1:
        text6= Text(window6, text="Congratulations! You are now certified!")
        window6= Window(window, width= 600, height= 800)
        cert= Picture (window6, image="Certificate.gif")        
    else:
        text65= Text(window6, text="You did not pass. Better luck next time!")
        
        
        
        
    
    
    
CheckName()
nameCheck(textbox1)
name(textbox1)




#so basically I can like run it and it'll open up the password window and let me type password in, but when i press submit it like gives me error, stuff not defined, WHEN I DEFINED ITTTTT, and it's like supposed to go to password when it confirms the name is valid but since it gives error, that no happen, i shall send u screenshots now of what's showing up.