from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print('this is concrete method')
    @abstractmethod    
    def method3(self):
        pass
class b(a):
    def method1(self):
        print('method1 inherited in subclass b')
    def method3(self):
        print('method3 inherited in sublclass b ')

############
obj1 = b()
obj1.method1()
obj1.method2()
obj1.method3()


