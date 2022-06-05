# Session 1: Variables #

We will use this [Python compiler](https://www.programiz.com/python-programming/online-compiler/) to run the Python code and to enable you to follow along with this session!

In this session we will talk about what **variables** are and why they are so useful in Python.
Variables are basically like a container where you can store things; it makes it a lot easier to manage and work with the different data inside of our programs.

*So how do we create a variable?* All we do is give a variable a name, then *assign* it some data.  This data can be anything we choose!
```
my_name = "Sinclair"
```

We can print data back to us by using the `print()` function; with this we can print back words, numbers, data types and also variables.
```
print(my_name)
```

OK so we can print variables back to us, but let's take a look at a situation where variables would come in handy.
We have 4x lines from a paragraph that we want to print out:
```
print("There was a man named George.")
print("He was 70 years old.")
print("He really liked the name George.")
print("But he didn't like being 70.")
```
If I wanted to chnage the name `George` to `Sinclair` and the age from `70` to `35`, I would have to rewrite each line of the print statement and chnage the name and age to what I wanted.  There is only 4x lines of code but imagine if there were 100s of lines of code and that the name and age were referenced many times?  This would be a long task to do, and we could easily make mistakes in the process.
This is where variables become handy.  Instead of manually changing the data within the program, we could store the data in a variable to use in one part of the program, then change the value of the variable to something else in another part of the program.
We will store my name in a variable called `my_name`, then store the age in a variable called `my_age`.  With these varaibles we can then use them instead of writing out the name & age each time.
```
my_name = "Sinclair"
my_age = "35"

print("There was a man named " + my_name + ".")
print("He was " + my_age + " years old.")
print("He really liked the name " + my_name + ".")
print("But he didn't like being " + my_age + ".")
```
Now when we run this we will see that the names and ages of the paragraph has been changed.
Saving the data in variables also allow us to change the values as we please.  We can change the name and age half-way through the paragraph by chnaging the values of the variables.
```
my_name = "Sinclair"
my_age = "35"

print("There was a man named " + my_name + ".")
print("He was " + my_age + " years old.")

my_name = "John"
my_age = "50"

print("He really liked the name " my_name + ".")
print("But he didn'y like being " + my_age + ".")
```

### Naming Variables ###
When giving variables a name it is very important that you give your variable a clear name that not only you will understand but also other developers.  A good name will be easy to understand what the variable is doing; **it's better to have a long variable name that is descriptive than a name that is short and confusing**.

There are some rules that developers use when naming a variable.
- Names are case sensitive and can begin with: *any letter, $ or _*
- After the first charater of the variable you can include the following: *any letter, any number, $, _*
- Variables with more than 2x words should be separated by an underscore (`_`) 
**Your Python code will work if you do not follow these naming conventions but following these rules make it easier for you and other developers will understand your code much eaiser.**

### Data Types ###
There are different data types that we can use in Python to store as variables.  We have already used 2x data types in this session but there are more. 
- Text data type: *string*
- Numeric data type: *integer, float*
- Boolean data type: *True, False*
- Mapping data types: *Dictionaries*
- Sequence data types: *list, tuple, range*
** Here is just a sample of some of the different data types in Python, we will go through some of these more in depth as the course goes on.**


#### References ####
You can find more information on variables here:
- [W3 Schools](https://www.w3schools.com/python/python_variables.asp)
- [Geek for Geeks](https://www.geeksforgeeks.org/python-variables/)
