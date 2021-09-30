def decipher(ciphertext, key):

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    ciphertext = ciphertext.upper()
    newText = ''

    for x in range(len(ciphertext)):
        character = ciphertext[x]
        index = alphabet.index(character)
        index -= key
        if (index > 25):
            index %= 25
            index -= 1
        newText += alphabet[index]

    print(f'key = {key}: {newText}')


if __name__ == '__main__':
    print('\nLet\'s decipher some text that\'s been encrypted using the Caesar cipher!')
    text = input("Enter the text you wish to decipher: ")
    print('\n')

    for x in range(1, 26):
        decipher(text, x)
