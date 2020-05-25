def check_if_vowel(character):
    
    character = character.upper()
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    if character in vowels:
        return True

    return False

print(str(check_if_vowel(character = str(input('Enter your character : ')))))