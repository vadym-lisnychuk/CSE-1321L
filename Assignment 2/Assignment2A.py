print("Let's tune your guitar!")

untuned = 6 
current_string_number = ""
current_string_freq = 0.0

while untuned > 0:
    match untuned:
        case 1:
            current_string_number = "first"
            current_string_freq = 329.63
        case 2:
            current_string_number = "second"
            current_string_freq = 246.94
        case 3:
            current_string_number = "third"
            current_string_freq = 196.00
        case 4:
            current_string_number = "fourth"
            current_string_freq = 146.83
        case 5:
            current_string_number = "fifth"
            current_string_freq = 110.00
        case 6:
            current_string_number = "sixth"
            current_string_freq = 82.41
    
    input_freq = float(input(f"What is the frequency of the {current_string_number} string?: "))
    if(input_freq == current_string_freq):
        print("Perfect! You are in tune, let's move on to the next string...")
        untuned = untuned - 1
    elif(input_freq < current_string_freq):
        print("Too Low! Tighten the string.")
    elif(input_freq > current_string_freq):
        print("Too High! Loosen the string.")
    print()

print("Your guitar is tuned and ready to use!")