# Getting User Input #

Creating a user input allows us as developers to get data from people who are using our programs.
We can store data from the user into a variable then do whatever we choose with the varibale for 
our programs.

To create a user input all we need to do is type `input()`.  Indside the brackets we can write
our prompt for the user - absically tell the user what we want from them.
*Note that you want to leave a space so when the user types otherwise it will be too close to your 
prompt.*
```
# input 1
input("what is your name?")

# input 2
input("what is your name? ")
```
Now in **input 2** when the user enters their name, there will be a space between the user's answer and
the questionmark.

We can also store input into a variable.
```
name = input("What is your name? ")
print(name)
```
Notice that when we print the **variable**, we get the user's input data.  This makes it really easy to manage
the data we can get from users.

We can also use what the user has written along with a string or another piece of data.
***This is know as concatenation***.
```
name = input("What is your name? ")

print("Hello " + name + "!") 
```

We can create multiple input statements in separate variables and then print them in one string like before.
```
name = input("What is your name? ")
age = input("What is your age? ")

print("Hello " + name + "! You are " + age)
```

We can also create multiple statements in **ONE** variable.  What Python will do is do through each input
statement and store them in a data type called a **tuple** *(we will cover more on this later)*.
To access the data we need to reference the index, the first input statement starting from 0 *(similar to the 
way we done string indexes)*.
```
prompt = input("What is your name? "), input("What is your age? )

print("Hello " + prompt[0] + "! You are " prompt[1])
```
This will give you the same as before.
Pretty useful if you are creating many input statements all round one thing.. like if you want to get the user's
name, DOB, etc.