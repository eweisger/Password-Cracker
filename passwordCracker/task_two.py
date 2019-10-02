#Emma Weisgerber
#CSCI 373: Intro to Cyber Security - Dr. Brain Drawert
#Homework 1: Passwords - 1/29/19
#------------------------------------------------------
#Cracks passwords using burte force. For each line in passwords.txt, get the hashed password and pass it to the brute_force function to be cracked.
#All combinatoins of 94 characters, from shortest to longest, up to a maximum length of 20 are attempted by taking the potential password and hashing it
#using the original hashed password as salt, then seeing if the resulting hash matches the one we are looking for.
#Prints the password, password entropy, and time taken to crack the password once found. If the password was not found, print failure.

import itertools
import crypt
import time
import math

def task_two():
    with open("passwords.txt", "r") as user_info:
        for line in user_info:
            user_info = line.rstrip("\r\n").split(":")
            brute_force(user_info[1])


def brute_force(hashed_password):
    character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+={[}]\|<,>.?/:;\"'~`"
    max_length = 20

    print("Cracking password...")
    start_time = time.time()
    for i in range(1, max_length + 1):
        for test_password in itertools.chain(itertools.product(character_set, repeat = i)):
            test_password = ''.join(test_password)
            test_hash = crypt.crypt(test_password, hashed_password)
            if test_hash == hashed_password:
                end_time = time.time()
                entropy = math.log(94, 2)*len(test_password)
                print("Password: " + test_password)
                print("Entropy: {}".format(entropy))
                print("Time: {}".format(end_time - start_time))
                return

    #Failed to crack password, must be longer than 20 characters
    end_time = time.time()
    print("Password was not cracked...")
    print("Time elapsed: {}".format(end_time - start_time))

            
if __name__ == "__main__":
    task_two()

