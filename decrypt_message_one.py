cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below
keys = [key for key in cipher]
values = [value for value in cipher.values()]

reverse_cipher = dict(zip(values, keys))

decrypted_message = ''

for i in range(len(encrypted_message)):
    decrypted_message += reverse_cipher[encrypted_message[i]]
    
print(decrypted_message)

