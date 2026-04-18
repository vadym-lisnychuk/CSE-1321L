sentence = input("Enter a sentence: ")
rearranged_sentence = ""

print(sentence.split())
short = []
mid = []
long = []

for i in sentence.split(" "):
    if len(i) <= 3:
        short.append(i)
    elif len(i) <= 6:
        mid.append(i)
    else:
        long.append(i)

for i in short:
    rearranged_sentence += i
    rearranged_sentence += " "

for i in mid:
    rearranged_sentence += i
    rearranged_sentence += " "

for i in long:
    rearranged_sentence += i
    rearranged_sentence += " "

rearranged_sentence = rearranged_sentence[:-1]
print(f"Rearranged sentence: {rearranged_sentence}")