def print_list(a_list):
    for i in a_list:
        print(i, end = '')
    print('\n')

def encrypt(word, key):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypt_list = []

    for i in word:
        if i != ' ':
            for j, k in enumerate(letters):
                if i == k:
                    new_p = (j + key) % 26
                    encrypt_list.append(letters[new_p])
        else:
            encrypt_list.append(' ')
    
    print_list(encrypt_list)

def decrypt(word, key):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decrypt_list = []

    for i in word:
        if i != ' ':
            for j, k in enumerate(letters):
                if i == k:
                    new_p = (j - key) % 26
                    decrypt_list.append(letters[new_p])
        else:
            decrypt_list.append(' ')

    print_list(decrypt_list)


task = input("enter 'e' to encrypt or 'd' to decrypt and press enter:\n")
if task == 'e' or task == 'd':
    word = input("Enter word: ").lower()
    key = int(input("Number key : "))
else:
    print("invalid input!!!")

if task == 'e':
    encrypt(word, key)
elif task == 'd':
    decrypt(word, key)
else:
    print("try again")
