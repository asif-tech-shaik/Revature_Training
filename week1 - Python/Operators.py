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
>>> str.split()
...     
['asif']
>>> str1='hello asif how are you'
...     
>>> str1.split()
...     
['hello', 'asif', 'how', 'are', 'you']
>>> str1.split('o')
...     
['hell', ' asif h', 'w are y', 'u']
>>> str1.join(str)
...     
'ahello asif how are youshello asif how are youihello asif how are youf'
>>> str2='      mohammad    '
...     
>>> str2.strip()
...     
'mohammad'
