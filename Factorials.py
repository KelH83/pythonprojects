#lookup table
factorials_lookup = {}

#Multiplication function
def multiply(n1, n2):
    return n1 * n2

#Factorial function
def factorial():
    number = int(input("What number do you want the factorial of?\n"))
    if number in factorials_lookup:
        print(f"\nThat number has already been calculated the factorial of {number} is {factorials_lookup[number]}\n")
           
        print(f"\nThese are the factorials already in the lookup table {sorted(factorials_lookup.items())}\n")#This sorts the lookup table into numerical order to make it easier for the user to see each item
        check_another()
    else:
#Initial calculation
        num2 = number -1
        answer = multiply(number, num2)

#Loops through each number lower than the input number multiplying it by the previous answer until the next number to multiply is 0
        counter = number-1
        factorial_numbers = [counter] #This is for displaying the numbers in the calculations to the user
        while counter != 1:
            num1 = answer
            num2 -=1
            answer = multiply(num1, num2)
            counter -=1
            factorial_numbers.append(counter)    
    
    #Reverse the order
        factorial_numbers.reverse()
    #Join the array with * in between
        factorial_numbers = ' * '.join([str(x) for x in factorial_numbers])
    #Adds the factorial to the lookup table
        factorials_lookup[int(number)] = answer
    
        print(f"\nFactorial of {number} is {number}! = {number} * {factorial_numbers}\n {number}! = {answer}")
        check_another()

#checks if user wants to find the factorial of another number
def check_another():
    another_factorial = input("\nWould you like to look up another number? 'y' or 'n'?\n")
    if another_factorial == "y":
        factorial()
    else: 
        print(f"Okay, just to re-cap the factorials you have requested and their answers are:{sorted(factorials_lookup.items())}")#This sorts the lookup table into numerical order

factorial()



