print('21_classes_and_objects')

""" 
    Python 是一种面向对象的编程语言。
    Python 中的一切都是一个对象，有它的属性和方法。
    程序中使用的数字、字符串、列表、字典、元组、集合等是相应内置类的对象。
    我们创建类来创建一个对象。
    类就像一个对象构造函数，或者是创建对象的“蓝图”。
    我们实例化一个类来创建一个对象。
    类定义了对象的属性和行为，而另一方面，对象代表了类。

从这个挑战一开始，我们就在不知不觉中处理类和对象。Python 程序中的每个元素都是一个类的对象。让我们检查一下python中的所有东西是否都是一个类：

 """

# 类构造函数
# 在上面的例子中，我们从 Person 类创建了一个对象。
# 然而，没有构造函数的类在实际应用中并没有真正的用处。
# 让我们使用构造函数使我们的类更有用。
# 
# 与Java或JavaScript中的构造函数一样，python也有内置的init ()构造函数。的初始化构造函数有自参数这对类的当前实例的引用 实施例：


# class Person:
#       def __init__ (self, name):
#           self.name =name

# p = Person('Asabeneh')
# print(p.name)
# print(p)


# class Person:
#     def __init__ (self, name):
#         self.name = name

# p = Person('ABCD')
# print(p.name)
# print(p)

""" class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

 """

#  对象可以有方法。方法是属于对象的函数。

""" class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
 """


# 对象默认方法
# 有时，您可能希望为对象方法设置默认值。
# 如果我们在构造函数中给参数赋予默认值，就可以避免在不带参数的情况下调用或实例化我们的类时出错。让我们看看它的外观：
""" class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
 """

#  修改类默认值的方法
# 在下面的例子中，person 类，所有的构造函数参数都有默认值。
# 除此之外，我们还有技能参数，我们可以使用方法访问它。
# 让我们创建 add_skill 方法来将技能添加到技能列表中。

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills) 


# 使用继承，我们可以重用父类代码。
# 继承允许我们定义一个从另一个类继承所有方法和属性的类。
# 父类或超类或基类是提供所有方法和属性的类。
# 子类是从另一个类继承的类。让我们通过继承 person 类来创建一个学生类。
""" class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills) """

# 我们没有在子类中调用init ()构造函数。
# 如果我们没有调用它，那么我们仍然可以从父级访问所有属性。
# 但是如果我们确实调用了构造函数，我们就可以通过调用super来访问父属性。

# 我们可以向子类添加一个新方法，也可以通过在子类中创建相同的方法名称来覆盖父类。
# 当我们添加init ()函数时，子类将不再继承父类的init ()函数。
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# 我们可以使用 super() 函数或父名 Person 来自动继承其父级的方法和属性。
# 在上面的例子中，我们覆盖了 parant 方法。
# 
# child 方法有一个不同的特点，它可以识别性别是男性还是女性并指定适当的代词（他/她）。




   
