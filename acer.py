#Trial 1
#num = 45
#print(num)

#Using input 
print("Welcome user")
name = input("Please identify yourself: ")
print("Welcome", name)

#Doing basic calculations with two numbers
num1 = int(input("Can I have your first number?: "))
num2 = int(input("Can I have your second number?: "))

print("Press A for addition")
print("Press S for subtraction")
print("Press M for multiplication")
print("Press D for division")
print("Press R for modulus")
print("Plese put on your Cap Lock")

operate = (input("Choose your operation: "))



#addition
sum = num1 + num2
print("Addition equals", sum)

#subtraction
diff = num1 - num2
print("Subtraction equals", diff)


#multiplication
product = num1 * num2
print("Multiplication equals", product)

#division
divide = num1 / num2
print("Division equals", divide)

#modulus
mod = num1 // num2
print("Mod equals", mod)

