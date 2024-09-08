# Custom import
from library import *


def main():
    operations = [
        "",
        "",
        "",
    ]  # contains history of ops, 3 in the beginning to print empty
    while True:
        try:
            clear_screen()
            print_ui(operations)
            prompt_calculation(operations)
        except KeyboardInterrupt:
            clear_screen()
            print_ui(operations, False)  # Do NOT print instructions when exiting
            print("exited from SIGINT")
            exit(0)


if __name__ == "__main__":
    main()
