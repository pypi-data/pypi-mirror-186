import sys
sys.dont_write_bytecode = True
import os
from sys import stdout
from time import sleep
import ctypes

def clear():
    system = os.name
    if system == "nt":
        os.system(f'cls')
    elif system == "posix":
        os.system(f'clear')
    else:
        print(f'\n'*200)

def slowWrite(_str):
    for letter in _str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.04)

def sTitle(_str):
    syst = os.name
    if syst == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{_str}')
    elif syst == "posix":
        sys.stdout.write(f'{_str}')
    else:
        # I do nothing
        pass

def writeInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.04)
    value = input()
    return value