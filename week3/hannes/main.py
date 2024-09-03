import calculate
from os import system, name


def clear_terminal():
    # Windows
    if name == "nt":
        _ = system("cls")
    # Mac and Linux
    else:
        _ = system("clear")


def convert_to_number(input):
    try:
        number = int(input)
    except ValueError:
        try:
            number = float(input)
        except ValueError:
            raise ValueError("Input is not a valid number")
    return number


def get_validated_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = convert_to_number(user_input)
            return number
        except ValueError as e:
            print(f"Invalid input! {e}. Please enter a valid number.")


def main():
    clear_terminal()

    terminal_line = "-" * 40
    history = []

    while True:
        print(f"{terminal_line}\nCalculator")

        if history != []:
            print(f"{terminal_line}")

            if len(history) > 3:
                history.pop(0)

            for item in history:
                print(item)

        print(
            f"{terminal_line}\n- add | Add two numbers\n- sub | Subtract two numbers\n- mul | Multiply two numbers\n- div | Divide two numbers\n\n- quit | Exit this process\n{terminal_line}"
        )

        command = input("Type one of the above commands\n> ")

        if command == "add" or command == "sub" or command == "mul" or command == "div":
            a = get_validated_number("Num 1:\n> ")
            b = get_validated_number("Num 2:\n> ")

            if command == "div" and b == 0:
                print(
                    "Cannot divide by zero. Please enter a different value for Num 2."
                )
                continue
        elif command == "quit":
            exit()
        else:
            print("Command is not recognized, press enter to try again...")
            input("> ")

        if command == "add":
            history.append(f"{a} + {b} = {calculate.add(a, b)}")
        elif command == "sub":
            history.append(f"{a} - {b} = {calculate.sub(a, b)}")
        elif command == "mul":
            history.append(f"{a} * {b} = {calculate.mul(a, b)}")
        elif command == "div":
            history.append(f"{a} / {b} = {calculate.div(a, b)}")

        clear_terminal()


if __name__ == "__main__":
    main()
