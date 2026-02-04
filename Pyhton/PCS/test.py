# Write a function to return largest even number from an integer array
# also declare an array with odd and even numbers and invoke this function
# collect the result from function and print it on the screen
# you can hard code values of the numbers in code

def largest_even_number(numbers):

    largest_even = 0
    for number in numbers:
        #check if number is even
        #Store even number in an variable
        #Compare next even with largest even to check if it is largest if yes update the new 
        #Else no action
        #The loop will do this for all the elments at the end largest even will have the required answer
        if(number % 2 == 0):
            if(number>largest_even):
                largest_even = number
            

    #send back the largest even to the caller of the function
    return largest_even

def largest_odd_number(numbers):

    largest_odd = 0
    for number in numbers:
        #check if number is even
        #Store even number in an variable
        #Compare next even with largest even to check if it is largest if yes update the new 
        #Else no action
        #The loop will do this for all the elments at the end largest even will have the required answer
        if(number % 2 != 0):
            if(number>largest_odd):
                largest_odd = number
            

    #send back the largest even to the caller of the function
    return largest_odd

def get_count_odd_number(numbers):

    odd_count = 0
    for number in numbers:
        #check if number is even
        #Store even number in an variable
        #Compare next even with largest even to check if it is largest if yes update the new 
        #Else no action
        #The loop will do this for all the elments at the end largest even will have the required answer
        if(number % 2 != 0):
            #odd_count = odd_count+1
            odd_count+=1

                        
        
            

    #send back the largest even to the caller of the function
    return odd_count












def invoke_largesteven():
    numbers = [40,17,180,452,160,24,9]
    result = largest_even_number(numbers)
    print(f"Largest even number is:", result)

    result = largest_odd_number(numbers)
    print(f"Largest odd number is:", result)

    result = get_count_odd_number(numbers)
    print(f"Count of odd numbers is:", result)

invoke_largesteven()


