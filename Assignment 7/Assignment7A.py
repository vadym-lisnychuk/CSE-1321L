def is_valid_passcode(number):
    return number >= 1000 and number <= 9999

def count_correct_position(secret, guess):
    if not (is_valid_passcode(secret) and is_valid_passcode(guess)):
        return
    
    secret = str(secret)
    guess = str(guess)
    ix = 0

    for i in range(4):
        if secret[i] == guess[i]:
            ix += 1
    return ix

def count_wrong_position(secret, guess):
    if not (is_valid_passcode(secret) and is_valid_passcode(guess)):
        return
    
    secret = str(secret)
    guess = str(guess)
    ix = 0
    for i in range(4):
        for j in range(4):
            if secret[i] == guess[j] and i != j:
                ix += 1

    return ix

def main():
    total_guesses = 0
    secret = int(input("Enter secret passcode: "))
    while True:
        guess = int(input("Enter your guess: "))
        print(f"Correct position: {count_correct_position(secret, guess)}")
        print(f"Wrong position: {count_wrong_position(secret, guess)}")
        print()
        
        total_guesses += 1
        if secret == guess:
            break

    print("--- Game Over ---")
    print(f"Total guesses: {total_guesses}")

    if total_guesses <= 3:
        performance = "Excellent"
    elif total_guesses <= 6:
        performance = "Good"
    else:
        performance = "Needs Practice"

    print(f"Performance: {performance}")


if __name__ == "__main__":
    main()