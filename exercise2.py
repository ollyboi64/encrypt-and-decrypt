def caesar_cipher(text, shift, mode='Encrypt'):
    result = ""

    #adjust shit for Decryption
    if mode =='decrypt':
        shift = -shift

    for char in text:
        #Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) +shift - 65) % 26 + 65)
        #Encrypt/Decrypt uppercase letters
        elif char.islower():
            result += chr((ord(char) +shift - 97) % 26 + 97)
        else:
            result += char # non_alphabetic characters remain unchanged

    return result

# Example usage
if __name__== "__main__":
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25) "))

    if choice == 'e':
        Encrypted_text = caesar_cipher(text, shift, mode="encrypt")
        print("Encrypted Text:", Encrypted_text)
    elif choice == 'd':
        Decrypted_text = caesar_cipher(text, shift, mode="decrypt")
        print("Decrypted text:", Decrypted_text)
    else:
        print("Invalid choice!please enter 'e'for encrypt or 'd'for decrypt")