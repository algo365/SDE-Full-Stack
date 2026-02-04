def get_largetst_even_number(numbers):

    # Read one number at a time
    # Check if the number is even, divice by 2 and get reminder and check if reminder is 0 
    # if it is zero then remember it 
    # go through next numbers till you finish all numbers
    # update largest number if you find any number greater than prev largest even number
    # at the end return the largest even number you rememebered 

    larget_even_number = 0 

    print("reading one number at a time ")
    for number in numbers:
        print(f"number is {number}")

        # check if number is odd or even 
        if (number % 2 == 0 and number > larget_even_number):            
            larget_even_number = number

    return larget_even_number

numbers = [19,18,2,11,7,6,5]
largest_even = get_largetst_even_number(numbers)
print(f"largest even number is {largest_even}")