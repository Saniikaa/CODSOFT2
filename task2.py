print("SIMPLE CALCULATOR!!")
print("Choose which operation you want to perform : ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. DIVISION")
print("4. MULTIPLICATION")

def sum(num1,num2):
    return num1+num2

def diff(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2 != 0: 
        quotient = num1 / num2
        remainder = num1 % num2
        return quotient, remainder
    else:
        return "Division by zero is not allowed"
    
def calculator():
    try:
        choice = input("Enter which operation you want to perform, Enter choice 1/2/3/4 : ")
        if choice not in ["1","2","3","4"]:
            print("Enter valid choice : ")
            return
        
        num1 = float(input("Enter first Number : "))
        num2 = float(input("Enter second Number : "))

        if choice == "1":
            result = sum(num1, num2)
            print(f"The result is: {result}")

        elif choice == "2":
            result = diff(num1, num2)
            print(f"The result is: {result}")

        elif choice == "4":
            result = mul(num1, num2)
            print(f"The result is: {result}")

        elif choice == "3":
            result = div(num1, num2)
            if isinstance(result, tuple):
                quotient, remainder = result
                print(f"The quotient is: {quotient} and the remainder is: {remainder}")
            else:
                print(result)
    except ValueError:
        print("Invalid Input. Please enter correct values")
        
calculator()


