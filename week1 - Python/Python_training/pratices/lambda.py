
mul=lambda a:a*2
print(mul(5))

add=lambda a,b:a+b
print(add(3,4))

max_value=lambda a,b:a if a>b else b
print(max_value(3,4))
min_value=lambda a,b:a if a<b else b
print(min_value(3,4))
full_name=lambda first,last:first+" "+last
print(full_name("John","Smith"))

is_even =lambda x:x%2==0
print(is_even(4))
age_check=lambda age: True if age>=18 else False
print(age_check(13))