def swap_strings(st):
    index = 1
    new_str = ""
    for char in st:
        if index % 2 == 0:
            new_str += char.upper()
        else:
            new_str += char.lower()

        index += 1

        return new_str


swap_strings("Anthropomorphism")
