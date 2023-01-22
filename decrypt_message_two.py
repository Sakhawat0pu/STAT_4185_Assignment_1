encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

start = 1
end = len(encrypted_message) - 2

char_list = list(encrypted_message)
while (start < end):
    char_list[start], char_list[end] = char_list[end], char_list[start]
    start += 2
    end -= 2
    
print(''.join(char_list))