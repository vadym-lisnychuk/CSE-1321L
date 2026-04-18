i = 0
sentence = input("Enter a sentence (lowercase letters only): ")
while i < range(len(sentence)):
    freq_count = 0

    for j in range(sentence):
        if sentence[i] == j:
            freq_count += 1

    curr = int(input(f"Guess the frequency of letter '{sentence[i]}': "))
    if curr > freq_count:
        print("Too high!")
    elif curr < freq_count:
        print("Too low!")
    else:
        print("Correct!")