#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def main():

    name_list = []
    with open("Input/Names/invited_names.txt") as names:
        name_list = names.readlines()

    with open("Input/Letters/starting_letter.txt") as file:
        template = file.read()

    for name in name_list:
        letter = template.replace("[name]", name.strip("\n"))
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as output:
            output.write(letter)


if __name__ == "__main__":
    main()
