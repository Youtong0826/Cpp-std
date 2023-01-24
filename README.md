# Python C++/std #
C++ standard library emulated by Python
雖然有很多人做過了 但我還是想試著做做看w

## Usage
Creat a Python file that under this folder and put in some code.

### Require
Python

### Example Code

```py
from std import * #using namespace std;

name = variable() # declare a variable "name" (NoneType)
age = variable() # declare a variable "age" (NoneType)

std.cout << str("What's your name? ")
std.cin >> name #input name
std.cout << str("What's your age? ")
std.cin >> age  #input age
response = variable(str(f"Hello, {name}! You're {age} years old!")) # declare a variable "response"
std.cout << response #print it
```
```
What's your name? Peter
What's your age? 20
Hello, Peter! You're 20 years old!
```

also you can do this. 
```
from std import * #it's like "using namespace std" in C++;

name = variable() # declare a variable "name" (NoneType)
age = variable() # declare a variable "age" (NoneType)

std.cout << str("What's your name? ")
std.cin >> name
std.cout << str("What's your age? ")
std.cin >> age
std.cout << str("Hello, ") << name << str("!") << std.endl << str("You're ")    << age << str(" years old!")
```
or this. (need to create object)
```
from std import variable
from std import str
from std import cout

var = variable(str("Hello World"))
cout() << var
```

These code are all in test.py





