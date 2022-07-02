# Seesion 3: Math #

We will use this [Python compiler](https://www.programiz.com/python-programming/online-compiler/) to run the Python code and to enable you to follow along with this session!

In this session we will look at how we can use math with Python.

With Python you can print different types of numbers in the terminal *(whole numbers, decimals, negative numbers)* as well as basic arithmatics (add, subtract, multiply & divide).

### Integers & Floats ###
A **String** is a whole number.
They are often used to store numbers that can't be broken up (like the number of minutes in the hour - you wouldn't stay it's 10:32.5).
*Integers* can calso be used for counting the number of tinmes something has hapened.

A **float** is a decimal number.
They are often used when preciscion is a factor - like scientific measurements, or when representing percentages (0.0 - 1.0).


# Math Operations #
Lets see how we can use the different math operations in our terminal 
```
print(10 * 2)       # 10 multiply 2
print(10 / 2)       # 10 divide 2
print(10 + 2)       # 10 add 2
print(10 - 2)       # 10 subtract 2

print(2 ** 3)       # 2 power of 3
print(10 % 3)       # 10 modulo 3
print(1 + 2 * 3)    # order of operations
print(10 / 3.0)     # ints & doubles
```

### Modulo Operator ###
The **modulo** operator is `%` operator.  Similar to division, this divides the two numbers together then only returns the remainder (whatever is left after the division).
If we write `10 % 3`, we are basically saying divide 10 by 2 and only return the remainder as the asnwer.  If there is no remainder, then it will return `0`.
So for this example, when we divide 10 by 3 we get 3 remainder 1.  *Modulo* will only return the remainder so the answer would be `1`. 
***Modulo only divides the number when the value is equal or greater than number.  If the value is lower than the number, instead of trying to divide what is left, it is returned as the remainder.***


### Order of Operations ###
In Python we can chnage the order of operatoion by using parenthesis (brackets).  So normally for `(3 * 4 + 5)` we would `3 * 4` then `+ 5` to the answer, but we can add brackets to chnage the order.
```
(3 * (4 + 5))    # 4 + 5 first, then 3 * answer
```

You can also create a varibale and store a number (even a calculation), then reference the variable name when you want to print to terminal (or use the calculation/number) elsewhere in your code.
```
my_num = 10 % 3

print(my_num)
```
We can convert the number to a string by wrapping the variable name in brackets and putting `str` in front of the brackets
```
my_num = 10 % 1

print(str(my_num))
```
This also allows you to *concatenate* the number with a string.
**REMEMBER!!** *To use an integer or float with a string you will need to convert it to a string or you will get an error.*

Here are just a few built-in math functions you may find useful when calculating math using Python.

- `abs(num)` : Will give you the *absolute number* if it's a nagative.  You want to think if it's nagative number then the highest number is the exact opposite but a positive number.
- `pow(num1, num2)` : The *power of..* takes 2x parameters - the first is your starting number, the second is the number which you want raise the first parameter to.
- `max(num1, num2, num3)` : This returns the highest or *maximum* number.
- `min(num1, num2, num3)` : This returns the lowest or *minimum* number.
- `round(num)` : Rounds a **float** to the *nearest integer*.

With the math module you can have access to a wider range of math functions, all you have to do is import the module in your Python code.
```
from math import floor, ceil, sqrt

num1 = 3.9
num2 = 4.1
num3 = 16

floor(num1)    # this will round DOWN the number
ceil(num2)     # this willl round UP the number
sqrt(num3)     # find the square root of a number
```
There are many more functions from the math module, a link will be provided at the bottom of this page.

### Python Assignment Operators ###
Another thing we can use in Python are called *Python Operators*. There ae many, for this example I will cover some of the *Assignment Operators* - they are used when assigning values to variables.
```
num1 = 5
num2 = 3

num1 += num2
print(num1)
```
This is the same as:
```
num1 = 5

num1 += 3
print(num1)
```
In the two examples above, what we are basically doing is saying add `3` to the value of `num1` (which is already 5).  This will make the value `8` (like saying `num1 = num1 + 3`).
A list of Python operators are at the bottom of the page.  We will cover some more in depth later on in the course.

#### Refrences ###
You can find more information on math with Pyhon here:
- [w3 Shools](https://www.w3schools.com/python/python_math.asp)
- [Math module functions](https://www.w3schools.com/python/module_math.asp)
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
