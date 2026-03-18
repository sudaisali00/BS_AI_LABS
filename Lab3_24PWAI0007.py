def welcome_message():
 print("welcome to python")
welcome_message

#task 2
def add_numbers(a, b):
    return  a+b
result = add_numbers(5, 6)
print("the sum is :", result)
  
  # task 3 
def functionA():
   print("inside Function A")
   functionB()

def functionB():
   print("inside Funtion B")

functionA()

#task 4
def greet(name="student"):
   print("hello", name)

greet()
greet("sudais ali shah")

#task 5 : VARIABLE SLOPE
x= 5
def show_x():
 print("Global x:", x)
 y= 10
 print("Local y", y)


   #task 6
def total_number(*numbers):
   return sum(numbers)


   #task7: VARIABLE LENGTH ARGUMENTS (* ARGS)
def student_info(**data):
   print("student info:")
   for key, value in data.items():
      print(f"{key}: {value}")
      student_info(name="sudais ali shah", age= 20, grade="F")

#Task 8
square= lambda x: x ** 2
print("square of 8:", square(8))

#Task 9
numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x**2,numbers))
print("squares:",squares)

#Task  10
marks = [45, 67, 58, 92, 83, 74]
above_50 = list(filter(lambda x: x > 50, marks))
print("marks above 50:", above_50)