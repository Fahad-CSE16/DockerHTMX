print("hello world")

# lambda Function

# a = lambda a,b : a*a + 2*a*b + b*b # basic Syntax = labda perameters : experession

# calling lambda with perameters
a = (lambda a,b : a*a + 2*a*b + b*b)(2,3)

print(a)

# map functions
# b= map(functionname, list_variable) # basic syntax

b= map( lambda a: a*a  , [3,4] ) # It will return map object.. To get values make it as list
print(list(b))

## COmprehensive List
num=[3,4,5]
comprehensive= [ x*x for x in num]

print(comprehensive)


# For Filtering in comprehensive list 



filtered= [x for x in range(1,11) if x%2==0]

print(filtered)

# swap variable value

a, b= 5, 10
a,b = b, a

print(a,b)