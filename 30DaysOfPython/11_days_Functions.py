print('days - 11 - functions')
print('')

""" 
定义函数
函数是设计用于执行特定任务的可重用代码块或编程语句。为了定义一个函数，Python 提供了def关键字。以下是定义函数的语法。代码的功能块只有在我们调用它时才会执行。

"""

""" def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
 """
""" def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

 """

""" def greetings (name) :
    message = name + '. welcome to Python for Everyone!'
    return message

print(greetings('Wang'))

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050
 """


""" # 两个参数：一个函数可能有也可能没有一个或多个参数。一个函数可能有两个或多个参数。如果我们的函数接受参数，我们应该使用参数调用它。让我们检查一个带有两个参数的函数：
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2019, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
 """


""" def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname='Asabeneh', lastname='Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2=3, num1=2) # Order does not matter

def  add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)
    return total

add_two_numbers(num1=12, num2=32)
"""

""" def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
 """

""" def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
 """

""" def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
 """

""" def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2019):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1819))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
 """

""" 
任意数量的参数
如果我们不知道传递给函数的参数数量，我们可以通过在参数名称前添加 * 来创建一个可以接受任意数量参数的函数。

"""

""" 
def sum_all_nums (* nums):
    total = 0
    for num in nums :
        total += num
    return total

print(sum_all_nums(1,23,4,1,2,3,8))
 """

""" def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')


def generate_groups (team, * args) :
    print(team)
    for i in  args:
        print(i)
    
generate_groups('Team-1', 'A', 'B', 'C')

 """
#You can pass functions around as parameters
# 函数作为另一个函数的参数
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)

print(do_something(square_number, 3))
    

