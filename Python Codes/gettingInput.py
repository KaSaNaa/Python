from unittest import result


name = input("Enter your name: ") #takes an input from user and stores it in the assigned variable
age = input("Enter your age: ")  
print("Hello " + name + "!. you are "  + age+ " years old.")

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
#result= int(num1)+int(num2)  you can't input deciaml values when the variable is declared as a integer.
result = float(num1)+ float(num2)

print(result)