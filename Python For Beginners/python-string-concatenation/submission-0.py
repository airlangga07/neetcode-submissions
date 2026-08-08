def concatenate(s1: str, s2: str) -> str:
    concatenated_string = s1 + s2
    if len(concatenated_string) > 10:
        return "Too long!"
    
    return concatenated_string



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
