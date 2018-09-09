import subprocess, sys

lowInt = -sys.maxint
highInt = sys.maxint

greater = "The value is greater than your guess.\n"
less = "The value is less than your guess.\n"


def binary_search(guess_num):
    global lowInt
    global highInt

    result = subprocess.check_output(["python", "guess.zip", str(guess_num)])

    if result == greater:
        lowInt = guess_num
        mid = (lowInt + highInt) / 2
        binary_search(mid)

    elif result == less:
        highInt = guess_num
        mid = (highInt + lowInt) / 2
        binary_search(mid)

    else:
        print(result)


binary_search(0)




