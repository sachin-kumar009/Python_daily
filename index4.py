# squares = [x*x for x in range(5)]
# print(squares)

# numbers = [1,2,3,4,5]

# square = [i*i for i in numbers]
# print (square)


# even = [x for x in range(1,11) if x%2 == 0]
# print(even)

# odd = [ x for x in range(1,11) if x%2 != 0]
# print(odd)


# names = ["rahul","aman","rohit"]

# upper_names = [names.upper() for names in names]

# print(upper_names)

# words = ["apple","banana","mango"]

# lengths = [len(word) for word in words]
# print(lengths)

# result = ["Even" if i%2 ==0 else "Odd" for i in range(1,6)]

# print(result)

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)


#functions


def greet(name,age):
  return f"Hello,{name} and {age}"

message = greet("Rahul",23)
print(message)


def add(a,b):
  return a+b

sum = add(2,3)
print(sum)


#Traditional Function
square = lambda x:x*x
print(square(5))

multiply = lambda a,b:a*b
print(multiply(5,4))


students =[
  ("Aman",80),("Rahul",95),("Priya",88)
]

students.sort(key = lambda x:x[1])
print(students)