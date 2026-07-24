# List of names without spaces
list_with_stripped_words = []

# Reads each line of the file as list item
with open(r"C:\Users\Alisha\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    list_of_names = names.readlines()

# Reads the content of the file
with open(r"C:\Users\Alisha\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter:
    content = letter.read()

# Removes the newline characters from each name
for name in list_of_names:
    new_name = name.strip()
    list_with_stripped_words.append(new_name)

# Creates a personalized letter for each name
for name in list_with_stripped_words:
    with open(
        rf"C:\Users\Alisha\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\letter_to_{name}.txt",
        "w",
    ) as new_letter:
        replaced_letter = content.replace("[name]", name)
        new_letter.write(replaced_letter)