# Basic Variables:

# 1- string [str,char,]
# 2- numbers[int,float,hex,complex,long]
# 1- boolean [bool]

# String
name="Rasheed"
first_char='R'
print('name: {}, first letter is _{}'.format(name,first_char))


# Numbers:
number=8
decimal_number=number/5 #1.6
number2=8j
print(type(number2)) #<class 'complex'>
number3=float.hex(number+0.3)#0x1.099999999999ap+3
number4=hex(number)#0x8
number5=oct(number)#0o10
print(number5)

boolean=True # or False
print("boolean:{} or False".format(boolean))
