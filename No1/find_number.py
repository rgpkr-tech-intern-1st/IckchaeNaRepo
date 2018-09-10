import subprocess, sys


def binary_search(low_int, high_int):
    guess_num = (low_int + high_int) / 2

    result = subprocess.check_output(["python", "guess.zip", str(guess_num)])

    if result == greater:
        low_int = guess_num
        binary_search(low_int, high_int)

    elif result == less:
        high_int = guess_num
        binary_search(low_int, high_int)

    else:
        print(result)


greater = "The value is greater than your guess.\n"
less = "The value is less than your guess.\n"

binary_search(-sys.maxint, sys.maxint)




