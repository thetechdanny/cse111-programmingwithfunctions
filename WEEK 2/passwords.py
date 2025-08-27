# For creativity, I added a password suggestion that adds 5 random characters to the provided password, 
# for passwords greater than 4 characters but less than 10 characters; this is to add it up to the minimum 
# password and also increase strength to 5

# Import the random function to be used later in the program to generate a list of random characters
import random

# List out characters to be used in the program
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', '"', ",", ".", "<", ">", "?", "/", "`", "~"]

# Define function that checks for match in provided file
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
       
        for line in file:
            line_word = line.strip()
          
            if case_sensitive==False:
                if word.lower() == line_word.lower():
                    return True
            else:
                if word == line_word:
                    return True
                
        return False
    
# Define function that loops through characters in the word to check for a match with reference with the character list      
def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    
    return False
       
# Define function that returns a numeric value based on the types of characters the word contains
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    
    return complexity

# Define a function that selects randomly from the character list and add the random characters to the password
def suggest_stronger_password(base_password):
    random_chars = (
        random.sample(LOWER, 1) +
        random.sample(UPPER, 1) +
        random.sample(DIGITS, 2) +
        random.sample(SPECIAL, 1)
    )
    
    # Use the shuffle from the random module to mix the characters randomly
    random.shuffle(random_chars)  
    return base_password + ''.join(random_chars)

# Define function that checks the length requirement, calls the word complexity function to calculate complexity and returns password strength
def password_strength(password, min_length=10, strong_length=16):
    strength = 1
    dictionary_file = "wordlist.txt"
    common_password = "toppasswords.txt"

    # Check if password is a dictionary word
    if word_in_file(password, dictionary_file):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Check if password is an already used password
    elif word_in_file(password, common_password, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check password's minimum length requirement and return strength value
    if len(password) < min_length:
        print("Password is too short and is not secure.")

        # Give a password suggestion if password is greater than 4 but less than 10
        if (len(password)) > 4 and (len(password)) < 10:
            suggested_password = suggest_stronger_password(password)
            print(f"Suggested Password: {suggested_password}")
            print()
        return strength 

    # Check password's strong length requirement and return strength value
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")

        # Give a password suggestion if password is greater than 4 but less than 10 
        if (len(password)) > 4 and (len(password)) < 10:
            suggested_password = suggest_stronger_password(password)
            print(f"Suggested Password: {suggested_password}")
            print()
        strength += 4 
        return strength

    # Check password's strength based on word complexity when password is not too short or too long
    else:
        strength += word_complexity(password)
    
    if strength > 5:
        strength = 5
    
    # Print out the password strength after checking all criteria above
    print(f"Strength value is: {strength}")
    print()
    
    return strength        
   
# Define the main function that loops the user's input for password and quits when user inputs "q" or "Q"
def main():

    password = ""
    while password != "q" and password != "Q":
       password = input("Type in your password: ")
       
       if password != "q" and password != "Q":
            password_test = password_strength(password)
            print(f"Your password strength is {password_test}")
            print()

 
if __name__ == "__main__":
    main()


  