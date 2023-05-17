#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string and type(roman_string) != str:
        return 0    
        roman_string = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,"M": 1000, 
                   "IV": 4, "IX": 9, "XL": 90, "XC": 90, "CD": 400, "CM": 900}
    
