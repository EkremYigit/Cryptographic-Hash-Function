import base64

DIGEST_LENGTH = 32
PADDING_STRING = "XLtjhSuszj6vcC5ohlYKZ8oH9vX5GSN8NG5iqk6yu9G8qoKjdUCVIVjGk8yhLWnvKq2VYTfrENq"
KEY_STRING = "Its My New Key."


def KeyProcess(final_ascii):
    return_ary = ""
    print("KEY STATE")
    for i in range(len(final_ascii)):
        char = ord(final_ascii[i]) ^ ord(KEY_STRING[(3+i*2) % len(KEY_STRING)])
        if char < 48:
            char += 65
            if 90 < char < 97:
                char += 14
        elif 57 < char < 64:
            char += 21
        elif char >= 123:
            char -= 21
        if 90 < char < 97:
            char += 14
        return_ary += chr(char)
    return return_ary


def XOR(byte_array):
    return_ary = ""
    print("XOR STATE")
    firstLen = len(byte_array)
    i = 0
    if firstLen / 2 > 32:
        while i <= firstLen / 2:
            char = ord(byte_array[i]) ^ ord(byte_array[len(byte_array) - 1 - i])
            if char < 48:
                char += 65
                if 90 < char < 97:
                    char += 14
            elif 57 < char < 64:
                char += 21
            elif char >= 123:
                char -= 21
            if 90 < char < 97:
                char += 14
            return_ary += chr(char)

            if i > 32:
                i = i + ((i * 11) % 4 + 1)
            else:
                i += 1

    if firstLen / 2 <= 32:
        while i < 32:
            char = ord(byte_array[i%len(byte_array)]) ^ ord(byte_array[len(byte_array) - 1 - (i%len(byte_array))])
            if char < 48:
                char += 65
                if 90 < char < 97:
                    char += 14
            elif 57 < char < 64:
                char += 21
            elif char >= 123:
                char -= 21
            if 90 < char < 97:
                char += 14
            return_ary += chr(char)
            i += 1

    return return_ary


while 1:
    val2 = input("Enter your value or press 1 to auto fill: ")
    key2 = input("Enter a key or press 1 to auto fill: ")

    if val2 == '1' and key2 == '1':
        with open('test.bin', 'rb') as f:  #if you want to change file that will be hashed just change this line.
            ascii_text = ""
            binary = f.read()
            for i, c in enumerate(base64.b64encode(binary)):
                ascii_text += chr(c)
                if i == 100000000:
                    break

        for i in range(len(PADDING_STRING)):
            if len(ascii_text) % 32 != 0:
                ascii_text += PADDING_STRING[i]
            if len(ascii_text) % 32 == 0:
                break
        while len(ascii_text) > DIGEST_LENGTH:
            if len(ascii_text) < 20000000:
                ascii_text = KeyProcess(ascii_text)
            ascii_text = XOR(ascii_text)
        print('Hashed Value : ->'+ascii_text)

    elif val2 != 1 and key2 != 1:
        ascii_text = val2
        KEY_STRING = key2
        for i in range(len(PADDING_STRING)):
            if len(ascii_text) % 32 != 0:
                ascii_text += PADDING_STRING[i% len(PADDING_STRING)]
            if len(ascii_text) % 32 == 0:
                break
        ascii_text = XOR(ascii_text)
        ascii_text = KeyProcess(ascii_text)

        print('Hashed Value : ->' + ascii_text + '\nKey :-> ' + KEY_STRING + "\nValue :->" + val2)
        print('---------///---------------///--------')
