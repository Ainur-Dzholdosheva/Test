from abc import ABC, abstractmethod, abstractproperty


# Полиморфизм - разное поведение одного и того же метода в разных классах. Например, мы можем сложить два числа, и можем сложить две строки. При этом получим разный результат, так как числа и строки являются разными классами.
#Полиморфизм — очень важная идея в объектно-ориентированном программировании.
# Получается один и тот же метод то есть знак плюс выполняет разный вывод

# Например

name="Ainur"
surname="Dzholdosheva"
print(name+surname)

a=29
c=34
print(c+a)

#Абстракция – это выделение основных, наиболее значимых характеристик объекта и игнорирование второстепенных.
class AbstractBase(ABC):

    @abstractmethod
    def foo(self):
        pass

    @abstractproperty
    def baz(self):
        pass


class Base(AbstractBase):
    def foo(self):
        print('foo')
    @property
    def baz(self):
        return 'baz'


base = Base()
base.foo()