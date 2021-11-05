play_again = "y"

"""
This function converts words into Pig Latin. 
"""
def pig(word):
    VOWELS = "AEIOU"
    i = len(word)
    if word[0] in VOWELS:
    # For example, "IS" becomes "ISAY".
        return word + "ay"
    elif word[1] in VOWELS:
    # Consonant is followed by vowel.
        return word[1:i] + word[0] + "ay"
    else:
        return word[1:i] + word[0:1] + "ay"

while play_again == "y":
    # User input is taken.
    phrase = input("Welcome to Pig Latin, Type a word or a sentence. ")
    # After user inputs, "Your phrase is (user's input translated into Pig Latin)" will appear.
    print("Your phrase is: ", phrase)
    # Split method splits string using spaces between words.
    words = phrase.split(" ")
    # Initialise output list.
    output = []
    # Recognises each word or item in words.
    for word in words:
        word = pig(word)
        # Translates each word to Pig Latin
        output.append(word)
        # Relays each translated word in the array/list element back to user.
    print(" ".join(output))
    # Above function should print the inputted sentence back in Pig Latin including spaces.
    play_again = input("Have another go? (y/n) ")

print("I hope you had fun!")

input('Press ENTER to exit')