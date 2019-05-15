# ##############################################################继承##################################
#
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#     def __sleep(self):
#         print('这是私有财产。')
#
#     def jump(self):
#         print('you jump i  jump')
#
# class Dog(Animal):
#     def eat(self):
#         print('天啦噜')
#
#     pass
# class Cat(Animal):
#     pass
# dog = Dog()
# dog.run()
# dog.eat()
# # dog.__sleep()###注意此处无法调用父类的私有方法
# dog.jump()
# #
#
##########################################################################################多态问题
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#     def __sleep(self):
#         print('这是私有财产。')
#
#     def jump(self):
#         print('you jump i  jump')
#
# class Dog(Animal):
#     def eat(self):
#         print('天啦噜')
#
#     def run(self):
#         print('dog is running....')
#
# class Cat(Animal):
#     pass
# dog = Dog()
# dog.run()#多态为在此处虽然继承了父类的object类但在此处依然会调用属于自己的run方法，称之为多态

# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型
#
# print(f'a是否为list类型：{isinstance(a, list)}')
# print(f'b是否为Animal类型：{isinstance(b, Animal)}')
# print(f'c是否为Dog类型：{isinstance(c, Dog)}')
#
# print(f'c是否为Dog类型：{isinstance(c, Dog)}')
# print(f'c是否为Animal类型：{isinstance(c, Animal)}')
#
# b = Animal()
# print(f'b是否为Dog类型：{isinstance(b, Dog)}')
# def run_two_times(animal):
#     animal.run()
#     animal.run()
#
# run_two_times(Animal())#直接调用，其威力在于调用时只管调用，不管细节，当我们新增一个其父类的子类时，只要保证你需要的方法编写正确即可，
## 不用管之前的代码如何调用的，这就是开闭原则，对子拓展开放，允许新增子类；对于粉笔修改，不需要修改定义在全局下的方法语法函数

#####未封装
# class Student():
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#
#     def info(self):
#         print(f'学生:{self.name};分数:{self.score}')
#
#
# std = Student('xiaoming',95)
# def info(std):
#     print(f'学生:{std.name};分数：{std.score}')
#
# info(std)
# ################封装
# class Student():
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#
#     def info(self):
#         print(f'学生:{self.name};分数:{self.score}')
# # stu = Student()
#
# stu = Student('xiaoming',95)
# print(f'修改前分数:{stu.score}')
# stu.info()#只需要知道创造示例是给我出的name和score其余的都不用去管，你不用知道其内部是怎么样的
#
# stu.score = 0
# print(f'修改后分数:{stu.score}')
# stu.info()
#
# ################################3多重继承
# class Animal(object):
#     pass
#
# # 大类:
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# # 各种动物:
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running...')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
# class Dog(Mammal, Runnable):
#     pass
#
# class Bat(Mammal, Flyable):
#     pass