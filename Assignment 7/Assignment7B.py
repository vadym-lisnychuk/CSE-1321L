def has_upper(password):
    for c in password:
        if c.isupper():
            return True
    return False

def has_lower(password):
    for c in password:
        if c.islower():
            return True
    return False

def has_digit(password):
    for c in password:
        if c.isdigit():
            return True
    return False

def classify_password(password):
    if len(password) >= 8 and has_upper(password) and has_lower(password) and has_digit(password):
        return "Strong" 
    elif len(password) >= 6 and (has_upper(password) or has_lower(password)) and has_digit(password):
        return "Moderate"
    else:
        return "Weak"

def main():
    
    current_password = ""
    total_passwords = 0
    strong_passwords = 0
    moderate_passwords = 0
    weak_passwords = 0


    longest_password = ""
    shortest_password = ""

    while True:
        current_password = input("Enter password: ")

        #validating input
        if current_password == "STOP":
            break
        
        #giving user a feedback
        password_classification = classify_password(current_password)

        #increase counters accordingly
        total_passwords += 1
        match password_classification:
            case "Strong":
                strong_passwords += 1
            case "Moderate":
                moderate_passwords += 1
            case "Weak":
                weak_passwords += 1

        print(f"Password Strength: {password_classification}\n")

        # records:

        if longest_password == "":
            longest_password = current_password
        if shortest_password == "":
            shortest_password = current_password
        
        if len(current_password) > len(longest_password):
            longest_password = current_password
        if len(current_password) < len(shortest_password):
            shortest_password = current_password

    print("--- Password Report ---")
    print(f"Total passwords: {total_passwords}")
    print(f"Strong: {strong_passwords}")
    print(f"Moderate: {moderate_passwords}")
    print(f"Weak: {weak_passwords}")
    print(f"Longest password: {longest_password}")
    print(f"Shortest password: {shortest_password}")



if __name__ == "__main__":
    main()