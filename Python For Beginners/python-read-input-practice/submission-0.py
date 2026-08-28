def add_two_numbers() -> int:
    total = 0
    inputted_int = input()
    for i in inputted_int.split(","):
        total += int(i)

    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
