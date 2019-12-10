# aoc_2019_5.py
import sys
import aoc_2019_intcode as ic



with open("input5.txt","r") as f:
    code = ic.Intcode()
    code.set_code_from_string(f.readline())
    code.run()
    