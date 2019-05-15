class Animal(object):
    def run(self):
        print('Animal is running...')

    def __sleep(self):
        print('这是私有财产。')

    def jump(self):
        print('you jump i  jump')

class Dog(Animal):
    def eat(self):
        print('天啦噜')


    pass


class Cat(Animal):
    pass
dog = Dog()
dog.run()
dog.eat()
# dog.__sleep()###注意此处无法调用父类的私有方法
dog.jump()