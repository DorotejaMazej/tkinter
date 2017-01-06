#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox
import random

window = Tkinter.Tk() #ustvarili smo objekt poimenovan window

#text
besedilo = Tkinter.Label(window, text = "Select a number between 1 and 100")
besedilo.pack()

number = random.randint(1,100)

#vnosno polje
guess = Tkinter.Entry(window)
guess.pack()


#preveritev števil
def check_guess():
    for x in range(1, number):
        if x % 3 == 0 and x % 5 == 0:
            result_text = "fizzbuzz"
        if x % 3 == 0:
            result_text = "fizz"
        elif x % 5 == 0:
            result_text = "buzz"
        else:
            result_text = int(x)


        tkMessageBox.showinfo("Result", result_text)

#potrditveni gumb
submit = Tkinter.Button(window, text = "Submit", command = check_guess) #kreirali smo objekt tipa button poimenovan submit, ki preveri vnos check_guess
submit.pack() #metoda pack() gumb pripne na okno programa

window.mainloop() #zanka, ki omogoča, da je okno programa nenehno odprto
