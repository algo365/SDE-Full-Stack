def get_string_length(str):
    count = 0
    for index in range(len(str)):
        print(str[index])
        str[index] = 'a'
        count+=1 
    
    return count

str = "mahesh"
print("String length ", get_string_length(str))