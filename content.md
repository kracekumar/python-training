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
>>> description = """Python is a general-purpose, high-level programming language whose design philosophy emphasizes code readability. It is an expressive language which provides language constructs intended to enable clear programs on both a small and large scale. Python supports multiple programming paradigms, including object-oriented, imperative and functional programming styles.""">>> print description
Python is a general-purpose, high-level programming language whose design philosophy emphasizes code readability. It is an expressive language which provides language constructs intended to enable clear programs on both a small and large scale. Python supports multiple programming paradigms, including object-oriented, imperative and functional programming styles.
>>> 
```

**Condition**
```
if 
```
