symbols = {
    "M":1000, 
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40, 
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
}

def checkInput(userInput):
    if (type(userInput) !=int):
        raise ValueError("*Value must be a numeric integer value\n")

    if (userInput < 0):
        raise ValueError("No negatives in ancient Rome, enter a positive number\n")


def toRoman(number):
    checkInput(number)
    roman = ""
    for symbol in symbols:
        while number > 0 and symbols[symbol]<=number:
            if number >= symbols[symbol]:                
                roman+=symbol
                number-=symbols[symbol]
    return roman
