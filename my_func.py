#Turn the string red
import random


def red(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;31m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string green
def green(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;32m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string blue
def blue(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;34m{value}{value2}{value3}{value4}{value5}\033[0m"
#Choose your random rate from 1 to 99
def random_func(rate: float) -> float:
    try:
        1 >= rate <= 100
    except ValueError:
        print(red("Please enter a number between 0 and 100"))
    else:
        if random.random() < rate / 100:
            return True
        else:
            return False
