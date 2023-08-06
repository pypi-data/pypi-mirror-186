### What is this package for?

This package is to simplify the user to use the input function with different data types. For example, we can simplify this:

```
x = int(input("please insert a number"))
```

to

```
x = inpt.i(int,"please insert a number")
```

### How to install it?

You can type this in the terminal or command prompt to install this package:

```
pip install inpt
```

### Minumum requirement
python 3.5

### Current version

0.0.5
### How to use this version

To use this version, you will first need to import it like this:

```
from inpt import inpt
```

The format for the library and parameters is like this:

```
inpt.i(data_type, text for input)
```

Let's say we want to have a string input that wants the user to input their name. We can do it like this:

```
from inpt import inpt
c = inpt.i(str,"What is your name?")
```

The output will be:


What is your name?<br>
&lt;Insert a string here and press enter&gt;

### This version has to offer:

Automatic one line space after the input text