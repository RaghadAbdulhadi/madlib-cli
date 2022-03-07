# Python String format() Method

The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}.
The placeholders can be identified using named indexes {price, numbered indexes {0}, or even empty placeholders {}

The format() method returns the formatted string.

    string.format(value1, value2...)

Formatting Types

[formatting types](https://www.w3schools.com/python/ref_string_format.asp)


# Passing Multiple Arguments to a Function
*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.

Unpacking operator (*): accepts positional arguments 
- The iterable object you’ll get using the unpacking operator * is not a list but a tuple
- Can be used on any iterable that Python provides.

Unpacking operator (**): accepts keyword (or named) arguments
- The iterable object is a standard dict. If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values().
- Can only be used on dictionaries.

**Function that takes a changeable number of both positional and named arguments**

The order for the parameters should be:
1. Standard arguments
2. *args arguments
3. **kwargs arguments


# Single-responsibility principle
Is a computer-programming principle that states that every module, class or function in a computer program should have responsibility over a single part of that program's functionality, and it should encapsulate that part.

It would be a bad design to couple two things that change for different reasons at different times.

# Lab Requirments:

open file:

```
f = open("././madlib_cli/assets/madlib_template.txt", "r")
print(f.name)
print(f.mode)
f.close()

with open("././madlib_cli/assets/madlib_template.txt", "r") as f:
    print(f.name)
    print(f.mode)
    print(f.read())
print(f.closed)

    f_content = f.readline()
    print(f_content)

    f_content = f.readline()
    print(f_content)

    f_content = f.readline()
    print(f_content)

    for line in f:
        print(f_content)

    f_content = f.read(80)
    print(f_content)

    f_content = f.read(20)
    print(f_content)

    with open("././madlib_cli/assets/madlib_template.txt", "r") as f:
    size_to_read = 20
    f_content = f.read(size_to_read)

    # while len(f_content) > 0:
    #     print(f_content, end=" ")
    #     f_content = f.read(size_to_read)
    # print(f.tell())

    # start at the beginning of the file, before the 2nd read
    #f.seek()

```
```
write:
with open("././madlib_cli/assets/madlib_template2.txt", "w") as f:
    f.write('hello')
    f.seek(0) #overrides 
    f.write('y')
```

with open("././madlib_cli/assets/madlib_template.txt", "r") as template1: #reading the file
    with open("././madlib_cli/assets/madlib_template2.txt", "w") as template: #writing in the file
        for line in template1:
            template.write(line)


# Strip method
The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

# Regex

findall	Returns a list containing all matches

sub	Replaces one or many matches with a string

r"\{(.*?)\}"
\{ matches the character { literally (case sensitive)
(.*?) 1st Capturing Group
.*? matches any character
*? Quantifier — Matches between zero and unlimited times, as few times as possible, expanding as needed (lazy)
\} matches the character } literally (case sensitive)