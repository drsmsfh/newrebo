def crpter():
    pswrd = input("Enter your password: ")
    crepted = input("what do you want to encrypt: ")
    us_keyboard_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', ' '
]
    char_value_dict = {}
    input_length = len(pswrd)
    for i, char in enumerate(us_keyboard_characters):
        char_value_dict[char] = pswrd[i % input_length]
    m = list(crepted)
    cript = "".join(char_value_dict[i] for i in m)
    print(cript)

def decrypter():
    pswrd = input("Enter your password: ")
    crepted = input("what do you want to decrypt: ")
    us_keyboard_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', ' '
]
    char_value_dict = {}
    input_length = len(pswrd)
    for i, char in enumerate(us_keyboard_characters):
        char_value_dict[char] = pswrd[i % input_length]
    m = list(crepted)
    zb = []
    for i in m:
        if i in char_value_dict.values():
            for key, value in char_value_dict.items():
                if value == i:
                    zb.append(key)
    
    print("".join(zb))
    
crpter()
decrypter()
                    
    