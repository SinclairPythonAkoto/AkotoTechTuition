# getting user input
name = input("What is your name? ")
print(name)

# printing data with the user input
age = input("What is your age? ")
print("Hello " + name + ", you are " + age + " years old.")

# creating mulitiple inputs from one variable
prompt = input("What is your name? "), input("What is your age? ")
print("Hello " + prompt[0] + ", you are " + age)
