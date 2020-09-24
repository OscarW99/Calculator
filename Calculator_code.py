#-*- coding: utf-8 -*-
"""
Created on Wed Jul 15 08:34:09 2020

@author: oscar
"""

""" A simple calculator app with tkinter """


from tkinter import *
import string



#function that adds a number to entry widget when clicked
def number(num):
    get = str(my_entry.get())
    post = get+str(num)
    my_entry.delete(0, END)
    my_entry.insert(0, post)



#function that performs calculation when equals button is pressed
def equals():
    list_of_signs = ['+','-','*','/']
    get = str(my_entry.get())
    split = [get.split(sign) for sign in list_of_signs if sign in get]
    if '+' in get:
        answer = int(split[0][0]) + int(split[0][1])
    elif '-' in get:
        answer = int(split[0][0]) - int(split[0][1])
    elif '*' in get:
        answer = int(split[0][0]) * int(split[0][1])
    elif '/' in get:
        answer = int(split[0][0]) / int(split[0][1])
    my_entry.delete(0, END)
    my_entry.insert(0, answer)
        
    
    

#A function to add sign to entry widget and perform calculation if sign already in entry widget
def math(sign):
    get = str(my_entry.get())
    for char in get:
        if char not in str(string.digits):
            split = get.split(char)
            if '+' in get:
                equate = int(split[0]) + int(split[1])
            elif '-' in get:
                equate = int(split[0]) - int(split[1])
            elif '*' in get:
                equate = int(split[0]) * int(split[1])
            elif '/' in get:
                equate = int(split[0]) / int(split[1])
                if equate == int(equate):
                    equate = int(equate)
            break 
        
        else:
            equate = get
    post = str(equate) + sign
    my_entry.delete(0, END)
    my_entry.insert(0, post)
 
    
    
    
#tkinter GUI loop
root = Tk()
root.title("calculator")

#entry for visualising calculation
my_entry = Entry(root, font = 'Ariel')
my_entry.grid(columnspan = 4, row=0,column=0, padx = 0, pady =5)


#Buttons for numbers 0-9                                                               
btn7 = Button(text = '7', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(7)).grid(row = 1,
                                                          column = 0, padx = 5, pady = 6)
btn8 = Button(text = '8', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(8)).grid(row = 1,
                                                          column = 1, padx = 5, pady = 6)
btn9 = Button(text = '9', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(9)).grid(row = 1,
                                                          column = 2, padx = 5, pady = 6)
btn4 = Button(text = '4', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(4)).grid(row = 2,
                                                          column = 0, padx = 5, pady = 6)
btn5 = Button(text = '5', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(5)).grid(row = 2,
                                                          column = 1, padx = 5, pady = 6)
btn6 = Button(text = '6', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(6)).grid(row = 2,
                                                          column = 2, padx = 5, pady = 6)
btn1 = Button(text = '1', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(1)).grid(row = 3,
                                                          column = 0, padx = 5, pady = 6)
btn2 = Button(text = '2', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(2)).grid(row = 3,
                                                          column = 1, padx = 5, pady = 6)
btn3 = Button(text = '3', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(3)).grid(row = 3,
                                                          column = 2, padx = 5, pady = 6)
btn0 = Button(text = '0', font = 'Ariel', width = 5, justify = LEFT, command = lambda: number(0)).grid(row = 4,
                                                          column = 0, padx = 5, pady = 6)
                                              
#add button
butn_add = Button(root, text = '+', font = 'Ariel', width = 5, justify = LEFT, command = lambda: math('+')).grid(row = 1,
                                                          column = 3, padx = 5, pady = 6)
#subtract button
butn_subtract = Button(root, text = '-', font = 'Ariel', width = 5, justify = LEFT, command = lambda: math('-')).grid(row = 2,
                                                          column = 3, padx = 5, pady = 6)
#multiplication button
butn_multiply = Button(root, text = '*', font = 'Ariel', width = 5, justify = LEFT, command = lambda: math('*')).grid(row = 3,
                                                          column = 3, padx = 5, pady = 6)
#division button
butn_divide = Button(root, text = '/', font = 'Ariel', width = 5, justify = LEFT, command = lambda: math('/')).grid(row = 4,
                                                          column = 3, padx = 5, pady = 6)
#equals button
butn_equals = Button(root, text = '=', font = 'Ariel', width = 5, justify = LEFT, command = equals).grid(row = 4,
                                                          column = 2, padx = 5, pady = 6)
#clear button
butn_clear = Button(root, text = 'AC', font = 'Ariel', width = 5, justify = LEFT, command = lambda: my_entry.delete(0, END)).grid(row = 4,
                                                          column = 1, padx = 5, pady = 6)


root.mainloop()

