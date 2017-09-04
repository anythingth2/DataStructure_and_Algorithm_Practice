from lab3_1 import Queue

# encoded_message = input('Enter Encoded Message : ')
# i = Queue(queue=list(input('Enter i sequence : ')))

encoded_message = 'K quwm Saynpv'
i = Queue(queue=list('256183'))

next_i , decoded_message = Queue() , Queue()

for char in encoded_message:
    
    if not i.isEmpty() and char != ' ':
        decode_factor = int(i.deQueue())
        if ord(char) - decode_factor in range(ord('a'),ord('z')+1) or ord(char) - decode_factor in range(ord('A'),ord('Z')+1):
            decoded_message.enQueue( chr( ord(char) - decode_factor ) )
        elif ord(char) - decode_factor :
            decoded_message.enQueue( chr( ord(char) - decode_factor + ord('z') ) )
    else:
        if i.isEmpty():
            i = next_i
        if char == ' ':
            decoded_message.enQueue(' ')
    next_i.enQueue( decode_factor )
print(decoded_message)


