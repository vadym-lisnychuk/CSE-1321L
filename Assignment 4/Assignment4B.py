def check_length(password):
    return len(password) >= 8

def check_upper_lower(password):
    upper_case = lower_case = False

    for i in password:
        if i >= 'a' and i <= 'z':
            lower_case = True
            break

    for i in password:
        if i >= 'A' and i <= 'Z':
            upper_case = True
            break

    return upper_case and lower_case

def check_special_character(password):
    txt = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    spec_char = False
    for i in password:
        for j in txt:
            if i == j:
                spec_char = True
                break

    return spec_char

def main():
    while True:
        password = input("Enter a password: ")
        requirments = "Password does not meet the requirements:"
        passing = True

        if not check_length(password):
            requirments += " Must be at least 8 characters long."
            passing = False
        if not check_upper_lower(password):
            requirments += " Must contain both uppercase and lowercase letters."
            passing = False

        if not check_special_character(password):
            requirments += "  Must include at least one special character (!, @, #)."
            passing = False

        if passing:
            print("Password is strong!")
            break
        else:
            print(requirments)

if __name__ == "__main__":
    main()

