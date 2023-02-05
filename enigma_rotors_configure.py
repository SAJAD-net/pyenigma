#!/usr/bin/env python3

import pickle
import random


alpha = list("abcdefghijklmnopqrstuvwxyz")

#initialize the rotors
rotor1, rotor2, rotor3 = alpha, alpha, alpha

random.shuffle(rotor1)
rotor1 = ''.join(rotor1)

random.shuffle(rotor2)
rotor2 = ''.join(rotor2)

random.shuffle(rotor3)
rotor3 = ''.join(rotor3)

#save the rotors' configuration in enigma_rotors_configuration.enigma
econfig = open("enigma_rotors_configuration.enigma", "wb")
pickle.dump((rotor1, rotor2, rotor3), econfig)

print("- rotors successfully configured!")

