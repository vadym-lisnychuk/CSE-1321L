def format_word (word):
    return word.capitalize()

def convert_to_pascal_case(text):
    text += " "
    word = ""
    pascal = ""
    for i in text:
        if i == " ":
            word = format_word(word)
            pascal += word
            word = ""
        else:
            word += i

    return pascal


sample_text = input("Enter a string: ")
sample_text = convert_to_pascal_case(sample_text)
print(f"Pascal Case: {sample_text}")