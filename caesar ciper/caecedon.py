import caesar_logo

print(caesar_logo.logo)

letters = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(word, key):
    encrypted_text = ""
    for char in word:
        if char in letters:
            pos = letters.index(char)
            new_pos = (pos + key) % 26
            encrypted_text += letters[new_pos]
        else:
            encrypted_text += char
    print(f"here is your encrypted word: {encrypted_text}")


def decrypt(word, key):
    decrypted_text = ""
    for char in word:
        if char in letters:
            pos = letters.index(char)
            new_pos = (pos - key) % 26
            decrypted_text += letters[new_pos]
        else:
            decrypted_text += char
    print(f"your decrypted word is: {decrypted_text}")


play = True
while play:
    mode = input("type 'encrypt' for encryption or 'decrypt' for decryption:\n").lower()
    message = input("type your message:\n").lower()
    key = int(input("enter the key:\n"))

    if mode == "encrypt":
        encrypt(message, key)
    elif mode == "decrypt":
        decrypt(message, key)
    else:
        print("invalid choice, please type 'encrypt' or 'decrypt'")

    again = input("type 'yes' if you want to go again, otherwise type 'no':\n").lower()
    if again != "yes":
        play = False
        print("good bye")
