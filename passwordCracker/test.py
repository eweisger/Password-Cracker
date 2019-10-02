

def test():
    string = "ABCDabcd"
    print(string)
    new_string = string.replace("a", "@", 1)
    print(new_string)
    for char in range(len(string)):
        if string[char] == "d":
            new_string = string[:char] + "8" + string[char+1:]     
    print(string)
    print(new_string)



if __name__ == "__main__":
    test()
