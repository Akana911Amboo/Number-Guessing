def find_first_repeating_character(s):         
    character_count = {}        # Dictionary to store count of characters
    
    # Iterating through characters in the string
    for character in s:
        # Check if character already encountered
        if character in character_count:         # Print the repeating character and its memory address
            print(f"The memory adderess of the first repeating character '{character}' is: {id(character)}")
            return character, id(character)  # Return repeating character and its memory address
        else:            # Store count of character
            character_count[character] = 1
    # No repeating character found
    return None

x = input("What is  your favourite word: ")
y = find_first_repeating_character(x)
if y is None:
    print("No repeating character found.")
