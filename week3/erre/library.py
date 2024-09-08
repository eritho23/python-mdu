# File imported by calculator in order to split the code into modules

import os
import subprocess

from decimal import Decimal, InvalidOperation


def ui_bar(length=12):
    print("-" * length)


def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def print_ui(operations, print_instructions=True):
    ui_bar()
    print("CALCULATOR".center(12))
    ui_bar()
    for op in operations[-3:]:  # Could be replaced by popping the zeroth index
        print(op)
    ui_bar()
    if print_instructions:
        print(
            " add - adds two numbers\n sub - subtracts two numbers\n mul - multiplies two numbers\n div - divides two numbers"
        )
        ui_bar()


def prompt_numbers():
    while True:
        try:
            a = Decimal(input("a = "))
            b = Decimal(input("b = "))
            return (a, b)
        except InvalidOperation:
            print("You need to enter numbers")
            ui_bar(3)
            continue


def prompt_calculation(operations):
    op = input("> ").strip()
    if op in ["add", "sub", "mul", "div"]:
        ui_bar(6)
        a, b = prompt_numbers()
        if op == "add":
            operations.append(f" {a} + {b} = {a + b}")
        elif op == "sub":
            operations.append(f" {a} - {b} = {a - b}")
        elif op == "mul":
            operations.append(f" {a} * {b} = {a * b}")
        elif op == "div":
            if b == 0:  # <-- HERE
                res = "Infinity"
            else:
                try:
                    res = a / b
                except ZeroDivisionError:
                    print("???")  # Should never be reached due to the check above ^^
            operations.append(f" {a} / {b} = {res}")
    else:
        input("invalid operation, press enter to proceed")
