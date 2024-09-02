import statistics
numbers = []
user_input = input("> ")

while user_input != "exit":
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Enter a valid number")

    user_input = input("> ")

if numbers:
    print(f"Sum: {sum(numbers)}")
    print(f"Mean: {statistics.mean(numbers)}")
    print(f"Cardinality: {len(numbers)}")
