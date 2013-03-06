**Python?**

- Interpreted language
- Multiparadigm

**Introduction**
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

**Condition**
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

**First Python Program**
```
#! /usr/bin/env python
#! -*- coding: utf-8 -*-
# Write a program to get integer from user and find it is positive or negative or zero.

number = int(raw_input("Enter a number:"))
if number > 0:
    print "number %d is positive" % (number)
elif number == 0:
    print "number %d is zero" % (number)
elif number < 0:
    print "number %d is negative" % (number)
hasgeek@hasgeek-MacBook:~/codes/python/python-training/examples$ ./first.py 
Enter a number:23
number 23 is positive
hasgeek@hasgeek-MacBook:~/codes/python/python-training/examples$ python first.py 
Enter a number:23
number 23 is positive
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
 *nbuilt functions**
