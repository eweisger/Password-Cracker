#Emma Weisgerber
#CSCI 373: Intro to Cyber Securtiy - Dr.Brain Drawert
#Homework 1: Passwords - 1/29/19
#-----------------------------------------------------
#Stores username and password pair. Prompts user to enter username using input and password using getpass, which does not echo their password to stdout. 
#Calculates the entropy of the password and prints it. Hashes the password using crypt and a random salt then appends the hashed password and username
#to a new line in passwords.txt with the format username:hashed_password.

import getpass
import crypt
import math

def task_one():
    print("Enter username: ")
    username = input()
    print("Recieved username: " + username + "\n")

    password = getpass.getpass("Enter password: ")
    print("Recieved password of length {}".format(len(password)))
    
    entropy = math.log(94, 2)*len(password)
    print("Password entropy: {}\n".format(entropy))

    hashed_password = crypt.crypt(password)
    print("Hashed password: {}".format(hashed_password))

    with open("passwords.txt", "a+") as output:
        output.write("{}:{}\n".format(username, hashed_password))

if __name__ == "__main__":
    task_one()
