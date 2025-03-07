#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")


    #Instance method definition
    pass

fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()
snoopy.sit()

fido.__dir__()