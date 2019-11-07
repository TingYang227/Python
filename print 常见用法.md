### Fancier Output Formatting

1. ```f```-strings with Python {expression}

   ```python
   # Example 保留小数点
   import math
   print(f'The value of pi is approximately {math.pi:.3f}.')
   
   # 列对齐
   # Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
   table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
   for name, phone in table.items():
       print(f'{name:10} ==> {phone:10d}')
   ```

2. ```str.format()```

   ```python
   # Basic usage
   print('We are the {} who say "{}"!'.format('people', 'Hi'))
   -----------------------------------------------------------
   
   # {} 中加数字可以调整输出顺序
   print('{0} and {1}'.format('spam', 'eggs'))
   print('{1} and {0}'.format('spam', 'eggs'))
   -----------------------------------------------------------
   
   # If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.
   print('This {food} is {adjective}.',format(
         food='spam', adjective='absolutely horrible'))
   -----------------------------------------------------------
   
   # Positional and keyword arguments can be arbitrarily combined:
   print('The story of {0}, {1}, and {other}.'.format('Bill', 'Tom', other='Mary'))
   -----------------------------------------------------------
   
   # Reference the variables to be formatted by name instead of by position
   table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
   ...       'Dcab: {0[Dcab]:d}'.format(table))
   
   # Passing the table as keyword arguments with the '**' notation.
   table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
   ```

   

3. string slicing and concatenation

4. Not fancy, but for debugging purpose

   ```
   str() -- human readable
   repr() -- read by interpreter
   ```



###  Reading and Writing Files





### print 常见用法

##### 我赞同的用法

1. Just pass the values as parameters:

   ```python
   print("Total score for", name, "is", score)
   ```

   If you don't want spaces to be inserted automatically by ```print``` in the above example, change the ```sep``` parameter:

   ```python
   print("Total score for ", name, " is ", score, sep='')
   ```

2. To use formatted string literals,  ```f```-strings

   ```python
   print(f'Total score for {name} is {score}')
   ```



### Python 保留小数位方法

```python
  >>> 234042163/(2**24)
  13.949999988079071

  >>> a=13.946
  >>> print(a)
  13.946
  >>> print("%.2f" % a)
  13.95
  >>> round(a,2)
  13.949999999999999
  >>> print("%.2f" % round(a,2))
  13.95
  >>> print("{0:.2f}".format(a))
  13.95
  >>> print("{0:.2f}".format(round(a,2)))
  13.95
  >>> print(f'{a:.15f}')
    
  # 这是一个很危险的组合，丢失了精度
  >>> print("{0:.15f}".format(round(a,2)))
  13.949999999999999

  
```





