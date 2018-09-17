import sys
import subprocess
import find_number_const as const


def binary_search(low_int, high_int):
    guess_num = (low_int + high_int) / 2

    result = subprocess.check_output(["/usr/bin/python", "guess.zip", str(guess_num)])

    if result == const.GREATER:
        low_int = guess_num
        return binary_search(low_int, high_int)

    elif result == const.LESS:
        high_int = guess_num
        return binary_search(low_int, high_int)

    else:
        return guess_num


def binary_search_little_num(low_int, high_int, hidden_number):
    guess_num = (low_int + high_int) / 2

    if guess_num == hidden_number:
        return guess_num

    elif guess_num < hidden_number:
        low_int = guess_num
        return binary_search_little_num(low_int, high_int, hidden_number)

    elif guess_num > hidden_number:
        high_int = guess_num
        return binary_search_little_num(low_int, high_int, hidden_number)


if __name__ == '__main__':
    binary_search(-sys.maxint, sys.maxint)




