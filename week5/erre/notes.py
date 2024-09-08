import json
import os
import subprocess

def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def print_notes(notes):
    print("-"*12)
    print("Notes:")
    print("-"*12)
    for note in notes.keys():
        print(note)
    print("-"*12)


def load_or_create_notes():
    path_to_notes_savefile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "notes.json"
    )
    if os.path.exists(path_to_notes_savefile):
        print(f"attempting to load notes from {path_to_notes_savefile}...", end="")
        try:
            with open(path_to_notes_savefile, "r") as fp:
                loaded = json.load(fp)
                print("success")
                return loaded
        except json.decoder.JSONDecodeError:
            print("save file corrupt, decide if you keep it or not")
            exit(1)
    else:
        print("creating notes in memory, will save on exit")
        return {}


def dump_notes(notes):
    path_to_notes_savefile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "notes.json"
    )
    print(f"saving notes to: {path_to_notes_savefile}...", end="")
    with open(path_to_notes_savefile, "w") as fp:
        json.dump(notes, fp)
    print("done")


def print_prompt():
    print("(V)iew, (A)dd, (R)emove or (E)xit...")


def prompt_for_action(notes):
    op = input("> ").strip().lower()
    if op == "":
        op = "_"
    else:
        op = op[0]

    if op == "a":
        item_text = input("Enter the title: ")
        body_text = input("Enter the note: ")
        notes[item_text] = body_text
    elif op == "v":
        title = input("Enter note title to view: ")
        if not title in notes:
            input("No note with specified name found...press ENTER to proceed")
        else:
            print(notes[title])
            input("Press ENTER to return to main UI")
    elif op == "r":
        title = input("Enter the title to delete: ")
        if not title in notes:
            input("No note with specified name found...press ENTER to proceed")
        else:
            notes.pop(title, None)
    elif op == "e":
        dump_notes(notes)
        exit(0)
    else:
        input("Invalid command, press ENTER to proceed")


def main():
    notes = load_or_create_notes()
    try:
        while True:
            clear_screen()
            print_notes(notes)
            print_prompt()
            prompt_for_action(notes)
    except KeyboardInterrupt:
        dump_notes(notes)
        exit(0)


if __name__ == "__main__":
    main()
