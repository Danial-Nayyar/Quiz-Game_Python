#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#Danial Nayyar, [30/12/2021 15:54]
#Quiz Game, Fixed it, The spacing after the question input and then the answer was the issue. Removed the spaces in between the speech marks and "word" in the if statements
# For some reason, the if statement only takes one input either "Yes" or "Y", adding the 'or' function didn't work, it resulted in the program following the 'if' path. 
# regardless of the input being entered, even if it is "n", the program continues like "Y" or "yes" were entered.
# However removing the 'or' option made it run as it was supposed to.
# The quiz is now finished completely. No more updates need to be done! unless wanna change questions etc.
# The code works the way it should.
#Properly.
# The code was officially finished at 17:50 Tuesday 29/06/2021.


print("""
Hello! Welcome to the Quiz. This quiz has multiple questions, each worth one point each.
 To win, the contestant must have a minimum of 6 correct answers. 
 There are 7 questions. Each incorrect answer is -1 point
 Each question is part of a different category. Good Luck! Don't Fail!
""")

score = 0 
name_of_player_one = input("What is your name? ").upper()
user_input = input(str(name_of_player_one ) + """ Are you ready to play? 
Y or N
""").upper()


if user_input == "Y":
    print ("Great! Get Ready!")
    print ("Starting Score = " +str(score))   
    question =input(""" Question 1 is... Who is the best superhero in the MCU? 

              A) Iron Man
              B) Captain Atom
              C) Ant Man
              D) Batman
    """).upper()
    if question == "IRON MAN":
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "A":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print ("No answer detected...")
        print("""The Correct answer is:
         A) Iron Man""")
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!")
        print(""" The Correct answer is: 
        A) Iron Man""") 
        score -=1 
        print("Score : "+str(score))

    question =input(""" Question 2: Who invented Python
    
                A) Naruto
                B) Garfield
                C) Guido van Rossum
                D) No One
     """).upper()
    if question == "Guido van Rossum" :
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "Guido":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "C":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print ("No answer detected...")
        print("""The Correct answer is:
         C) Danial Nayyar""")
        score -=1
        print("Score : "+str(score))
    elif question == "D":
        print( "Think... That can't be right")
        print ("""The correct answer is:
        C) Guido van Rossum""")
    else:
        print("Incorrect!") 
        print("""The Correct answer is:
         C) Guido van Rossum""")
        score -=1    
        print("Score : "+str(score))

    question =input(""" Question 3 ... Who was the first avenger? 
                
                A) Captain Marvel
                B) Captain America
                C) Nick Fury
                D) Black Widow
      """).upper()
    if question == "CAPTAIN AMERICA" :
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "B":
        print ("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print ("No answer detected...")
        print("""The correct answer is: 
        B) Captain America""")
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!") 
        print("""The Correct answer is: 
        B) Captain America""")
        score -=1
        print("Score : "+str(score))

    question =input(""" Question 4: Playstation 5 was made by?
               A) LG
               B) Samsung
               C) Apple
               D) Sony
    """).upper()
    if question == "SONY" :
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "D":
        print("Correct !")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print("No answer detected...")
        print("""The Correct answer is:
         D) Sony """)
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!") 
        print("""The Correct answer is:
        D) Sony""")
        score -=1
        print("Score : "+str(score))

    question =input(""" Question 5: Who is the A.I. made by Tony Stark for Peter Parker in Spiderman Far From Home? 
    
                A) EDITH
                B) Friday
                C) Saturday
                D) Robert 
    """).upper()
    if question == "EDITH" :
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "A":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print("No input detected...")
        print("""The correct answer is:
         A) EDITH""")
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!") 
        print("""The Correct answer is: 
        A) EDITH""")
        score -=1
        print("Score : "+str(score))

        
    question =input(""" Question 6: Who is the Tony's AI in Infinity War and Endgame? 
                A) Sunday 
                B) Sam
                C) Friday
                D) Tom
    """).upper()
    if question == "FRIDAY" :
        print("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "C":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == "":
        print("No input detected...")
        print("""The correct answer is:
         C) Friday""")
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!") 
        print("""The Correct answer is:
         C) Friday""")
        score -=1
        print("Score : "+str(score))

    question = input(""" Question 7: Who invented C++
                A) Guido van Rossum
                B) Iron Man
                C) Dave Chapelle
                D) Bjarne Stroustrup
     """).upper()
    if question == "Bjarne Stroustrup":
        print ("Correct!")
        score += 1
        print("Score : "+str(score))
    elif question == "D":
        print("Correct!")
        score +=1
        print("Score : "+str(score))
    elif question == " ":
        print("""The correct answer is:
         D) Bjarne Stroustrup""")
        score -=1
        print("Score : "+str(score))
    else:
        print("Incorrect!")
        print("""The Correct answer is: 
        D) Bjarne Stroustrup """)
        score -=1
        print("Score : "+str(score))

    print ("All questions are finished, Congrats")
    print ("You got" , score , "out of the 7 possible points... ")
    print ("That is ", round((score /7 *100)), "%")
    if score>= 6:
        print ("Well Done! You passed "+ str(name_of_player_one))
    elif score == 6:
        struggle = (""" You just met, the minimum requirement...
        Did you struggle
        Y or N
        """).input
        if struggle == "Y":
            print ("You should try again")
        elif struggle == "N":
            print(" You sure, you were one mark of failing this quiz")
        else:
            print("""None of the options were picked.
            Have a good day then
            """)

    else:
        print (str(name_of_player_one)+
        """ You Failed 
        The minimun requirement was 6 points 
        You got """ +str(score)+ " points")

elif user_input == "N":
    print("Understood, Play another time!")
else:
    print ("Bye!") 
    print ("Input requirements not met!") and quit()