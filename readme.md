# Overview
****Python has five standard Data Types:

- Numbers
- String
- List
- Tuple
- Dictionary

Python sets the variable type based on the value that is assigned to it. Unlike more riggers languages, Python will change the variable type if the variable value is set to another value.

## Numbers:

list
: int  ------->  `a=10`
: long   -------> ` b=345L`
: float -------> `c=45.32`
: complex  -------> `d=3.12J`

## Strings:

list
: str ---->`  firstName="Rasheed" `
: str ---->` message = """This is a string ` `that will span across multiple lines. Using ` `newline characters`
`and no spaces for the next lines. The end of lines within this string also count as a newline when printed""" `

## List

`A = [ ] # This is a blank list variable`
`B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.`
`C = [2, 4, 'john'] `

All lists in Python are zero-based indexed. When referencing a member or the length of a list the number of list elements is always the number shown plus one.

## Tuple

`myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')`
Here are some advantages of tuples over lists:

Elements to a tuple. Tuples have no append or extend method.
Elements cannot be removed from a tuple.
You can find elements in a tuple, since this doesn’t change the tuple.
You can also use the in operator to check if an element exists in the tuple.
Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.
It makes your code safer if you “write-protect” data that does not need to be changed.
It seems tuples are very restrictive, so why are they useful? There are many datastructures in Rhino that require a fixed set of values. For instance a Rhino point is a list of 3 numbers [34.5, 45.7, 0]. If this is set as tuple, then you can be assured the original 3 number structure stays as a point (34.5, 45.7, 0). There are other datastructures such as lines, vectors, domains and other data in Rhino that also require a certain set of values that do not change. Tuples are great for this.

# Dictionary
Dictionaries in Python are lists of Key:Value pairs. This is a very powerful datatype to hold a lot of related information that can be associated through keys. The main operation of a dictionary is to extract a value based on the key name. Unlike lists, where index numbers are used, dictionaries allow the use of a key to access its members. Dictionaries can also be used to sort, iterate and compare data.

Dictionaries are created by using braces ( { } ) with pairs separated by a comma ( , ) and the key values associated with a colon( : ). In Dictionaries the Key must be unique. Here is a quick example on how dictionaries might be used:
`room_num = {'john': 425, 'tom': 212}
`
`print (room_num.keys()) # print out a list of keys in the dictionary`