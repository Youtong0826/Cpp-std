from std import * #using namespace std;

name = variable() # declare a variable "name" (NoneType)
age = variable() # declare a variable "age" (NoneType)

std.cout << str("What's your name? ")
std.cin >> name
std.cout << str("What's your age? ")
std.cin >> age

response = variable(str(f"Hello, {name}! You're {age} years old!"))
std.cout << response

name = variable() # declare a variable "name" (NoneType)
age = variable() # declare a variable "age" (NoneType)

std.cout << str("What's your name? ")
std.cin >> name
std.cout << str("What's your age? ")
std.cin >> age

std.cout << str("Hello, ") << name << str("!") << std.endl << str("You're ")  << age << str(" years old!")

from std import variable
from std import str
from std import cout

var = variable(str("Hello World"))
cout() << var
from std import * #it's like "using namespace std" in C++;