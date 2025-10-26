Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5>6 and 3<7
False
5>6 or 3<7
True
not 0
True
not 6
False
not -5
False
7&9
1
7|9
15
7^9
14
5<<3
40
5>>2
1
5<<4
80
5>>4
0
5>>5
0
5>>>3
SyntaxError: invalid syntax
5<<<4
SyntaxError: invalid syntax
num1=10
type
<class 'type'>
type(num1)
<class 'int'>
num1 is int
False
type(num1) is int
True
num1 is int
False
print(num1)
10
num1
10
print('hello')
hello
'hello'
'hello'
print('hi'+'hello')
hihello
print(num1+10)
20
print(num1+'10')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(num1+'10')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('hi'+10)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('hi'+10)
TypeError: can only concatenate str (not "int") to str
print('sum: '+num1+10)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('sum: '+num1+10)
TypeError: can only concatenate str (not "int") to str
print('sum: ',num1+10)
sum:  20
sum:  20
print('sum: '+'\n',num1+10)
sum: 
 20
print('sum: ','\n',num1+10)
sum:  
 20
input
<built-in function input>
input()
'hi'
"'hi'"
input()
hi
'hi'
input("Enter the num")
Enter the num
''
input("Enter the num")
5
SyntaxError: multiple statements found while compiling a single statement
input("Enter the num")
Enter the num5
'5'
input("Enter the num")
5
SyntaxError: multiple statements found while compiling a single statement
input("Enter the num: ")
Enter the num: 5
'5'
input(True)
True
''
bool(input('Enter the num'))
Enter the num0
True
bool(input('Enter the num'))
Enter the num
False
bool(input('Enter the num'))

Enter the num'hi'
True
int(input('Enter the num: ')
    5
    
SyntaxError: '(' was never closed
int(input('Enter the num: '))
    
Enter the num: 5
5
int(input('Enter the num: '))
    
Enter the num: 9
9
int(input('Enter the num: '))
    
Enter the num: -9
-9
int(input('Enter the num: '))
    
Enter the num: 
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(input('Enter the num: '))
ValueError: invalid literal for int() with base 10: ''
int(input('Enter the num: '))
    
Enter the num: 5
5
float(input('Enter the num: '))
    
Enter the num: 5
5.0
int(input('Enter the num: '))

Enter the num: 5.0
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(input('Enter the num: '))
ValueError: invalid literal for int() with base 10: '5.0'
Status  T  T  T  F
data    5  0 -9  

int     5  0 -9  Error
bool    T  T  T  F


Enter the num: 5
5
int(input('Enter the num: '))  
Enter the num: 9
9
int(input('Enter the num: '))  
Enter the num: -9
-9

nt(input('Enter the num: '))   
Enter the num: 
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(input('Enter the num: '))
ValueError: invalid literal for int() with base 10: ''
int(input('Enter the num: '))  

SyntaxError: invalid syntax
int(input('Enter the num: '))  

Enter the num: 
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(input('Enter the num: '))
ValueError: invalid literal for int() with base 10: ''
a = 5      # int
b = 3j     # complex
c = a + b  # int promoted to complex
print(c)   # (5+3j)
print(type(c))  # <class 'complex'>

SyntaxError: multiple statements found while compiling a single statement
a = 5
    
b = 3j
    
c = a + b
    
print(c)
    
(5+3j)
print(type(c))
    
<class 'complex'>
'hi'
    
'hi'
"hi"
    
'hi'
"hello asif"
    
'hello asif'
'asif's house'
    
SyntaxError: unterminated string literal (detected at line 1)
"asif's house"
    
"asif's house"
'asif"s house'
    
'asif"s house'
Str1='hello asif '
    
str1
    
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    str1
NameError: name 'str1' is not defined. Did you mean: 'Str1'?
str='asif'
    
str
    
'asif'
len(str)
    
4
str[1]
    
's'
str[4]
    
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    str[4]
IndexError: string index out of range
str[3]
    
'f'
str[-2]
    
'i'
str[-5]
    
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    str[-5]
IndexError: string index out of range
str[-4]
    
'a'
str[0:2]
    
'as'
str[1:3]
    
'si'
str[0:3:1]
    
'asi'
str[0:3:2]
    
'ai'
str[0::2]
    
'ai'
str[0::3]
    
'af'
str[-3:-1]
    
'si'
str[-1:-3]
    
''
str[-3:-1:0]
    
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    str[-3:-1:0]
ValueError: slice step cannot be zero
str[-3:-1:1]

'si'
str.capitalize()
    
'Asif'
str.upper()
    
'ASIF'
str.lower()
    
'asif'
str.count('a')
    
1
str.endswith('f')
    
True
str.endswith('s')
    
False
str.find('s')
    
1
str.find('m')
    
-1
str.index('s')
    
1
str.index('m')
    
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    str.index('m')
ValueError: substring not found
str.encode('utf-8')
    
b'asif'
str.encode('utf-16')
    
b'\xff\xfea\x00s\x00i\x00f\x00'
str.replace('i','a')
    
'asaf'
str.split()
    
['asif']
str1='hello asif how are you'
    
str1.split()
    
['hello', 'asif', 'how', 'are', 'you']
str1.split('o')
    
['hell', ' asif h', 'w are y', 'u']
str1.join(str)
    
'ahello asif how are youshello asif how are youihello asif how are youf'
str2='      mohammad    '
    
str2.strip()
    
'mohammad'
id(str2)
    
2441736947888
numbers=[10,20,30]
    
numbers
    
[10, 20, 30]
numbers.append(40)
    
numbers
    
[10, 20, 30, 40]
numbers[3]
    
40
numbers[2]=300
    
numbers
    
[10, 20, 300, 40]
numbers.count(20)
    
1
numbers.index(20)
    
1
numbers.index(300)
    
2
numbers.insert(4,500)
    
numbers.remove(300)
    
numbers.pop()
    
500
numbers.pop(-2)
    
20
numbers
    
[10, 40]
numbers.reverse()
    
numbers
    
[40, 10]
numbers.sort()
    
numbers
    
[10, 40]
num5=numbers.copy()
    
num5
    
[10, 40]
id(numbers)
    
2441736952768
id(num5)
    
2441736599104
numbers.extend(num1)
    
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    numbers.extend(num1)
TypeError: 'int' object is not iterable
numbers.extend(num5)
    
numbers
    
[10, 40, 10, 40]
numbers.clear()
    
numbers
    
[]
del(numbers)
    
numbers
    
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    numbers
NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?
tupl=(10,20,30)
    
tup1
    
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    tup1
NameError: name 'tup1' is not defined. Did you mean: 'tupl'?
tupl
    
(10, 20, 30)
tupl.count(10)
    
1
tupl.index(30)
    
2
tupl.clear()
    
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    tupl.clear()
AttributeError: 'tuple' object has no attribute 'clear'
del(tupl)
    
tupl
    
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    tupl
NameError: name 'tupl' is not defined. Did you mean: 'tuple'?
set1={10,20,30,40,50}
    
set1
    
{50, 20, 40, 10, 30}
set1.add(100)
    
set1
    
{50, 20, 100, 40, 10, 30}
set2={90,80,70,60,50}
    
set1.union(Set2)
    
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    set1.union(Set2)
NameError: name 'Set2' is not defined. Did you mean: 'set2'?
set1.union(set2)
    
{100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
set1.intersection(set2)
    
{50}
set1.diiference(set2)
    
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    set1.diiference(set2)
AttributeError: 'set' object has no attribute 'diiference'. Did you mean: 'difference'?
set3=set1.diiference(set2)
    
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    set3=set1.diiference(set2)
AttributeError: 'set' object has no attribute 'diiference'. Did you mean: 'difference'?
set1.difference(set2)
    
{100, 40, 10, 20, 30}
set1.discard(20)
    
set1
    
{50, 100, 40, 10, 30}
dict1={1:10,2:20}
    
dict1
    
{1: 10, 2: 20}
dict1[2]
    
20
dict1[2]=300
    
dict1
    
{1: 10, 2: 300}
dict2={'rno':'123','name':'Asif'}
    
dict2
    
{'rno': '123', 'name': 'Asif'}
dict2['rno']
    
'123'
dict2['rno']=123
    
dict2['rno']

123
dict2['ph']=12232456789
    
dicts
    
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    dicts
NameError: name 'dicts' is not defined. Did you mean: 'dict1'?
dicts
    
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    dicts
NameError: name 'dicts' is not defined. Did you mean: 'dict1'?
dict2
    
{'rno': 123, 'name': 'Asif', 'ph': 12232456789}
ph=dict2.get('ph')
    
ph
...     
12232456789
>>> dict2.keys()
...     
dict_keys(['rno', 'name', 'ph'])
>>> dict2.values()
...     
dict_values([123, 'Asif', 12232456789])
>>> dict2.pop()
...     
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    dict2.pop()
TypeError: pop expected at least 1 argument, got 0
>>> dict1.pop(2)
...     
300
>>> dict1
...     
{1: 10}
