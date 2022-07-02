# Session 2: Strings #

We will use this [Python compiler](https://www.programiz.com/python-programming/online-compiler/) to run the Python code and to enable you t follow along with this session!

In this session we will delve into what *strings* are.  *A string is basically plain text in your code!*

Any text that you want to have inside of your code must be used as a string.  We can print out strings by using the `print()` function and placing double qoutes (`""`) or single qoutes (`''`) inside - inside the qoutation markes is where we will write our text in order to be printed back to us.
```
print("Hello world!")
```

We can print we new lines within a single print statement.
```
print("Hello world!\nHello Sinclair")
```
We create a new line by using `\n`.  The backslash `\` is called the *escape character*.  We use this to tell Python that whatever comes afterwards to print it within the string *(except for* `\n` *creates a new line)*.

We can create a string variable and and then print it out by putting the name of the variable inside the brackets of the print function.  *This time you don't need to add qoutation marks*.
```
hello = "hello world"

print(hello)
```

### String Concatenation ###
**String concatenation** is when we add two strings together - when we add one string onto another.  We can concatenate multiple strings as well as string variables together.
```
print("Hello " + "Sinclair" + ", have a nice day")

name = "Sinclair"
print("Hello " + name + ", have a nice day")
```
The two print statements will print the same thing.  We can also have *multiple* string concatenations.

### String Functions ###
A function is basically a piece of code that we can run and it will perform an operation or task for us.
Just like the `print()` function, everytime we use the function it prints back whatever we pass through it.
Strings also have functions which we can to get or modify our data.
```
name = "Sinclair"

print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower()
```
`.upper()` will convert the variable into all uppercase - any lowercase letters will be converted into a uppercase.
`.lower()` will convert the variable into all lowercases - any uppercase letters will be converted into a lowercase.
`.isupper()` will check if the string variable is in all uppercase letters - returns `True` or `False`.
`.islower()` will check if the string variable is in all lowercase letters and returns `True` or `False`.

We use `len()` to find out how many characters a string variable has.
*This also works on different data types like lists, dictionaries, tuples etc.*
```
name = "Sinclair"

print(len(name))    # This will return how many characters are in the variable
```
Notice we can also find how many characters are in a string without putting it into a variable; we can simply wrap the `len()` function around the string - then either print the function or place it in a varabile.
```
print(len("Sinclair"))
```

We can use a **string index** to grab individual characters of a string.  The index is basically giving each letter a number *(starting from zero)*, then we select the number of the character you want.  For example the string `"hello"` has 4x letters but remembering that the index starts from zero, it will start from `0` and end at `3`.
```
hi = "Hello"

print(hi[0])
print("Hello"[0])
```
This will print the first character of the variable.  Notice that the two print statements will return the same output.  
Indexes are **NOT** just for strings, they can be used on lists, tuples, dictionaries etc.


We can also use the *index function* `.index()` which will tell you the index *(the number)* of any string you pass through it.  We can also pass words as the parameter for the index function and it will tell you the index if there is a match.
```
hi = "Hello world"

print(hi.index("H"))
print(hi.index("Hello"))
```
As you can see we will get the same index number for the two print statements.  This is because `H` and `Hello` both start with the letter `H` so the index would be `0`.
If there are duplicates of the same letter/string within the index, then what is returned is teh first matching index and the rest are ignored.
*One thing to take note is that if there are multiple matches then it will only return the index of the first match*

We can also use the *replace function*.  This takes two parameters, the first one is the piece of the string we want to replace (this can be the letter, a pert of 
the word or the whole word). The second parameter is what we want to replace it with.
```
my_var  = "Akoto Tech"
my_var.replace("Tech", "Tuition")

print(my_var)    # Akoto Tuition
```

#### References ####
You can find more information on strings here:
- [w3 School](https://www.w3schools.com/python/python_strings.asp)
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-strings/)
