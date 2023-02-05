#!/usr/bin/env python3

import os
import pickle
import sys

#intialize the alpha and symbols
alpha = "abcdefghijklmnopqrstuvwxyz"
symbols = "'?!@#$%^&*():><{}-_"

#clear the screen before the programm runs
os.system("clear") if os.name == "posix" else os.system("cls")

print("""\td88888b d8b   db d888888b  d888b  .88b  d88.  .d8b.  
\t88'     888o  88   `88'   88' Y8b 88'YbdP`88 d8' `8b 
\t88ooooo 88V8o 88    88    88      88  88  88 88ooo88 
\t88~~~~~ 88 V8o88    88    88  ooo 88  88  88 88~~~88 
\t88.     88  V888   .88.   88. ~8~ 88  88  88 88   88 
\tY88888P VP   V8P Y888888P  Y888P  YP  YP  YP YP   YP\n\n\t\t\tEnigma Simulator\n""")


#load the rotors data from enigma_rotors_configuration.enigma file.
try:
    econfig = open("enigma_rotors_configuration.enigma", 'rb')
    rotor1, rotor2, rotor3 = pickle.load(econfig)

#return an error message if the enigma_rotors_configuration file doesn't exist.
except Exception as err:
    print("- error: enigma_rotors_configuration.enigma file does'n exist!")
    print("- please run enigma_rotors_configure.py first.")
    sys.exit()


#reflect every single character. example => a : z, b : y 
def reflector(c):
   reflected = alpha[(26-alpha.find(c))-1]
   return reflected


#rotate the rotors
def rotate_rotors(state):
    global rotor1, rotor2, rotor3
    rotor1 = rotor1[1:] + rotor1[0]
    if state >= 26:
        rotor2 = rotor2[1:] + rotor2[0]
    if state >= (26 * 26):
        rotor3 = rotor3[1:] + rotor3[0]


#enigma encryptor/decryptor
def enigma(plain):
    cipher = ""
    state = 0

    for ch in plain:
        #ignore the symbols
        if ch in symbols:
            cipher += ch
            continue

        #ignore the whitespaces
        if ch == " ":
            cipher += " "
            continue

        #enigma encrypt/decrypt
        c1 = rotor1[alpha.find(ch)]
        c2 = rotor2[alpha.find(c1)]
        c3 = rotor3[alpha.find(c2)]
        c3 = alpha[rotor3.find(reflector(c3))]
        c2 = alpha[rotor2.find(c3)]
        c1 = alpha[rotor1.find(c2)]
        
        cipher += c1
        
        state += 1
        rotate_rotors(state)        
    
    return cipher


def main():
    plain = input("text : ")
    cipher = enigma(plain)
    print(f"enc : {cipher}")


if __name__ == "__main__":
    main()
