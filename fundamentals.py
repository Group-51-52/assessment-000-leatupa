
#Question 1
def get_date_of_birth(id_number:str): 
    """
    STEP 2: Extract the date of birth from the ID number and result = it as a string

    result = format: DD/MM/YY: 
    """
    # year = id_number [0:2]
    # month = id_number[2:4]
    # day = id_number [4:6]
    date_of_birth = id_number [0:2]
    date_of_birth =  id_number [2:4]
    date_of_birth= id_number[4:6] 
    # date_of_birth = day + '/' + month + '/' + year
    
    return date_of_birth


#Question 2    
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and result =
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    gender_digit = int(id_number[6:10])
    
    if gender_digit < 5000:
        print ('Female')
    else:
        print ('Male')
    
    # if int(id_number[6]) > 4:
    #     result = 'Male'
    # else:
    #     result ='Female'

    
#Question 3
def get_citizenship(id_number):
    """
    STEP 4: Extract the citizenship from the ID number using the formula below and 
    result = it as a string

    Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
    a South African citizen and if it is greater than 01, the person is a non-South 
    African citizen.
    """
    if int(id_number[10]) == 0:
        result = 'South African'
    else:
        'Non-South African'


#Question 4

    """
    Fizzbuzz is a programme that prints the numbers from 1 to n, 
    but for multiples of 3, it prints "Fizz" instead of the number, 
    and for multiples of 5, it prints "Buzz" instead of the number. 
    For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
    """
def fizzbuzz(n):
    result = ""
    if n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
        result = "Buzz"
    elif n % 3 == 0 and n % 5 == 0: 
        result = "Fizzbuzz"
    else:
        result = str(n)

    return result
result = fizzbuzz(20)
print (result)
    

            

#Question 5
def check_number(n:int):
    if n % 2 != 0:
        return "odd"
    elif n % 2 == 0:
        if n <= 2 and n <= 5:
            return "not weird"
        elif n <= 6 and n <=20:
            return "weird"
        elif n <= 20:
            return "not weird"
        
    return "Neutral"

    """    
    TODO: Using TDD(Test Driven Development), Implement tests for the below functionality. 
    Create a test file called `test_my_tests.py` in the root directory.
    Create a test class called 'MyTestCases' and it should have the following test implementations:
        test_check_number_odd_number: Tests for positive odd numbers.
        test_check_number_even_range_2_to_5: Tests for even numbers in the range 2 to 5, ensuring it result =s "Not Weird".
        test_check_number_even_range_6_to_20: Tests for even numbers in the range 6 to 20, ensuring it result =s "Weird".
        test_check_number_even_greater_than_20: Tests for even numbers greater than 20, ensuring it result =s "Not Weird".
        test_check_number_negative_even_number: Tests for non-positive even numbers.
        test_check_number_negative_odd_number: Tests for non-positive odd numbers.
        test_check_number_neutral`: Tests for numbers that are neutral.

        
    TODO: Given an integer n, perform the following conditions actions:
    non-positive and non-negative digit(s) are 'Neutral'
    If n is odd, result = 'Weird'
    If n is even and in the inclusive range of 2  to 5 , result = 'Not Weird'
    If n is even and in the inclusive range of 6  to 20 , result = 'Weird'
    If n is even and greater than 20 , result = 'Not Weird'
    If n is non-positive and even then result = 'Very weird'
    If n is non-positive and odd then result = 'Extremely Weird'
    """

