# question - your  code only have to allow letters, numbers, whitespaces and count the special chracter as error, count the number of special characters


def check_error(input_string):
    
    error_count = 0
    
    for char in input_string:
        
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char == ' ':
        
            continue
        
        else: 
            error_count += 1
            
    
    return error_count

user_input = input(' type something: ')

print('no of errors in the input = ', check_error(user_input))       