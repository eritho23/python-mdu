import json
import os


def print_todos(todos):
    for idx, todo in enumerate(todos):
        string_to_print = f"{idx} | "
        if todo[0]:
            string_to_print += "[X] "
        else:
            string_to_print += "[ ] "
        string_to_print += todo[1]
        print(string_to_print)


def load_or_create_todos():
    path_to_todo_savefile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "todos.json"
    )
    if os.path.exists(path_to_todo_savefile):
        print(f"attempting to load todos from {path_to_todo_savefile}...", end="")
        try:
            with open(path_to_todo_savefile, "r") as fp:
                loaded = json.load(fp)
                print("success")
                return loaded
        except json.decoder.JSONDecodeError:
            print("save file corrupt, decide if you keep it or not")
            exit(1)
    else:
        print("creating todos in memory, will save on exit")
        return []


def dump_todos(todos):
    path_to_todo_savefile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "todos.json"
    )
    print(f"saving todos to: {path_to_todo_savefile}...", end="")
    with open(path_to_todo_savefile, "w") as fp:
        json.dump(todos, fp)
    print("done")


def print_prompt():
    print("(A)dd, (C)heck, (D)elete or (E)xit...")


def get_number_safe(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("You need to enter a number")
            continue




def prompt_for_action(todos):
    op = input("> ").strip().lower()

    if op == "":
        op = "_" # Phony, will never be reached
    else:
        op = op[0]

    if op == "a":
        item_text = input("Enter the text for the todo: ")
        todos.append([False, item_text])
    elif op == "c":
        idx = get_number_safe("Enter the index to check: ")
        try:
            todos[idx][0] = True
        except IndexError:
            print(f"Out of range, index can be maximum {len(todos) - 1}")
    elif op == "d":
        idx = get_number_safe("Enter the index to delete: ")
        try:
            todos.pop(idx)
        except IndexError:
            print(f"Out of range, index can be maximum {len(todos) - 1}")
    elif op == "e":
        dump_todos(todos)
        exit(0)
    else:
        print("Invalid command")


def main():
    todos = load_or_create_todos()
    try:
        while True:
            print_todos(todos)
            print_prompt()
            prompt_for_action(todos)
    except KeyboardInterrupt:
        dump_todos(todos)
        exit(0)


if __name__ == "__main__":
    main()
