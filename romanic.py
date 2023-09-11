# create a program to convert numbers to roman numerals

# create a dictionary of roman numerals
ROMAN_NUMERALS = {
    1: "I", 
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD", 
    500: "D",
    900: "CM",
    1000: "M"
}

def convert_to_roman(number):
    roman_numerals = ""
    while number > 0:
        for key in sorted(ROMAN_NUMERALS.keys(), reverse=True):
            if number >= key:
                roman_numerals += ROMAN_NUMERALS[key]
                number -= key
                break
    return roman_numerals
  
print(convert_to_roman(2023))


# Now create a program to convert roman numerals to numbers
def roman_to_int(roman):
    number = 0
    while len(roman) > 0:
        for key in sorted(ROMAN_NUMERALS.keys(), reverse=True):
            if roman.startswith(ROMAN_NUMERALS[key]):
                number += key
                roman = roman[len(ROMAN_NUMERALS[key]):]
                break
    return number
  
print(roman_to_int("XLIX"))