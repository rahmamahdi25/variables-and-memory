

def challenge_01():
# Challenge 1: outer_value is local to the function, becuase its declared inside the function only
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # Challenge 2: the function is locating the global variable on line 25? How is the print statement on line 11 accessing the global variable on line 25?
    print(f"The value from outside is: {outer_value}")

def challenge_03():
    # Challenge: it will throw an error becuase the inner value inside the function but the print value is first, and the inner value is second. 
    #We haven't declared the variable, so it doesnt know what to print
    inner_value = 42

    print(f"The value from outside is: {inner_value}")


def challenge_04():
    # 4
    outer_value = 42

    print(f"The value from outside is: {outer_value}")


outer_value = 1729