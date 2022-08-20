with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        name = name.strip()
        with open("./Input/Letters/starting_letter.txt") as letter:
            content = letter.read()
            with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as final_letter:
                final_content = content.replace("[name]", name)
                final_letter.write(final_content)


