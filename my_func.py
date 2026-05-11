#Turn the string red
def red(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;31m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string green
def green(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;32m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string blue
def blue(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;34m{value}{value2}{value3}{value4}{value5}\033[0m"