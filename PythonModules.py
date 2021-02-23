# Use a Module
import os
import mymodule
import mymodule as mx
import platform                         


os.system("cls")
mymodule.greeting("Benjamin Uchenna")
a = mymodule.person1["name"]
print(a)
print()

b = mx.person1["age"]
print(b)
print()

c = platform.system()
print(c)
print(platform.version())
print()

# Using the dir() Function
print(dir(platform))
print()
print(dir(platform.python_version))
print()

from mymodule import my_function
print(my_function("Joy"))