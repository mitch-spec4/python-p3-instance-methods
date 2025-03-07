#!/usr/bin/env python3

class Dog:
    # Class body goes here
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")


    #Instance method definition
    pass

luna = Dog()
luna.bark()
luna.sit()

rex = Dog()
rex.bark()
rex.sit()

luna.__dir__()