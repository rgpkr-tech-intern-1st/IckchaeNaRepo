import sys
import subprocess
import find_number_const as const


def binary_search(low_int, high_int):
    guess_num = (low_int + high_int) / 2

    result = subprocess.check_output(["python", "guess.zip", str(guess_num)])

    if result == const.GREATER:
        low_int = guess_num
        return binary_search(low_int, high_int)

    elif result == const.LESS:
        high_int = guess_num
        return binary_search(low_int, high_int)

    else:
        return guess_num


if __name__ == '__main__':
    binary_search(-sys.maxint, sys.maxint)




