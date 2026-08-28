from typing import List

def read_integers() -> List[int]:
    list_int = []
    inputted = input()

    for i in inputted.split(","):
        list_int.append(int(i))

    return list_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
