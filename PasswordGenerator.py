# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a #list.

import random


def ExitMethod():  # Method called to ask user if they'd like to exit the program
    print("Would you like to generate another? Enter yes to continue or no to exit")
    ExitChoice = input()
    if ExitChoice in ["yes", "YES", "Yes"]:  # If user enters any of these, then run program again
        Choice = False
        return Choice;
    else:  # Return true to exit the program
        Choice = True;
        return Choice;


SymbolList = ["!", ".",",", "@", "#", "%", "&","/"]  # List of symbols

AlphabetListLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

AlphabetListUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']

Lister = list(range(1, 10))  # List of Numbers

Checker = False;  # Control variable for program

while (Checker == False):

    GeneratedPassword = ""
    print("Welcome to the password generator.")
    print(  "Enter 1 for simple password. (No symbols or numbers)")
    print(" Enter  2 for medium password. (One Number and Upper/Lowercase Letters")
    print(" Enter  3 for strong password (One symbol, One Number, and Letters)")
    print(  "Enter 4 for complex password. (Numbers, symbols, and letters")
    UserInput = int(input())

    print("Enter a number for the size of your Password.")
    PasswordSize = input()
    NumControl = int(0);

    if (UserInput == 1):
        while NumControl != int(PasswordSize):
            GeneratedPassword = GeneratedPassword + random.choice(AlphabetListLower)
            GeneratedPassword = GeneratedPassword + random.choice(AlphabetListUpper)
            if len(GeneratedPassword) >= int(PasswordSize): #Checks to see if the password is greater or equal to the length
                print("Your generated password is ", GeneratedPassword)
                ReturnedChoice = ExitMethod()  # Calls ExitMethod
                if (ReturnedChoice == False):  # If Returned choice is False then run the program again
                    break;
                elif(ReturnedChoice == True):  # Ends program
                    print("Thanks for using the password generator. Don't forget to copy your password! ")
                    quit()
            else:
                NumControl = NumControl + 1

    if(UserInput == 2):
        GeneratedPassword2 = ""
        GeneratedPassword2 = GeneratedPassword2 + random.choice(str(Lister))
        while NumControl != int(PasswordSize):
            GeneratedPassword2 = GeneratedPassword2 + random.choice(AlphabetListLower)
            GeneratedPassword2 = GeneratedPassword2 + random.choice(AlphabetListUpper)
            if len(GeneratedPassword2) >= int(PasswordSize): #Checks to see if the password is greater or equal to the length
                print("Your generated password is ", GeneratedPassword2)
                ReturnedChoice = ExitMethod()  # Calls ExitMethod
                print (ReturnedChoice)
                if (ReturnedChoice == False):  # If Returned choice is False then run the program again
                    break;
                elif (ReturnedChoice == True):  # Ends program
                    print("Thanks for using the password generator. Don't forget to copy your password! ")
                    quit()
            else:
                NumControl = NumControl + 1

    if(UserInput == 3):
        GeneratedPassword3 = ""
        GeneratedPassword3 = GeneratedPassword3 + random.choice(str(Lister))
        GeneratedPassword3 = GeneratedPassword3 + random.choice(SymbolList)
        while NumControl != int(PasswordSize):
            GeneratedPassword3 = GeneratedPassword3 + random.choice(AlphabetListLower)
            GeneratedPassword3 = GeneratedPassword3 + random.choice(AlphabetListUpper)
            if len(GeneratedPassword3) >= int(
                    PasswordSize):  # Checks to see if the password is greater or equal to the length
                print("Your generated password is ", GeneratedPassword3)
                ReturnedChoice = ExitMethod()  # Calls ExitMethod
                print(ReturnedChoice)
                if (ReturnedChoice == False):  # If Returned choice is False then run the program again
                    break;
                elif (ReturnedChoice == True):  # Ends program
                    print("Thanks for using the password generator. Don't forget to copy your password! ")
                    quit()
            else:
                NumControl = NumControl + 1

    if(UserInput == 4):
        GeneratedPassword4 = ""
        while NumControl != int(PasswordSize):
            GeneratedPassword4 = GeneratedPassword4 + random.choice(AlphabetListLower)
            GeneratedPassword4 = GeneratedPassword4 + random.choice(AlphabetListUpper)
            GeneratedPassword4 = GeneratedPassword4 + random.choice(str(Lister))
            GeneratedPassword4 = GeneratedPassword4 + random.choice(SymbolList)
            if len(GeneratedPassword4) >= int(
                    PasswordSize):  # Checks to see if the password is greater or equal to the length
                print("Your generated password is ", GeneratedPassword4)
                ReturnedChoice = ExitMethod()  # Calls ExitMethod
                print(ReturnedChoice)
                if (ReturnedChoice == False):  # If Returned choice is False then run the program again
                    break;
                elif (ReturnedChoice == True):  # Ends program
                    print("Thanks for using the password generator. Don't forget to copy your password! ")
                    quit()
            else:
                NumControl = NumControl + 1


