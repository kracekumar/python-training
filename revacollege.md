**Python?**

- Interpreted language
- Multiparadigm

**Introduction**
1. Write Hello World in text editor and also show it interpreter. 

```
hasgeek@hasgeek-MacBook:~/codes/python/hacknight$ python
Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
```
>>> print "Let's learn Python"
Let's learn Python
```

**Numbers**
```
>>> 23 + 43
66
>>> 23 - 45
-22
>>> 23 * 45
1035
>>> 23 ** 4
279841
>>> 23 / 4
5
>>> 23 / 4.0
5.75
>>> 7 % 2
1
```

**Expressions**
```
>>> 3 < 2
False
>>> 3 > 2
True
>>> 3 > 2 < 1
False
>>> (3 > 2) and (2 < 1)
False
>>> 3 > 2 > 1 > 0
True
>>> (3 > 2) and (2 > 1) and (1 > 0)
True
>>> 1 or 2
1
>>> 2 or 1
2
>>> 1 + 2 + 3 * 4 + 5
20
1 + 2 + 3 * 4 + 5
  ↓
  3   + 3 * 4 + 5
          ↓
  3   +   12  + 5
      ↓
      15      + 5
              ↓
             20
>>> "python" > "perl"
True
>>> "python" > "java"
True
```

**Variables**
```
>>> a = 23
>>> print a
23
>>> a = "Python"
>>> print a
Python
```


**Guess the output**
```
True = False
False = True
print True, False
print 2 > 3
```

**Parallel Assignment**
```
>>> language, version = "Python", 2.7
>>> print language, version
Python 2.7
>>> x = 23
>>> x = 23
>>> y = 20
>>> x, y = x, x + y
>>> print x, y
23 43
```

**Guess the output**
```
z, y = 23, z + 23
a, b = 23, 12, 20
a = 1, 2
```

**Swap Variable**
```
>>> x = 12
>>> y = 21
>>> x, y = y, x
>>> print x, y
21 12
>>>
```

**String**
```
>>> language = "Python"
>>> print language
Python
>>> language = 'Python'
>>> print language
Python
>>> language = """Python"""
>>> print language
Python
>>> description = """Python is a general-purpose, high-level programming language whose design philosophy emphasizes code readability.
... It is an expressive language which provides language constructs intended to enable clear programs on both a small and large scale.
... Python supports multiple programming paradigms, including object-oriented, imperative and functional programming styles.
... """
>>> print description
Python is a general-purpose, high-level programming language whose design philosophy emphasizes code readability.
It is an expressive language which provides language constructs intended to enable clear programs on both a small and large scale.
Python supports multiple programming paradigms, including object-oriented, imperative and functional programming styles.
>>> 
 
```

**Guess output**
```
name = "krace" + "kumar"
print name
print name[0]
name[0] = "K"
```

**Guess output**
```
print 1 + 2.5
print "kracekumar" + 23
```

**Condition**
Use text editor

1. Write a program to find greatest of two numbers.

```
>>> a = 12
>>> b = 23
>>> if a > b:
...     print "a is greater than b"
... else:
...     print "b is greater than a"
... 
b is greater than a
>>> if a > 0:
...     print "a is positive"
... elif a == 0:
...     print "a is zero"
... elif a < 0:
...     print "a is negative"
... 
a is positive
```



**Data Structure**

*List*

- List is a collection of heterogenous data types like integer, float, string.

```
>>> a = [1, 2, 3]
>>> b = ["Python", 2.73, 3]
>>> len(a)
3
>>> len(b)
3
>>> a[0]
1
>>> a[-1]
3
>>> b[2]
3
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
>>> all = [a, b]
>>> all[0]
[1, 2, 3]
>>> all[-1]
['Python', 2.73, 3]
>>> all[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> all.append("Bangalore")
>>> all
[[1, 2, 3], ['Python', 2.73, 3], 'Bangalore']
>>> del all[-1]
>>> all
[[1, 2, 3], ['Python', 2.73, 3]]
>>> all[1] = "insert"
>>> all
[[1, 2, 3], 'insert']
>>> all
[[1, 2, 3], 'insert']
>>> 'insert' in all
True
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(10, 2)
[]
>>> range(10, 0, -1)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> range(0, 12, 1)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

```

range() -> `range([start,] stop[, step]) -> list of integers`

*Slicing*
```
>>> l = [1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
>>> l[:2] #first two elements
[1, 2]
>>> l[2:] #exclude first two elements
[3, 4, 5, 6, 7]
>>> l[::2] #every second element
[1, 3, 5, 7]
>>> l[::1] #every element
[1, 2, 3, 4, 5, 6, 7]
>>> l[::3] #every third element
[1, 4, 7]
>>> l[::10] #every tenth element
[1]
>>> l[::-1]
[7, 6, 5, 4, 3, 2, 1]
```


**Guess the output**
`>>> l[1:7:2]`
`>>> [][:2]`
`>>> [1][:2]`

*Accessing list elements*

```
>>> for item in all:
...     print item
... 
[1, 2, 3]
insert
>>> for number in range(10):
...     print number
... 
0
1
2
3
4
5
6
7
8
9
```

*Find all odd numbers from 0 to 9*
```
>>> for number in range(0, 10):
...     if number % 2:
...         print number
... 
1
3
5
7
9
```

**inbuilt functions**
```
>>> help([])
>>> min([1, 2, 3])
1
>>> max([1, 2, 3])
3
>>> sum([1, 2, 3])
6
>>> pow(2, 3)
8
```

**Write program which takes a number as input and if number is divisible by 3, 5 print Fizz, Buzz, FizzBuzz respectively**
```
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        number = int(sys.argv[1])
        if number % 15 == 0:
            print "FizzBuzz"
        elif number % 3 == 0:
            print "Fizz"
        elif number % 5 == 0:
            print "Buzz"
        else:
            print number

    else:
        print "python filename.py 23 is the format"

```
**Tuples**

- Tuple is a sequence type just like list, but it is immutable.
- A tuple consists of a number of values separated by commas.

```
>>> t = (1, 2)
>>> t
(1, 2)
>>> t[0]
1
>>> t[0] = 1.1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t = 1, 2
>>> t
(1, 2)
>>> del t[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> for item in t:
...     print item
... 
1
2
```

**Sets**

- Sets are unordered collection of unique elements.

```
>>> x = set([1, 2, 1])
>>> x
set([1, 2])
>>> x.add(3)
>>> x
set([1, 2, 3])
>>> x = {1, 3, 4, 1}
>>> x
set([1, 3, 4])
>>> 1 in x
True
>>> -1 in x
False
>>> 
```

**Again Lists**
```
>>> even_numbers = []
>>> for number in range(0, 9):
...     if number % 2 == 0:
...         even_numbers.append(number)
... 
>>> even_numbers
[0, 2, 4, 6, 8]
```

`As a programmer your job is write lesser code`

**List Comprehensions**
```
>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x + 1 for x in range(10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers = []
>>> for x in range(10):
...     numbers.append(x + 1)
... 
>>> print numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> even_numbers = [x for x in range(10) if x %2 == 0]
>>> even_numbers
[0, 2, 4, 6, 8]
>>> [(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0]
[(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (4, 0), (4, 2), (4, 4)]
>>> 
```

**Dictionaries**
```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d['a']
1
>>> d.get('a')
1
>>> d['z']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'
>>> d.get('z')
>>>
>>> d['a'] = 2
>>> d
{'a': 2, 'c': 3, 'b': 2}
>>> d['z'] = 26
>>> d
{'a': 2, 'c': 3, 'b': 2, 'z': 26}
>>> d.keys()
['a', 'c', 'b', 'z']
>>> d.values()
[2, 3, 2, 26]
>>> d.items()
[('a', 2), ('c', 3), ('b', 2), ('z', 26)]
>>> type(d.items())
<type 'list'>
>>> d = {'a': 2, 'b': 2, 'c': 3, 'z': 26}
>>> for key in d:
...     print key
... 
a
c
b
z
>>> for key, value in d.items():
...     print key, value
... 
a 2
c 3
b 2
z 26
>>> 'a' in d
True
>>> d.has_key('a')
True
```

**Function**

- Just like a value can be associated with a name, a piece of logic can also be associated with a name by
defining a function.

```
>>> def square(x):
...     return x * x
... 
>>> square(2)
4
>>> square(2+1)
9
>>> square(x=5)
25
>>> def dont_return(name):
...     print "Master %s ordered not to return value" % name
... 
>>> dont_return("Python")
Master Python ordered not to return value
>>> def power(base, to_raise=2):
...     return base ** to_raise
... 
>>> power(3)
9
>>> power(3, 3)
27
>>> def power(to_raise=2, base):
...     return base ** to_raise
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument 
>>> square(3) + square(4)
25
>>> power(base=square(2))
16
>>> def sum_of_square(x, y):
...     return square(x) + square(y)
... 
>>> sum_of_square(2, 3)
13
>>> s = square
>>> s(4)
16
>>> def fxy(f, x, y):
...     return f(x) + f(y)
... 
>>> fxy(square, 3, 4)
25
```

**Methods**
- Methods are special kind of functions that work on an object.

```
>>> lang = "Python"
>>> type(lang)
<type 'str'>
>>> dir(lang)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser',
'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum',
'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> lang.upper()
'PYTHON'
>>> help(lang.upper)
>>> lang.startswith('P')
True
>>> help(lang.startswith)

>>> lang.startswith('y', 1)
True
```

**Files**
```
>>> f = open('foo.txt', 'w')
>>> help(f)

>>> f.write("First line")
>>> f.close()
>>> f = open('foo.txt', 'r')
>>> f.readline()
'First line'
>>> f.readline()
''
>>> f = open('foo.txt', 'a')
>>> f.write('Second line')
>>> f.close()
>>> f = open('foo.txt', 'r')
>>> f.readline()
'First lineSecond line'
>>> f = open('foo.txt', 'a')
>>> f.write("New line\n")
>>> f.write("One more new line")
>>> f.close()
>>> f = open('foo.txt', 'r')
>>> f.readline()
'First lineSecond lineNew line\n'
>>> f.readline()
'One more new line'
>>> f.readline()
''
>>> f.close()
>>> f = open('foo.txt')
>>> f.readlines()
['First lineSecond lineNew line\n', 'One more new line']
>>> f = open('foo.txt', 'w')
>>> f.writelines(["1\n", "2\n"])
>>> f.close()
>>> f.readlines()
>>> f = open('foo.txt')
>>> f.readlines()
['1\n', '2\n']
>>> f.close()
```

**Exception Handling**
```
>>> f = open('a.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'a.txt'
>>> try:
...     f = open('a.txt')
... except:
...     print "Exception occured"
... 
Exception occured
>>> try:
...     f = open('a.txt')
... except IOError, e:
...     print e.message
... 

>>> e
IOError(2, 'No such file or directory')
>>> dir(e)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__getslice__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', 'args', 'errno', 'filename', 'message', 'strerror']
>>> e.strerror
'No such file or directory'
>>> try:
...     print l[4]
... except IndexError, e:
...     print e
... 
list index out of range
>>> raise Exception("error message")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: error message
>>> try:
...     print "a"
...     raise Exception("doom")
... except:
...     print "b"
... else:
...     print "c"
... finally:
...     print "d"
... 
a
b
d
```

**Object Oriented Programming**
```
>>> class BankAccount:
        def __init__(self):
            self.balance = 0

        def withdraw(self, amount):
            self.balance -= amount
            return self.balance

        def deposit(self, amount):
            self.balance += amount
            return self.balance

>>> a = BankAccount()
>>> b = BankAccount()
>>> a.deposit(200)
200
>>> b.deposit(500)
500
>>> a.withdraw(20)
180
>>> b.withdraw(1000)
-500
>>> class MinimumBalanceAccount(BankAccount):
...    def __init__(self, minimum_balance):
...        BankAccount.__init__(self)
...        self.minimum_balance = minimum_balance
...
...    def withdraw(self, amount):
...        if self.balance - amount < self.minimum_balance:
...            print "Sorry, you need to maintain minimum balance"
...        else:
...            return BankAccount.withdraw(self, amount)
>>> a = MinimumBalanceAccount(500)
>>> a
<__main__.MinimumBalanceAccount instance at 0x7fa0bf329878>
>>> a.deposit(2000)
2000
>>> a.withdraw(1000)
1000
>>> a.withdraw(1000)
Sorry, you need to maintain minimum balance 
>>> class A:
...     def f(self):
...         return self.g()
...     def g(self):
...         return "A"
... 
>>> a = A()
>>> a.f()
'A'
>>> a.g()
'A'
>>> class A:
...     def __init__(self):
...         self._protected = 1
...         self.__private = 2
... 
>>> a = A()
>>> a._protected
1
>>> a.__private
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: A instance has no attribute '__private'
```

**Sample Python Program**
```
#! /usr/bin/env python
#! -*- coding: utf-8 -*-


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print "Sorry, you need to maintain minimum balance"
        else:
            return BankAccount.withdraw(self, amount)

    def __repr__(self):
        return "MinimuBalanceAccount, Balance: %d" %(self.balance)


if __name__ == "__main__":
    a = MinimumBalanceAccount(500)
    print a.deposit(5000)
    print a.withdraw(4500)
    print a.withdraw(500)
```
