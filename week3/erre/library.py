# File imported by calculator in order to split the code into modules

import os
import subprocess

def ui_bar(length=12):
    print("-"*length)

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def print_ui(operations):
    ui_bar()
    print("CALCULATOR".center(12))
    ui_bar()
    for op in operations[-3:]:
        print(op)
    ui_bar()
    print(" add - adds two numbers\n sub - subtracts two numbers\n mul - multiplies two numbers\n div - divides two numbers")
    ui_bar()

def prompt_numbers():
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            return (a, b)
        except ValueError:
            print("You need to enter numbers")
            ui_bar(3)
            continue

def prompt_calculation(operations):
    op = input("> ").strip()
    ui_bar(6)
    a, b = prompt_numbers()
    if op == "add":
        operations.append(f" {a} + {b} = {a + b}")
    elif op == "sub":
        operations.append(f" {a} - {b} = {a - b}")
    elif op == "mul":
        operations.append(f" {a} * {b} = {a * b}")
    elif op == "div":
        if b == 0: # <-- HERE
            res = "Infinity"
        else:
            try:
                res = a / b
            except ZeroDivisionError:
                print("???") # Should never be reached due to the check above ^^
        operations.append(f" {a} / {b} = {res}")
    else:
        print("invalid operation")
