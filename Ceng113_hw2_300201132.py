from timeit import default_timer as timer

# Function to check if the is prime() function, an integer number, which is given as a parameter, will be checked to notice if it is a prime number; otherwise, False must be returned.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check the accuracy test is prime() function, the is prime() function will be checked if the given case is true or not.
def accuracy_test_is_prime(test_case, expected_value):
    result = is_prime(test_case)
    if result == expected_value:
        print(f"Test for {test_case} passed")
    else:
        print(f"Test for {test_case} failed")

# Function to measure the speed test is prime() function, the duration of the is prime() function as seconds will be measured for the given number using the timer() function.
def speed_test_is_prime(number):
    start = timer()
    is_prime(number)
    end = timer()
    duration = end - start
    print(f"Time taken to check {number}: {duration:.8f} seconds")
    return duration

# Besides the functions, you must test using the accuracy test is prime() function for three prime and three composite numbers.
print("Accuracy Tests:")
accuracy_test_is_prime(2, True)      
accuracy_test_is_prime(17, True)     
accuracy_test_is_prime(97, True)     
accuracy_test_is_prime(4, False)     
accuracy_test_is_prime(18, False)   
accuracy_test_is_prime(100, False)   

# Also, you need to measure the performance using the speed test is prime() function, using 16-bit, 20-bit,24-bit, 28-bit, and 32-bit prime numbers.
print("\nSpeed Tests:")
speed_test_is_prime(65521)          
speed_test_is_prime(1048573)         
speed_test_is_prime(16777213)     
speed_test_is_prime(268435459)       
speed_test_is_prime(4294967311)      