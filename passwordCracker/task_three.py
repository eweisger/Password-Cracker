#Emma Weisgerber
#CSCI 373: Intro to Cyber Security - Dr. Brian Drawert
#Homework 1: Passwords - 1/29/19
#------------------------------------------------------
#Cracks passwords using dictionary attack. For each line in passwords.txt, get the hashed password and pass it to the dictionary_attack function to be cracked.
#Attempts every word in a dictionary, from shortest to longest by taking the word and hashing it using the original hashed password as salt,
#then seeing if the resulting hash matches the one we are looking for.
#If none of the dictionary words work, attempt all variations of single, common character substitutions of letters for each word with use of the swap function.
#If none of the single substitutions work, attempt all variations of two, common character subsitiutions of letters for each word with use of the swap function.
#Prints the password, password entropy, and time taken to crack the password once found. If the password was not found, print failure.

import crypt
import time
import math

def task_three():
    with open("passwords.txt", "r") as user_info:
        for line in user_info:
            user_info = line.rstrip("\r\n").split(":")
            dictionary_attack(user_info[1])


def dictionary_attack(hashed_password):
    print("Cracking password...")
    start_time = time.time()
    #Attempt every dictionary word
    with open("dictionary_sorted.txt", "r") as dictionary:
        for word in dictionary:
            test_password = word.rstrip("\r\n")
            test_hash = crypt.crypt(test_password, hashed_password)
            if test_hash == hashed_password:
                end_time = time.time()
                entropy = math.log(94, 2)*len(test_password)
                print("Password: " + test_password)
                print("Entropy: {}".format(entropy))
                print("Time: {}".format(end_time - start_time))
                return

    #Attempt all variations of single, common character substituitions of letters for each word
    with open("dictionary_sorted.txt", "r") as dictionary:
        for line in dictionary:
            word = line.rstrip("\r\n")

            #For each char in word, pass it to swap
            for index in range(len(word)):
                char = switch(word[index])
                #If the char was changed by swap, substitute the char in the original word
                if char != word[index]:
                    test_password = word[:index] + char + word[index + 1:]

                    #Attempt password
                    test_hash = crypt.crypt(test_password, hashed_password)
                    if test_hash == hashed_password:
                        end_time = time.time()
                        entropy = math.log(94, 2)*len(test_password)
                        print("Password: " + test_password)
                        print("Entropy: {}".format(entropy))
                        print("Time: {}".format(end_time - start_time))
                        return

    #Attempt all variations of two, common character substitutions of letters for earch word
    with open("dictionary_sorted.txt", "r") as dictionary:
        for line in dictionary:
            word = line.rstrip("\r\n")

            #For each char in word, pass it to swap
            for index_one in range(len(word)):
                char_one = switch(word[index_one])
                #If the char was changed by swap, substitute the char in the original word
                if char_one != word[index_one]:
                    word_one = word[:index_one] + char_one + word[index_one + 1:]

                    #For each char in word starting at index_one, to avoid repeats, pass it to swap
                    for index_two in range(index_one, len(word)):
                        char_two = switch(word[index_two])
                        #If the char was changed by swap and not already subsituted, substitute the char in the original word with the first substitution
                        if char_two != word_one[index_two]:
                            test_password = word_one[:index_two] + char_two + word_one[index_two + 1:]

                            #Attempt password
                            test_hash = crypt.crypt(test_password, hashed_password)
                            if test_hash == hashed_password:
                                end_time = time.time()
                                entropy = math.log(94, 2)*len(test_password)
                                print("Password: " + test_password)
                                print("Entropy: {}".format(entropy))
                                print("Time: {}".format(end_time - start_time))
                                return

    #Failed to crack password, not in dictionary or has different subtitutions
    end_time = time.time()
    print("Password was not found...")
    print("Elapsed time: {}".format(end_time - start_time))


#Common character substitutions of letters. 
#If character matches any of these replace it with character to be substituted and return, otherwise don't change it.
def switch(case):
    if case.find("A") != -1:
        return case.replace("A", "@", 1)
    if case.find("a") != -1:
        return case.replace("a", "@", 1)
    if case.find("B") != -1:
        return case.replace("B", "8", 1)
    if case.find("b") != -1:
        return case.replace("b", "8", 1)
    if case.find("E") != -1:
        return case.replace("E", "3", 1)
    if case.find("e") != -1:
        return case.replace("e", "3", 1)
    if case.find("G") != -1:
        return case.replace("G", "6", 1)
    if case.find("g") != -1:
        return case.replace("g", "6", 1)
    if case.find("I") != -1:
        return case.replace("I", "!", 1)
    if case.find("i") != -1:
        return case.replace("i", "!", 1)
    if case.find("L") != -1:
        return case.replace("L", "1", 1)
    if case.find("l") != -1:
        return case.replace("l", "1", 1)
    if case.find("O") != -1:
        return case.replace("O", "0", 1)
    if case.find("o") != -1:
        return case.replace("o", "0", 1)
    if case.find("S") != -1:
        return case.replace("S", "$", 1)
    if case.find("s") != -1:
        return case.replace("s", "$", 1)
    if case.find("T") != -1:
        return case.replace("T", "7", 1)
    if case.find("t") != -1:
        return case.replace("t", "7", 1)
    return case

if __name__ == "__main__":
    task_three()
